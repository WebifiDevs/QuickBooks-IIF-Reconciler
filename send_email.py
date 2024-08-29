from email import encoders
from email.mime.base import MIMEBase
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(report_file, recipient_email):
    if not os.path.exists(report_file):
        print(f"Report file {report_file} does not exist.")
        return

    msg = MIMEMultipart()
    msg['From'] = "your_email@example.com"
    msg['To'] = recipient_email
    msg['Subject'] = "Automated Reconciliation Report"

    body = "Please find attached the latest reconciliation report."
    msg.attach(MIMEText(body, 'plain'))

    with open(report_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(report_file)}")
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(msg['From'], "your_password")
        server.sendmail(msg['From'], recipient_email, msg.as_string())
        server.quit()
        print(f"Reconciliation report sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email("./output_files/reconciliation_report.xlsx", "recipient@example.com")
