from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



options = Options()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options) # now webdriver is set

driver.maximize_window()

driver.get("https://chat.openai.com/auth/login")

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID,"login-button"))
)

log_in_button = driver.find_element(By.ID, "login-button")
log_in_button.click()

time.sleep(5)
driver.quit()


