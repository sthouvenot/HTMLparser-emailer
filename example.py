import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import WebDriverException

#   IMPORTANT: Please fill out the following settings and email condition before 
#   running this script                                                     

hide_ui = False # Set to True to hide the UI, some websites require UI or it detects you as a bot and does not display everything
wait_time = 60 # Adjust the wait time as desired (in seconds)
url = "" # uRL of website to scrape
sender_email = '' # Enter your sender email address
sender_gmail_app_password = '' # Enter your sender email app password (gmail accounts have an app password (seperate from the gmail password) to send emails via python)
receiver_email = ''  # Enter your receiver email address
email_subject = "" # Enter the subject of the email
email_text = "" # Enter the text of the email

def email_condition(soup):

    # The following is an example condition. Replace this with your condition. 

    # It checks that a certain flight is buyable on Southwest by checking that the 9th row's button is enabled. 
    # It first looks for an li element with a specified data-test attribute ("air-booking-select-detail--row-0-9").
    # If the li element is found, it then searches for a div element nested within it with a specific data-test attribute ("fare-button--wanna-get-away").
    # If the div element is found, it checks if it contains a button element that is disabled.
    # If the buttom is disabled, this function returns False - no email sent.
    # If the button is enabled, this function returns True - an email is sent. 
    # If it does not reach the button, it prints that there was an error parsing and returns False.

    # Find the li element with the specified data-test attribute
    li_element = soup.find("li", {"data-test": "air-booking-select-detail--row-0-9"})
    # Check if the li element is found
    if li_element:
        # Find the div element within the li element
        div_element = li_element.find("div", {"data-test": "fare-button--wanna-get-away"})
        # Check if the div is disabled
        if div_element:
            if div_element.find("button", {"disabled": True}):
                print(f"\n {datetime.now()} - The div is disabled \n")   
                return False;           
            else:
                print(f"{datetime.now()} - The div is enabled \n")
                return True;
    print(f"{datetime.now()} - Error parsing  \n")
    return False;

#   From this point foward, the following code can be run unmodified

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--window-size=1280,700")

# Hide UI if set to
if hide_ui:
    chrome_options.add_argument("--headless") 

# Set up the Chrome driver
chrome_driver_path = "chromedriver.exe"
service = Service(chrome_driver_path)

# Define a function to perform the scraping and email sending
def check_and_send_email():
    try:
        # Create a new instance of the Chrome driver
        with webdriver.Chrome(service=service, options=chrome_options) as driver:
            # Open the URL in the browser
            driver.get(url)
            # Get the updated page source after JavaScript execution
            html_content = driver.page_source
            # Parse the HTML content
            soup = BeautifulSoup(html_content, "html.parser")

            if email_condition(soup):
                print(f"{datetime.now()} - Attempting to send email.")
                message = MIMEMultipart("alternative")
                message["Subject"] = email_subject
                message["From"] = sender_email
                message["To"] = receiver_email

                # Attach parts to the message
                part1 = MIMEText(email_text, "plain")
                message.attach(part1)
                # Create secure connection with server and send email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, sender_gmail_app_password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                print(f"{datetime.now()} - Email sent successfully")
    except WebDriverException as e:
        print(f"Exception occurred: {e}")
    except Exception as e:
        print(f"Unhandled exception occurred: {e}")

# Main loop
while True:
    try:
        check_and_send_email()
    except Exception as e:
        print(f"Unhandled exception occurred: {e}")
    time.sleep(wait_time)