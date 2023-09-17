# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
import time

class WebBrowser():
    def setup(self):
        self.url = "https://www.cathaybk.com.tw/cathaybk/"
        self.driver = "chromedriver.exe"
        self.srv = Service(executable_path=self.driver)
        self.browser = webdriver.Chrome(service=self.srv)

    def teardown(self):
        self.browser.quit()

    def homepage(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'cubre-o-footer__copyright')))
        self.browser.set_window_size(750, 1000)
        time.sleep(1)
        
    def card_menu(self):    
        self.browser.find_element(By.XPATH, "//div[@class='cubre-o-header__burger']").click()
        self.browser.find_element(By.XPATH, "//div[text()='產品介紹']").click()
        self.browser.find_element(By.XPATH, "//div[@class='cubre-a-menuSortBtn'][text()='信用卡']").click()
        time.sleep(1)

    def card_introduction(self):
        self.browser.find_element(By.LINK_TEXT, "卡片介紹").click()
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'cubre-o-footer__copyright')))

    def beautifulsoup_and_find(self, html, parser, locator, flag=False, **element):
        soup = BeautifulSoup(html, parser)
        if(flag):
            return soup.find_all(locator, **element)[1]
        else:
            return soup.find_all(locator, **element)

    def browser_find_element(self, element):
        self.browser.find_element(By.XPATH, element).click()
        time.sleep(1)
