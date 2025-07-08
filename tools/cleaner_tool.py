import re

class CleanerTool:
    def clean_text(self, raw_text):
        """
        Limpia y prepara el texto extraído para análisis semántico.
        - Elimina encabezados redundantes y frases promocionales
        - Normaliza saltos de línea y espacios
        """
        if not raw_text:
            return ''
        # Eliminar encabezados y frases típicas
        patterns = [
            r'^EUR/USD Analysis Summary Today\s*',
            r'^Trading Advice:\s*',
            r'^Technical Levels for the EUR/USD:\s*',
            r"Ready to trade our daily Forex analysis\?.*",
            r"^Today's EUR/USD trading,.*$",
            r"^EUR/USD Trading Signals:.*$",
            r"^EUR/USD Technical Analysis Today:.*$",
            r"^On the monetary policy front,.*$",
            r"^Buy EUR/USD.*$",
            r"^Sell EUR/USD.*$",
        ]
        text = raw_text
        for pat in patterns:
            text = re.sub(pat, '', text, flags=re.MULTILINE)
        # Quitar firmas y frases promocionales al final
        text = re.sub(r'Ready to trade our daily Forex analysis\?.*', '', text, flags=re.DOTALL)
        # Normalizar saltos de línea y espacios
        text = re.sub(r'\n{2,}', '\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip() 