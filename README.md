# WebScraper-Mailer

## Overview
This Python project is designed to scrape web pages for specific content and send email notifications based on certain conditions.

## Usage

### Python File Structure
- **Edit settings:** Modify settings in the Python file to customize the scraping and email functionality.
- **Edit email_condition function:** Customize the logic in the `email_condition` function to define when emails should be sent.

### Running the Project
To run the project:
1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the command: `python3 webscraper-mailer.py`

### Dependencies
If your computer is outdated or lacks the necessary dependencies:
- Install Python by typing `python3` in the terminal and following the installation prompts.
- Install required packages by typing: `pip install requests beautifulsoup4 selenium`

### ChromeDriver
If your ChromeDriver is outdated:
- Download the updated ChromeDriver from [here](https://googlechromelabs.github.io/chrome-for-testing/).
- Ensure you download "chromedriver" and not "chrome".
- Replace the existing chromedriver file in the project directory with the downloaded one.
