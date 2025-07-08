# 🚀 Forex Agent - GitHub Actions Setup

Este proyecto automatiza el análisis de EUR/USD usando GitHub Actions para ejecutarse diariamente sin necesidad de mantener tu computadora encendida.

## 📋 Configuración Inicial

### 1. Crear repositorio en GitHub
1. Sube tu código a un repositorio de GitHub
2. Asegúrate de que sea público (gratis) o privado ($4/mes)

### 2. Configurar Secrets en GitHub
Ve a tu repositorio → Settings → Secrets and variables → Actions

Agrega estos secrets:

| Secret | Descripción | Ejemplo |
|--------|-------------|---------|
| `GROQ_API_KEY` | Tu API key de Groq | `gsk_xxxxxxxxxxxxx` |
| `EMAIL_SENDER` | Tu email de Gmail | `tuemail@gmail.com` |
| `EMAIL_PASSWORD` | Contraseña de aplicación Gmail | `abcd efgh ijkl mnop` |
| `EMAIL_RECIPIENTS` | Emails separados por coma | `destino1@gmail.com,destino2@gmail.com` |

### 3. Configurar Gmail App Password
1. Ve a tu cuenta de Google
2. Seguridad → Verificación en 2 pasos → Contraseñas de aplicación
3. Genera una contraseña para "Mail"
4. Usa esa contraseña en `EMAIL_PASSWORD`

## ⚙️ Cómo Funciona

### Workflow Automático
- **Ejecución**: Diariamente a las 9:00 AM UTC (6:00 AM Argentina)
- **Duración**: ~2-3 minutos por ejecución
- **Costo**: Gratis (GitHub Actions incluye 2000 minutos/mes)

### Proceso
1. **Scraping**: Obtiene el último artículo de EUR/USD
2. **Limpieza**: Remueve headers y texto promocional
3. **Análisis**: Usa Groq LLM para análisis semántico
4. **Email**: Envía el análisis por email
5. **Almacenamiento**: Guarda resultados en artifacts

## 🔧 Ejecución Manual

Puedes ejecutar el agente manualmente:
1. Ve a tu repositorio en GitHub
2. Actions → Forex Analysis Agent
3. Click en "Run workflow"

## 📊 Monitoreo

### Ver Logs
1. GitHub → Actions
2. Click en el workflow más reciente
3. Ver logs detallados de cada paso

### Descargar Resultados
1. En la página del workflow
2. Artifacts → forex-analysis-results
3. Descargar archivos de análisis

## 🛠️ Troubleshooting

### Error: "No se encontró el link al artículo"
- Verifica que el sitio web esté funcionando
- Revisa los logs para más detalles

### Error: "Groq API key inválida"
- Verifica que `GROQ_API_KEY` esté correctamente configurado
- Asegúrate de que la key tenga saldo

### Error: "Email no enviado"
- Verifica `EMAIL_SENDER` y `EMAIL_PASSWORD`
- Asegúrate de usar contraseña de aplicación, no la normal

## 📈 Ventajas de GitHub Actions

✅ **100% Automatizado** - No necesita tu computadora
✅ **Gratis** - Para repositorios públicos
✅ **Confiable** - Servidores de GitHub
✅ **Escalable** - Puedes agregar más funcionalidades
✅ **Monitoreo** - Logs y notificaciones integradas
✅ **Open Source** - Todo el código es visible

## 🔄 Personalización

### Cambiar Horario
Edita `.github/workflows/forex-agent.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'  # 9:00 AM UTC
```

### Agregar Notificaciones
Puedes agregar notificaciones a Discord, Slack, etc.

### Múltiples Ejecuciones
Puedes ejecutar múltiples veces al día cambiando el cron.

## 💡 Próximos Pasos

1. **Subir a GitHub**: Crea el repositorio y sube el código
2. **Configurar Secrets**: Agrega las variables de entorno
3. **Probar**: Ejecuta manualmente la primera vez
4. **Monitorear**: Revisa los logs y emails

¡Tu agente Forex estará funcionando 24/7 sin intervención manual! 