from time import sleep
from locators import ChatLocators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from simon.accounts.pages import LoginPage
from simon.header.pages import HeaderPage
from simon.pages import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as SelTimeOut

# Creating the driver (browser)
s = Service(executable_path='/usr/local/bin/geckodriver/geckodriver', log_path='geckodriver.log')
driver = webdriver.Firefox(service=s)
driver.maximize_window()

driver.get('https://web.whatsapp.com/')
sleep(60)
print('refresh')
driver.refresh()
sleep(30)
print(driver.title)
for key, value in driver.__dict__.items():
    print(key, value)

print(driver.find_element(ChatLocators.CHAT))
# 2. The base page is inherited by all pages
#       and here you can check whether any
#       page is available on the screen of
#       the browser.

# we don't need to load the pages as whatsapp
# # web works as one-page web app
# base_page = BasePage(driver)
# print(base_page.__dict__)
# base_page.is_title_matches()
# base_page.is_welcome_page_available()
# base_page.is_nav_bar_page_available()
# base_page.is_search_page_available()
# base_page.is_pane_page_available()
# # chat is only available after you open one
# base_page.is_chat_page_available()

#
# # 3. Logout
# header_page = HeaderPage(driver)
# header_page.logout()
#
# # Close the browser
# driver.quit()