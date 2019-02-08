# FacebookPagePoster
# This file is part of the spottedPoster distribution (https://github.com/horstmannmat/spottedPoster).
# Copyright (C) 2018 Matheus Horstmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, print_function
import io
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)



class FacebookPagePoster(object):

    def __init__(self):
        self.driver = None
        self.email = None
        self.password = None
        self.login = False
        self.drive_service = None
        self.page_url = None


    def facebook_post(self, message):

        def open_text_area():
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.driver.execute_script("window.scrollTo(0, 100);")
            text_area = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "xc_message")))
            # text_area = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "PageComposerPagelet_")))
            text_area.click()
            return self.driver.switch_to.active_element

        def post_message(message):
            text_box = open_text_area()
            text_box.clear()
            text_box.send_keys(' ')


            logging.info(message)

            text_box.send_keys(message)
            post_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "view_post")))
            post_button.click()
            # time.sleep(4)

            # if platform == "linux" or platform == "linux2" or platform == "win32" or platform == "win64":
            # # linux or windows
            #     text_box.send_keys(Keys.CONTROL,Keys.RETURN)
            #
            # elif platform == "darwin":
            # # OS X
            #     text_box.send_keys(Keys.COMMAND,Keys.RETURN)

        post_message(message)
    def sending_login_details(self):
        def send_email():
            em = self.driver.find_element(By.XPATH,'//*[@id="m_login_email"]')
            em.clear()
            em.send_keys(self.email)

        def send_password():
            pwd = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/div[2]/div[2]/form/ul/li[2]/div/input')
            # pwd = self.driver.find_element_by_name("pass")
            pwd.clear()
            pwd.send_keys(self.password)
            pwd.send_keys(Keys.RETURN)

        send_email()
        send_password()

    def get_if_loggin_successful(self):
        
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "pagelet_composer")))

    def getting_login_details(self):

        def ask_email():
            email = input("What's your FB email? >> ") if len(
                user_email) == 0 else user_email
            self.email = email

        def ask_password():
            import getpass
            password = getpass.getpass("What's your FB password? >> ") if len(
                user_password) == 0 else user_password
            self.password = password


        f = open('facebook_credentials.txt', 'r')
        user_email= config.EMAIL
        user_password= config.PASSWORD

        ask_email()
        ask_password()

    def firing_up_driver(self):
        def initialize_driver():
            try:  # Linux
                profile = webdriver.FirefoxProfile()
                profile.set_preference("browser.cache.disk.enable", False)
                profile.set_preference("browser.cache.memory.enable", False)
                profile.set_preference("browser.cache.offline.enable", False)
                profile.set_preference("permissions.default.desktop-notification", 1);
                profile.set_preference("network.http.use-cache", False)
                profile.set_preference("keep_alive",False)
                options = webdriver.FirefoxOptions()
                # options.add_argument('-headless')
                logging.info("Initializing Firefox")


                self.driver = webdriver.Firefox(profile,options=options)

                # logging.info("Initializing Chrome")
                # chrome_options = webdriver.ChromeOptions()
                #
                # chrome_options.add_argument("--disable-notifications")
                # self.driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

                # logging.info("Initializing Safari")
                # os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
                # self.driver = webdriver.Safari()

                # self.driver.implicitly_wait(3)
            except Exception as error:
                logging.error("Can't initialize Firefox")
                logging.error(type(error))    # the exception instance
                logging.error(error.args)     # arguments stored in .args
                logging.error(error)
            else:
                logging.info("Setup successful")

        initialize_driver()
        self.driver.get('https://m.facebook.com/login.php?login_attempt=1&lwv=110')

    def close(self):
        logging.info("Closing Firefox")
        self.driver.quit()

    def sign_in(self):
        def go_to_page():
            self.driver.get(self.page_url)

        def login_attempt():
            self.getting_login_details()
            logging.info("Logging in...")
            self.sending_login_details()

        while self.login is False:
            login_attempt()
            time.sleep(2)
            self.driver_open_url()

            try:
                self.get_if_loggin_successful()
            except:
                logging.error("Wrong email or password?")
            else:
                self.login = True
                logging.info("Login Successful!")
                go_to_page()






def main():
    app = Spotted_Poster()
    app.main()

if __name__ == '__main__':
    main()
