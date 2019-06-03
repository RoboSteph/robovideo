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

        #NEEDS TO BE TESTED
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)

        # e_date = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[3]/div/div[1]/a/div/div/div[2]/div/div/div/div[1]")
        # date = e_date.text
        e_test_date = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[31]/div/div[1]/a/div/div/div[2]/div/div/div/div[1]")
        test_date = e_test_date.text

        # e_title = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[3]/div/div[1]/a/div/div/div[2]/div/h5")
        # title = e_tite.text


        # print("Date: " + date)
        # print("Title: " + title)

        time.sleep(3)

        #selecting by page position? Chose third down to avoid breaking affiliate 24hr rules
        # menu_button = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[3]/div/div[1]/a/div/div")
        # menu_button.click()
        test_menu = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div/div/div[5]/div[31]/div/div[1]/a/div/div")
        test_menu.click()

        time.sleep(3)

        export_button = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div[3]/button/div/div[2]")
        export_button.click()

        time.sleep(3)

        #NEEDS TO BE TESTED
        video_description_box = self.browser.find_element_by_xpath("//*[@id=\"ye-description\"]")
        video_description_box.send_keys(test_date)

        start_export_button = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[7]/div[2]/button/div/div")
        start_export_button.click()

        time.sleep(3)

        #NEEDS TO BE TESTED
    def sign_out(self):
        avatar_menu = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[1]/nav/div/div[3]/div[5]/div/div/div/div[1]/button/figure/div[1]/img")
        avatar_menu.click()

        log_out_button = self.browser.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[1]/nav/div/div[3]/div[5]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div/div[5]/button/div/div[2]")
        log_out_button.click()

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