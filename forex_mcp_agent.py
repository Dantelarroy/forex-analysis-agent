import os
import logging
from datetime import datetime
from tools.scraper_tool import ScraperTool
from tools.cleaner_tool import CleanerTool
from tools.analyzer_tool import AnalyzerTool
from tools.emailer_tool import EmailerTool
from tools.formatter_tool import FormatterTool
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info('Iniciando flujo MCP Forex...')
    scraper = ScraperTool()
    cleaner = CleanerTool()
    analyzer = AnalyzerTool()
    formatter = FormatterTool()
    emailer = EmailerTool()
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)
    recipients = os.getenv('EMAIL_RECIPIENTS', '').split(',')
    recipients = [r.strip() for r in recipients if r.strip()]

    # 1. Scraping
    url = scraper.get_latest_article_link()
    if not url:
        logging.error('No se encontró el link al artículo más reciente.')
        return
    article = scraper.get_article_content(url)
    if not article or not article['body']:
        logging.error('No se pudo extraer el contenido del artículo.')
        return
    logging.info(f"Artículo extraído: {article['title']}")

    # 2. Limpieza
    cleaned = cleaner.clean_text(article['body'])
    logging.info('Texto limpio listo para análisis.')

    # 3. Análisis LLM
    analysis = analyzer.analyze_text(cleaned)
    if not analysis:
        logging.error('No se pudo obtener el análisis del LLM.')
        return
    logging.info('Análisis LLM recibido.')

    # 4. Formatear análisis
    formatted_analysis = formatter.format_analysis(analysis)
    logging.info('Análisis formateado listo.')

    # 5. Guardar en /data
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"eurusd_analysis_{timestamp}.txt"
    filepath = os.path.join(data_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Título: {article['title']}\n")
        f.write(f"URL: {article['url']}\n\n")
        f.write(formatted_analysis)
    logging.info(f'Análisis guardado en {filepath}')

    # 6. Enviar email
    subject = f"Análisis EUR/USD Diario - {datetime.now().strftime('%Y-%m-%d')}"
    body = f"Título: {article['title']}\nURL: {article['url']}\n\n{formatted_analysis}"
    try:
        emailer.send_email(subject, body, recipients)
        logging.info(f'Email enviado a: {", ".join(recipients)}')
    except Exception as e:
        logging.error(f'Error al enviar el email: {e}')

if __name__ == '__main__':
    main() 