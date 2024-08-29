import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_report(matched_file, unmatched_bank_file, unmatched_qb_file, report_file):
    matched = pd.read_csv(matched_file)
    unmatched_bank = pd.read_csv(unmatched_bank_file)
    unmatched_qb = pd.read_csv(unmatched_qb_file)

    with pd.ExcelWriter(report_file) as writer:
        matched.to_excel(writer, sheet_name='Matched Transactions', index=False)
        unmatched_bank.to_excel(writer, sheet_name='Unmatched Bank Transactions', index=False)
        unmatched_qb.to_excel(writer, sheet_name='Unmatched QB Transactions', index=False)
    print(f"Reconciliation report saved to {report_file}")

def send_email(report_file, recipient_email):
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
        part.add_header('Content-Disposition', f"attachment; filename= {report_file}")
        msg.attach(part)

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(msg['From'], "your_password")
    server.sendmail(msg['From'], recipient_email, msg.as_string())
    server.quit()
    print(f"Reconciliation report sent to {recipient_email}")

if __name__ == "__main__":
    generate_report("./output_files/reconciliation_matches.csv", "./output_files/reconciliation_unmatched_bank.csv", "./output_files/reconciliation_unmatched_qb.csv", "./output_files/reconciliation_report.xlsx")
    send_email("./output_files/reconciliation_report.xlsx", "recipient@example.com")
