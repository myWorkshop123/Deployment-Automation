import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from constant import OUTLOOK


def send_mail(subject, body):
    # Email details

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = OUTLOOK.SENDER_EMAIL
    message["To"] = ",".join(OUTLOOK.RECEIEVER_EMAIL)
    message["Cc"] = ",".join(OUTLOOK.CC_EMAIL)
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the server and send the email
    server = None
    try:
        # Connect to the Outlook SMTP server
        server = smtplib.SMTP(OUTLOOK.SMTP_SERVER, OUTLOOK.SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(OUTLOOK.SENDER_EMAIL, OUTLOOK.SENDER_PASSWORD)

        # Send the email
        server.send_message(message)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    finally:
        # Terminate the SMTP session and close the connection
        server.quit() if server else None


if __name__ == "__main__":
    send_mail("Test Email", "This is a test email.")
