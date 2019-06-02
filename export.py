import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class ExportVideo():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()

        self.email = email
        self.password = password

    def sign_in(self):
        self.browser.get("https://www.twitch.tv/login")
        email_input = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[1]/div/div[2]/input")
        pass_input = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div/div[1]/div[2]/div[1]/input")

        email_input.send_keys(self.email)
        pass_input.send_keys(self.password)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(3)


    def export_video(self):
        self.browser.get("https://www.twitch.tv/robosteph/manager")
        time.sleep(3)
        #selecting by page position? Chose third down to avoid breaking affiliate 24hr rules
        menu_button = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[3]/div/div[1]/a/div/div")
        menu_button.click()

        #date for this vid - Needs to be tested, was getting captcha
        #//*[@id="root"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[3]/div/div[1]/a/div/div/div[2]/div/div/div/div[1]
        date = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[3]/div/div[1]/a/div/div/div[2]/div/div/div/div[1]").getText()
        print("Date: " + date)

    # def close_browser
    # def exit



f = open("user.config", "r")
l = f.readlines()
email = l[0]
password = l[1]


e = ExportVideo(email, password)
e.sign_in()
e.export_video()







# driver = webdriver.Chrome()

# driver.get("https://www.twitch.tv/robosteph/manager")

# print(driver.title)

# inputElement = driver.find_element_by_name("q")

# inputElement.send_keys("cat")

# inputElement.submit()

# try:
# 	WebDriverWait(driver, 10).until(expected_conditions.title_contains("cat"))

# 	print(driver.title)

# finally:
# 	driver.quit()



####NOTES
#Look into using Get Video API to get video info for posting


#<div data-a-target="login-username-input" class="tw-relative"><input type="text" class="tw-block tw-border-bottom-left-radius-medium tw-border-bottom-right-radius-medium tw-border-top-left-radius-medium tw-border-top-right-radius-medium tw-font-size-6 tw-full-width tw-input tw-pd-l-1 tw-pd-r-1 tw-pd-y-05" autocapitalize="off" autocorrect="off" autocomplete="username" data-a-target="tw-input" value=""></div>