import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === CONFIGURATION ===
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"  # Use an App Password (not your real password)
receiver_email = "recipient@example.com"
subject = "Test Email from Python"
body = "Hello! This is a test email sent using Python."

# === CREATE EMAIL MESSAGE ===
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add the email body
message.attach(MIMEText(body, "plain"))

# === SEND EMAIL ===
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.send_message(message)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", e)
