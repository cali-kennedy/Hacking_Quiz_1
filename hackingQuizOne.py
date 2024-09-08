from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from itertools import product
import time

# Set up the web driver
driver = webdriver.Chrome(executable_path='C:\\Users\\calik\\IdeaProjects\\Hacking_Quiz_1\\chromedriver.exe')



# Create A dictionary of question/answer combos
answer_choices = {
    'q1': ['T', 'F'],
    'q2': ['T', 'F'],
    'q3': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q4': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q5': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q6': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q7': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q8': ['A', 'B', 'C', 'D', 'E', 'F'],
    'q9': ['A', 'B', 'C', 'D'],
    'q10': ['A', 'B', 'C', 'D']
}
# Generate all combinations of answers
all_combinations = list(product(answer_choices['q1'], answer_choices['q2'], answer_choices['q3'],
                                answer_choices['q4'], answer_choices['q5'], answer_choices['q6'],
                                answer_choices['q7'], answer_choices['q8'], answer_choices['q9'],
                                answer_choices['q10']))

# Make sure combination list generated as expected
print("Number of Combinations:", len(all_combinations))

for combination in all_combinations:
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
    time.sleep(1)

    print(f"Trying combination: {combination}")

    # Use a select object to Handle drop down menus
    q1_dropdown = Select(driver.find_element_by_name('TF:1'))
    q1_dropdown.select_by_visible_text(combination[0])

    q2_dropdown = Select(driver.find_element_by_name('TF:2'))
    q2_dropdown.select_by_visible_text(combination[1])

    q3_dropdown = Select(driver.find_element_by_name('MC:3'))
    q3_dropdown.select_by_visible_text(combination[2])

    q4_dropdown = Select(driver.find_element_by_name('MC:4'))
    q4_dropdown.select_by_visible_text(combination[3])

    q5_dropdown = Select(driver.find_element_by_name('MC:5'))
    q5_dropdown.select_by_visible_text(combination[4])

    q6_dropdown = Select(driver.find_element_by_name('MC:6'))
    q6_dropdown.select_by_visible_text(combination[5])

    q7_dropdown = Select(driver.find_element_by_name('MC:7'))
    q7_dropdown.select_by_visible_text(combination[6])

    q8_dropdown = Select(driver.find_element_by_name('MC:8'))
    q8_dropdown.select_by_visible_text(combination[7])

    q9_dropdown = Select(driver.find_element_by_name('MC:9'))
    q9_dropdown.select_by_visible_text(combination[8])

    q10_dropdown = Select(driver.find_element_by_name('MC:10'))
    q10_dropdown.select_by_visible_text(combination[9])

    driver.find_element_by_xpath("//input[@alt='Grade and Submit']").click()
    time.sleep(5)
    # Use JavaScript to click the button
    send_anyway_button = driver.find_element_by_id("proceed-button")
    driver.execute_script("arguments[0].click();", send_anyway_button)
    time.sleep(4)


