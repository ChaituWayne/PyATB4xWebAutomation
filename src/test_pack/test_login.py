from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from src.Utilities.BaseClass import BaseClass


class test_sample(BaseClass):

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
