from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.debugger_address = 'localhost:9222'
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options) # now webdriver is set


def interact_with_chatgpt(input_text):
    # Open the ChatGPT web page
    driver.get('https://chat.openai.com/chat')

    # Wait for the input field to be ready (you might need to adjust the selector)
    time.sleep(5)  # Adjust this delay as needed

    # Find the input field and enter the text
    input_field = driver.find_element("xpath","//input[@placeholder='what is nepal'?"]")
    input_field.send_keys(input_text)
    input_field.send_keys(Keys.RETURN)

    # Wait for the response (adjust the delay as necessary)
    time.sleep(5)  # Adjust this delay as needed

    # Retrieve the response (you'll need to identify the correct selector)
    response = driver.find_element_by_xpath('xpath_to_response_element').text

    return response

# Read from the input file
with open('input.txt', 'r+') as file:
    input_text = file.read().strip()
    response = interact_with_chatgpt(input_text)
    
    # Append the response to the file
    file.write("\nResponse:\n" + response)

# Close the driver
driver.close()
