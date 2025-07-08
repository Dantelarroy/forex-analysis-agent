import os
import requests
import logging
import json
from dotenv import load_dotenv

load_dotenv()

class AnalyzerTool:
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        self.api_url = 'https://api.groq.com/openai/v1/chat/completions'
        self.model = os.getenv('GROQ_MODEL', 'llama3-70b-8192')

    def analyze_text(self, cleaned_text):
        """
        Envía el texto limpio a la API de Groq y retorna el análisis estructurado y didáctico.
        """
        if not self.api_key:
            logging.error('GROQ_API_KEY no está configurada en el entorno.')
            return None
        prompt = (
            "Eres un analista financiero experto y didáctico. Analiza el siguiente texto de análisis EUR/USD y responde en un JSON con los siguientes campos. Explica todo de forma clara, como si tu audiencia no supiera nada de trading ni de análisis técnico. No des nada por sabido.\n"
            "\n"
            "Estructura de la respuesta (en JSON):\n"
            "{\n"
            "  'resumen': 'Explicación clara y sencilla del análisis, contexto y situación actual',\n"
            "  'soporte_resistencia': [\n"
            "    {'nivel': 'valor', 'tipo': 'soporte' o 'resistencia', 'explicacion': 'qué significa ese nivel y por qué es importante'}\n"
            "  ],\n"
            "  'tendencia': 'alcista, bajista o neutral',\n"
            "  'explicacion_tendencia': 'Explicación didáctica de por qué se considera esa tendencia',\n"
            "  'recomendacion': 'Recomendación clara y justificada para alguien sin experiencia',\n"
            "  'explicacion_recomendacion': 'Explicación didáctica de la recomendación'\n"
            "}\n"
            "\n"
            "Texto a analizar:\n"
            f"{cleaned_text}"
        )
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "Eres un analista financiero didáctico y claro."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            result = response.json()
            content = result['choices'][0]['message']['content']
            # Intentar extraer JSON de la respuesta
            try:
                # Buscar el primer bloque JSON en la respuesta
                start = content.find('{')
                end = content.rfind('}') + 1
                json_str = content[start:end]
                parsed = json.loads(json_str.replace("'", '"'))
                return parsed
            except Exception as e:
                logging.error(f'Error al parsear JSON del LLM: {e}\nRespuesta LLM: {content}')
                return {'error': 'No se pudo parsear la respuesta del LLM', 'raw': content}
        except Exception as e:
            logging.error(f'Error al llamar a la API de Groq: {e}')
            return None 