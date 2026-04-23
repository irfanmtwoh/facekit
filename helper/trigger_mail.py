import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv

dotenv.load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, "..", "public", "templates", "email_template.html")



def send_mail_with_template(to_email,  username, password, company_code, confirm_url):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_APP_PASS")
    
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as file:
            template = file.read()

        html_content = (template
                    .replace("{{username}}", username)
                    .replace("{{password}}", password)
                    .replace("{{company_code}}", company_code)
                    .replace("{{confirm_url}}", confirm_url))
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "Your Office Kit Lence Login Details"
        msg["From"] = sender_email
        msg["To"] = to_email

        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(msg["From"], [msg["To"]], msg.as_string())
        print("✅ Email sent successfully!")
        return True
    
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False
