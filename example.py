import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the URL to check
url = 'https://example.com'

# Define the condition you want to check (replace this with your logic)
condition = False

# Send a request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Define the condition you want to check (replace this with your logic)

# Replace this with your own logic
if condition:

    # Email configuration // FILL THIS OUT
    sender_email = ''
    receiver_email = ''
    GMAIL_APP_PASSWORD = ''

    message = MIMEMultipart("alternative")
    message["Subject"] = "Alert: Something is True"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Email body
    text = "The condition is true. This is the text version of the email."
    html = "<html><body><p>The condition is true. This is the HTML version of the email.</p></body></html>"

    # Attach parts to the message
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, GMAIL_APP_PASSWORD)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print("Email sent successfully")
else:
    print("Condition is false")