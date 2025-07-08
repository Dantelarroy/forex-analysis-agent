from playwright.sync_api import sync_playwright
import logging
import re

class ScraperTool:
    BASE_URL = "https://www.dailyforex.com"
    LIST_URL = f"{BASE_URL}/forex-technical-analysis/eur-usd-forecast/page-1"

    def get_latest_article_link(self) -> str:
        """
        Busca el primer enlace de artículo individual de EUR/USD Analysis y retorna la URL completa.
        """
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(self.LIST_URL, timeout=30000)
                links = page.query_selector_all('a')
                pattern = re.compile(r'/forex-technical-analysis/\d{4}/\d{2}/eurusd-analysis-.*?/\d+$')
                for link in links:
                    href = link.get_attribute('href')
                    if href and pattern.search(href):
                        url = href if href.startswith('http') else self.BASE_URL + href
                        browser.close()
                        return url
                browser.close()
                logging.error('No se encontró el enlace al artículo individual más reciente.')
                return None
        except Exception as e:
            logging.error(f'Error al obtener el enlace del artículo: {e}')
            return None

    def get_article_content(self, url: str) -> dict:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url, timeout=30000)
                html = page.content()
                with open('articulo_debug.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                print('HTML del artículo guardado en articulo_debug.html')
                title = page.query_selector('h1')
                title_text = title.inner_text().strip() if title else ''
                # Extraer el cuerpo del análisis desde el div correcto
                body_elem = page.query_selector('div.content-body.article-content')
                body_text = body_elem.inner_text().strip() if body_elem else ''
                browser.close()
                return {
                    'title': title_text,
                    'body': body_text,
                    'url': url
                }
        except Exception as e:
            logging.error(f"Error al extraer contenido del artículo: {e}")
            return None 