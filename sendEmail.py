import smtplib

SENDER_EMAIL = ""
SENDER_PASSWORD = ""


def send_email(subject, body, to_email):
    message = f"Subject: {subject}\n\n{body}"
    # Set up the SMTP server
    smtp_server = "smtp.example.com"
    smtp_port = 587
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, message)
        print(f"Email sent to {to_email}")


send_email("Test Subject", "This is a test email body.", "recipient@example.com")
