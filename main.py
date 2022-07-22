from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

selenium_path = "/home/marcoponce/Documents/Programas/Selenium/drivers/geckodriver-v0.31.0-linux64/geckodriver"
driver = webdriver.Firefox(executable_path=selenium_path)

url = "https://tinder.com/"
driver.get(url=url)
time.sleep(2)

log_in = driver.find_element(By.LINK_TEXT, "Log in")
log_in.click()
time.sleep(2)

sign_in = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
sign_in.click()
time.sleep(2)


base_window = driver.window_handles[0]

fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

# ---------------Sign in to Facebook

facebook_email = "#########"
facebook_password = "#######"

f_email_entry = driver.find_element(By.XPATH, '//*[@id="email"]')
f_password_entry = driver.find_element(By.XPATH, '//*[@id="pass"]')

f_email_entry.send_keys(facebook_email)
f_password_entry.send_keys(facebook_password)
f_password_entry.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(4)


cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div/button')
cookies.click()
allow_location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(2)
allow_notification = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_notification.click()
time.sleep(2)

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
