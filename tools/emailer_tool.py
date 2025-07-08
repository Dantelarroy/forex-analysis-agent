import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from dotenv import load_dotenv

load_dotenv()

class EmailerTool:
    def send_email(self, subject, body, recipients):
        """
        Envía un email con el análisis a los destinatarios.
        """
        email_host = os.getenv('EMAIL_HOST')
        email_port = int(os.getenv('EMAIL_PORT', 587))
        email_user = os.getenv('EMAIL_USER')
        email_password = os.getenv('EMAIL_PASSWORD')

        print(f"[DEBUG] Conectando a SMTP: {email_host}:{email_port}")
        print(f"[DEBUG] Usuario: {email_user}")
        print(f"[DEBUG] Destinatarios: {recipients}")

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(email_host, email_port, timeout=30)
            print("[DEBUG] Conexión SMTP establecida.")
            server.ehlo()
            server.starttls()
            print("[DEBUG] TLS iniciado.")
            server.login(email_user, email_password)
            print("[DEBUG] Login exitoso.")
            response = server.sendmail(email_user, recipients, msg.as_string())
            print(f"[DEBUG] Respuesta sendmail: {response}")
            server.quit()
            print("[DEBUG] Conexión SMTP cerrada.")
        except Exception as e:
            print(f"[ERROR] Error al enviar el email: {e}")
            raise 