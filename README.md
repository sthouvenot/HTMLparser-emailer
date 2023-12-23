# webscraper-mailer

## Overview
This Python project is designed to scrape web pages for specific content and send email notifications based on certain conditions.
It is built with the assumption that Chrome will be used for web scraping and Gmail for sending emails.

## Usage

### Setup Instructions
- **Set up email:** Configure sender email for third-party access [here](https://myaccount.google.com/apppasswords) (requires 2FA enabled). Save your app password.
- **Set up receiver email (optional):** Send a test email to receiver email and add a filter that incoming emails from that address are never sent to spam by following the instructions [here](https://support.google.com/mail/answer/6579?hl=en).
- **Edit settings:** Modify settings in the Python file to customize the scraping and email info.
- **Edit email_condition function:** Customize the logic in the `email_condition` function to determine when emails should be sent.

### Running the Project
To run the project:
1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Follow setup instructions above. 
4. Run the command: `python3 webscraper-mailer.py`
5. If an error occurs, determine if it is a dependency or chromedriver issue and fix by following the instructions below:

### Dependencies
If your computer lacks the necessary dependencies:
- Install Python by typing `python3` in the terminal and following the installation prompts.
- Install required packages by typing: `pip install requests beautifulsoup4 selenium`

### ChromeDriver
If your ChromeDriver is outdated (the version must match your current versoin of chrome)
- Download the updated ChromeDriver from [here](https://googlechromelabs.github.io/chrome-for-testing/).
- Ensure you download "chromedriver" and not "chrome".
- Replace the existing chromedriver file in the project directory with the downloaded one.

### ToDo
- Paid rotating proxy server to avoid IP detection would be ideal. 
