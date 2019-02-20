# FacebookPagePoster
# This file is part of the FacebookPagePoster distribution (https://github.com/horstmannmat/FacebookPagePoster).
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
import re
import config


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class FacebookPagePoster(object):

    def __init__(self):
        self.driver = None
        self.email = None
        self.password = None
        self.login = False
        self.drive_service = None
        self.page_url = None
        self.page_id = None


    def delete(self, story_fbid):
        def delete():
            self.driver.get('https://m.facebook.com/story.php?story_fbid='+story_fbid+'&id='+self.page_id)
            delete_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[1]/div[1]/table/tbody/tr/td[2]/div/div/a[2]')
            delete_button.click()
            confirm_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/form/input[3]')
            confirm_button.click()

        try:
            logger.info("Deleting Post")
            delete()
        except:
            logger.info("Post not Found")
            return None
        else:
            logger.info("Post Deleted")
            return True


    def post_image(self, message, image_path, filter = None):
        def send_image():
            image_area = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div[4]/form/div/span/div[1]/table/tbody/tr/td[2]/input')
            image_area.click()
            upload_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/form/div[1]/div/input[1]')
            upload_button.send_keys(image_path)
            if filter == "Enhance":
                x_path = '/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/form/div[3]/div/fieldset/label[1]/div/table/tbody/tr/td[1]/input'
            elif filter == "B&W":
                x_path = '/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/form/div[3]/div/fieldset/label[2]/div/table/tbody/tr/td[1]/input'
            elif filter == "Retro":
                x_path = '/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/form/div[3]/div/fieldset/label[3]/div/table/tbody/tr/td[1]/input'
            else:
                x_path = '/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/form/div[3]/div/fieldset/label[4]/div/table/tbody/tr/td[1]/input'

            self.driver.find_element(By.XPATH,x_path).click()
            time.sleep(100)

            self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/form/div[3]/input[1]').click()

        def send_message():
            text_box = self.driver.find_element(By.XPATH,'//*[@id="u_0_0"]')
            text_box.click()
            text_box.clear()
            text_box.send_keys(message)
            post_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/div/form/input[20]')
            post_button.click()

        send_image()
        send_message()

    def post(self, message):

        def open_text_area():

            text_area = self.driver.find_element(By.XPATH,'//*[@id="u_0_0"]')
            text_area.click()
            return self.driver.switch_to.active_element

        def post_message(message):
            text_box = open_text_area()
            text_box.clear()
            text_box.send_keys(' ')


            logger.info(message)


            text_box.send_keys(message)
            post_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div[4]/form/table/tbody/tr/td[3]/div/input')
            post_button.click()


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
        one_tap = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/table/tbody/tr/td/div/h3')))
        return one_tap.text == "Log In With One Tap" or WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/form/table/tbody/tr/td[2]/input')))

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


        user_email= self.email or config.EMAIL
        user_password= self.password or config.PASSWORD

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
                options.add_argument('-headless')
                logger.info("Initializing Firefox")


                self.driver = webdriver.Firefox(profile,options=options)

                # logger.info("Initializing Chrome")
                # chrome_options = webdriver.ChromeOptions()
                #
                # chrome_options.add_argument("--disable-notifications")
                # self.driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

                # logger.info("Initializing Safari")
                # os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-2.41.0.jar"
                # self.driver = webdriver.Safari()

                # self.driver.implicitly_wait(3)
            except Exception as error:
                logger.error("Can't initialize Firefox")
                logger.error(type(error))    # the exception instance
                logger.error(error.args)     # arguments stored in .args
                logger.error(error)
            else:
                logger.info("Setup successful")

        initialize_driver()
        self.driver.get('https://m.facebook.com/login.php?login_attempt=1&lwv=110')

    def close(self):
        logger.info("Closing Firefox")
        self.driver.quit()

    def setup(self, page_id, email, password):
        self.page_url = 'https://m.facebook.com/' + page_id + '/'
        self.firing_up_driver()
        self.sign_in()
        self.email = email
        self.password = password


    def sign_in(self):
        def go_to_page():
            self.driver.get(self.page_url)

        def get_page_id():
            img = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div/div[1]/div/a')
            img_url = img.get_attribute('href')
            regex = r"https:\/\/.*profile_id="
            page_id = re.sub(regex, "", img_url)
            self.page_id = page_id

        def login_attempt():
            self.getting_login_details()
            logger.info("Logging in...")
            self.sending_login_details()

        while self.login is False:
            login_attempt()

            try:
                self.get_if_loggin_successful()
            except:
                logger.error("Wrong email or password?")
            else:
                self.login = True
                logger.info("Login Successful!")
                go_to_page()
                get_page_id()
