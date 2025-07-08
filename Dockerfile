# Usar Python 3.11 como base
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    procps \
    libxss1 \
    && rm -rf /var/lib/apt/lists/*

# Instalar Playwright y navegadores
RUN pip install playwright
RUN playwright install chromium
RUN playwright install-deps

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Crear directorio de datos
RUN mkdir -p data

# Variables de entorno por defecto
ENV PYTHONPATH=/app
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Comando por defecto
CMD ["python", "forex_mcp_agent.py"] 