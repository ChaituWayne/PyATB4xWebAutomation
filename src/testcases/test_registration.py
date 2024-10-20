import time
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


@allure.title("Register With Valid User")
@allure.description("Validate whether User is registered or not")
@allure.testcase("TC_01")
@pytest.mark.regression
def test_valid_user_registration():
    # Create WebDriver instance for the browser
    driver = webdriver.Chrome()
    # Maximize window
    driver.maximize_window()
    # Add Implicit wait i.e. Global wait, value should be provided in seconds
    driver.implicitly_wait(10)
    # Navigate to URL
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    # Input First Name in the First Name Text box
    driver.find_element(By.ID, "input-firstname").send_keys("Salaar Devaratha")
    # Input Last Name in the Last Name Text box
    driver.find_element(By.NAME, "lastname").send_keys("Raisaar")
    # Input email id in the Text box
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("khansaarkasalaar@gmail.com")
    # Input telephone number in the Text box
    driver.find_element(By.CSS_SELECTOR, "input[name='telephone']").send_keys("9848032919")
    # Input password in the password text box
    driver.find_element(By.ID, "input-password").send_keys("varadharajamannar")
    # Confirm password
    driver.find_element(By.NAME, "confirm").send_keys("varadharajamannar")
    # select privacy policy checkbox
    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    # Click on Continue button
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(7)
