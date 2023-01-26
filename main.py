from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import json
import time


class TinderSwiper:
    def __init__(self,data):
        """This section contains data rom config.json"""
        self.email = data['email']
        self.password = data['password']
        self.driver = webdriver.Chrome(executable_path=data['driver_path'])    

    def login_tinder(self):
        """This section works for login into tinder account"""
        self.driver.get("https://tinder.com/")
        base_window = self.driver.window_handles[0]
        
        time.sleep(10)
        ignore_cookies = self.driver.find_element(By.XPATH, value='//*[@id="q-1380955487"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]').click()
        login_button = self.driver.find_element(By.LINK_TEXT, value='Log in')
        login_button.click()
        time.sleep(3)
        facebook_login = self.driver.find_element(By.XPATH, value='//*[@id="q1185630733"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
        facebook_login.click()
        time.sleep(5)

        fb_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_login_window)
        only_essential_cookies = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[1]').click()
        time.sleep(3)
        email = self.driver.find_element(By.ID, value="email")
        email.clear()
        email.send_keys(self.email)
        time.sleep(3)
        password = self.driver.find_element(By.ID, value="pass")
        password.clear()
        password.send_keys(self.password)
        time.sleep(2)
        fb_login = self.driver.find_element(By.ID, value="loginbutton")
        fb_login.click()
        time.sleep(10)
        self.driver.switch_to.window(base_window)

        allow_location = self.driver.find_element(By.XPATH, value="//button[@aria-label='Allow']").click()
        time.sleep(3)
        enable_location = self.driver.find_element(By.XPATH, value="//button[@aria-label='Not interested']").click()
        time.sleep(8)
        try:
            ignore_mode_adjustment = self.driver.find_element(By.XPATH, value='//*[@id="q1185630733"]/main/div/div[2]/button').click()
        except NoSuchElementException:
            time.sleep(20)
            ignore_mode_adjustment = self.driver.find_element(By.XPATH, value='//*[@id="q1185630733"]/main/div/div[2]/button').click()
        time.sleep(10)
        for n in range(100):
            try:
                # We have a problem finding like button
                like_button = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')
                like_button.click()
                
            except ElementClickInterceptedException:
                try:
                    match_popup = self.driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
                    match_popup.click()
                #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
                except NoSuchElementException:
                    time.sleep(2)


if __name__ == "__main__":
    with open("config.json") as config_file:
        data = json.load(config_file)

    bot = TinderSwiper(data)
    
    bot.login_tinder()
    







