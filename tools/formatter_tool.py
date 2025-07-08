import json
from datetime import datetime

class FormatterTool:
    def format_analysis(self, analysis_data):
        """
        Convierte el análisis JSON en un formato de texto legible y didáctico.
        """
        if not analysis_data or isinstance(analysis_data, str):
            return str(analysis_data)
        
        try:
            # Si es un string JSON, parsearlo
            if isinstance(analysis_data, str):
                analysis_data = json.loads(analysis_data)
            
            # Crear el formato legible
            formatted_text = self._create_readable_format(analysis_data)
            return formatted_text
            
        except Exception as e:
            # Si hay error, devolver el análisis original
            return str(analysis_data)
    
    def _create_readable_format(self, analysis):
        """
        Crea un formato de texto legible a partir del análisis JSON.
        """
        # Encabezado
        formatted = "ANÁLISIS EUR/USD EXPLICADO PASO A PASO\n\n"
        
        # Resumen del análisis
        if 'resumen' in analysis:
            formatted += f"Resumen del análisis:\n{analysis['resumen']}\n\n"
        
        # Niveles clave de soporte y resistencia
        if 'soporte_resistencia' in analysis and analysis['soporte_resistencia']:
            formatted += "Niveles clave de soporte y resistencia:\n"
            for nivel in analysis['soporte_resistencia']:
                formatted += f"- Nivel {nivel['nivel']} ({nivel['tipo']}): {nivel['explicacion']}\n"
            formatted += "\n"
        
        # Tendencia
        if 'tendencia' in analysis:
            formatted += f"Tendencia detectada: {analysis['tendencia']}\n"
            if 'explicacion_tendencia' in analysis:
                formatted += f"Explicación de la tendencia:\n{analysis['explicacion_tendencia']}\n\n"
        
        # Recomendación
        if 'recomendacion' in analysis:
            formatted += f"Recomendación para el lector: {analysis['recomendacion']}\n"
            if 'explicacion_recomendacion' in analysis:
                formatted += f"Explicación de la recomendación:\n{analysis['explicacion_recomendacion']}\n"
        
        return formatted 