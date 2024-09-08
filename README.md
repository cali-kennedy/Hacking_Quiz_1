"""
# Automated Brute Force Quiz Solver

This Python program demonstrates how to automate a brute force method to systematically submit different combinations of answers to a specific web-based quiz until all correct answers are found. It uses **Selenium** to interact with the quiz webpage and **IMAP** to retrieve feedback from emails sent by the quiz system.

### **DISCLAIMER**
Any personal information (email addresses, passwords, etc.) found in this repository is purely fictional and not valid. Users are required to replace the information in the code with their own credentials and settings.

---

## Prerequisites

To run this script, you will need the following:

### 1. Python 3.x
Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Selenium
Selenium is used to interact with the web browser. You can install it via `pip`:

    pip install selenium

### 3. WebDriver (ChromeDriver)
You will need the appropriate **ChromeDriver** to control the Chrome browser via Selenium. Download it from the following link:
- [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Make sure the downloaded **chromedriver.exe** is in your project folder or add its path to the system environment variables.

### 4. IMAP and Email Libraries
This script connects to a Gmail account using IMAP to retrieve emails sent by the quiz system. You will also need the following libraries:

    pip install beautifulsoup4

### 5. Gmail Configuration
You will need a Gmail account and enable **"Allow Less Secure Apps"** on your account to allow IMAP connections.
- Instructions: https://myaccount.google.com/lesssecureapps

Ensure that you replace the email and password in the code with your Gmail credentials:

    mail.login('your_email@gmail.com', 'your_app_specific_password')

**Important**: For security reasons, consider using an **App-Specific Password** instead of your regular Gmail password. This can be set up from your Google account's security settings.

---

## Configuration

### 1. ChromeDriver Setup
Download the **ChromeDriver** for your version of Chrome and place it in your project directory. In the code, replace the path for the `ChromeDriver` executable with the path to the one on your machine:

    driver = webdriver.Chrome(executable_path='C:\\path_to_your_chromedriver\\chromedriver.exe')

### 2. Change Email Information
The script will send quiz results to your specified email. Change the email in the JavaScript injection code so that results are sent to your own email:

    email_js = "document.getElementsByName('instructor_email')[0].setAttribute('value', 'your_email@gmail.com');"

### 3. Modify IMAP Login Credentials
Ensure the Gmail credentials used for fetching the feedback emails match your own:

    mail.login('your_email@gmail.com', 'your_app_specific_password')

### 4. Quiz URL
The script is designed to target a specific quiz. 

    driver.get("https://faculty.uca.edu/vparuchuri/4315/4315_quiz1.htm")

---

## Running the Program

Once you have set up everything:

1. Ensure ChromeDriver is in your PATH or modify the script to use its location.
2. Replace the email and password with your own details.
3. Run the script using Python:

    python your_script_name.py

The script will automatically:
- Open the quiz page.
- Submit random answers for each question.
- Retrieve feedback via email.
- Adjust the answers and resubmit until all answers are correct.

---


## Disclaimer

This script is intended for educational purposes only. Do not use it to break the terms of service of any website, quiz, or exam platform.
"""
