# 🤖 Agente de Análisis Forex Automatizado

Un agente inteligente que automatiza el análisis de EUR/USD utilizando web scraping, procesamiento de lenguaje natural y envío de reportes por email.

## ✨ Características

- 🔍 **Web Scraping Automático**: Obtiene análisis diarios de EUR/USD
- 🧹 **Limpieza Inteligente**: Remueve contenido promocional y headers
- 🤖 **Análisis con IA**: Usa Groq LLM para análisis semántico estructurado
- 📧 **Reportes por Email**: Envía análisis diarios automáticamente
- ⚡ **100% Automatizado**: Ejecuta diariamente con GitHub Actions
- 🐳 **Containerizado**: Entorno Docker reproducible

## 🚀 Instalación y Uso

### Requisitos
- Python 3.11+
- Docker (opcional)
- Cuenta de Groq API
- Gmail con contraseña de aplicación

### Configuración Local
```bash
# Clonar repositorio
git clone https://github.com/TU_USUARIO/forex-agent.git
cd forex-agent

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar
python forex_mcp_agent.py
```

### Configuración con Docker
```bash
# Construir imagen
docker build -t forex-agent .

# Ejecutar
docker run --env-file .env forex-agent
```

## 🔧 Configuración de GitHub Actions

Para automatización completa, sigue la guía en [README_GITHUB_ACTIONS.md](README_GITHUB_ACTIONS.md).

## 📁 Estructura del Proyecto

```
├── forex_mcp_agent.py      # Script principal
├── tools/                  # Herramientas del agente
│   ├── scraper_tool.py     # Web scraping
│   ├── cleaner_tool.py     # Limpieza de texto
│   ├── analyzer_tool.py    # Análisis con LLM
│   └── emailer_tool.py     # Envío de emails
├── data/                   # Archivos de análisis
├── .github/workflows/      # Configuración GitHub Actions
└── Dockerfile             # Configuración Docker
```

## 🔑 Variables de Entorno

| Variable | Descripción |
|----------|-------------|
| `GROQ_API_KEY` | API key de Groq |
| `EMAIL_SENDER` | Email de Gmail |
| `EMAIL_PASSWORD` | Contraseña de aplicación Gmail |
| `EMAIL_RECIPIENTS` | Emails destino (separados por coma) |

## 📊 Ejemplo de Salida

El agente genera análisis estructurados como:

```
📊 Análisis EUR/USD - 2024-01-15

🎯 Resumen Ejecutivo:
- Tendencia: Bajista
- Soporte: 1.0850
- Resistencia: 1.0950

📈 Factores Clave:
- Fed mantiene tasas altas
- Inflación europea en descenso
- Riesgo geopolítico moderado

💡 Recomendación:
Mantener posiciones cortas con stop en 1.0950
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## ⚠️ Disclaimer

Este software es solo para fines educativos. No constituye consejo financiero. El trading de Forex conlleva riesgos significativos. 