# 102. Send a simple email using smtplib.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver details
sender_email = "your_email@gmail.com"
receiver_email = "receiver@example.com"
password = "your_app_password"  # Use App Password, not your real Gmail password

# Create the email message
message = MIMEMultipart()
message["Subject"] = "Hello from Python"
message["From"] = sender_email
message["To"] = receiver_email

# Add body to the email
body = "This is a test email sent from a Python script."
message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server and send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)
        print(" Email sent successfully!")
except Exception as e:
    print(" Error:", e)
