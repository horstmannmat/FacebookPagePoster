# SpottedPoster
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
import difflib
from apiclient.http import MediaIoBaseDownload
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
import time
import os
from sys import platform
import signal
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')



class Spotted_Poster(object):

    def __init__(self):
        self.driver = None
        self.email = None
        self.password = None
        self.login = False
        self.drive_service = None
        self.page_url = None


    def facebook_post(self, spotted_message):

        def open_text_area():
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.driver.execute_script("window.scrollTo(0, 100);")
            text_area = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "xc_message")))
            # text_area = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "PageComposerPagelet_")))
            text_area.click()
            return self.driver.switch_to.active_element

        def post_message(spotted_message):
            text_box = open_text_area()
            text_box.clear()
            text_box.send_keys(' ')
            

            logging.info(spotted_message)

            text_box.send_keys(spotted_message)
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

        post_message(spotted_message)

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
        user_email= f.readline().rstrip()
        user_password= f.readline().rstrip()
        f.close()

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
        self.driver_open_url()

    def driver_open_url(self):
        self.driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')

    def sending_login_details(self):
        def send_email():
            em = self.driver.find_element_by_name("email")
            em.clear()
            em.send_keys(self.email)

        def send_password():
            pwd = self.driver.find_element_by_name("pass")
            pwd.clear()
            pwd.send_keys(self.password)
            pwd.send_keys(Keys.RETURN)

        send_email()
        send_password()

    def close(self):
        logging.info("Closing Firefox")

        self.driver.quit()

    def sign_in(self):
        def go_to_page():
            # self.driver.get('https://www.facebook.com/SpottedUFPR3.0/')
            self.driver.get(self.page_url)

        def login_attempt():
            self.getting_login_details()
            logging.info("Logging in...")
            self.sending_login_details()

        while self.login is False:
            login_attempt()
            time.sleep(5)
            self.driver_open_url()

            try:
                self.get_if_loggin_successful()
            except:
                # self.driver.close()

                logging.error("Wrong email or password?")
                global EMAIL
                global PASSWORD
                EMAIL = ""
                PASSWORD = ""
            else:
                self.login = True
                logging.info("Login Successful!")
                go_to_page()


    def setup_google_api(self):
        # Setup the Drive v3 API
        store = file.Storage('credentials.json')
        SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        drive_service = build('drive', 'v3', http=creds.authorize(Http()),cache_discovery=False)
        self.drive_service = drive_service
        logging.info("Google setup finished")


    def download_posts(self):

        def seek_differences():
            with open('spottedOld.tsv', 'r', encoding='utf-8') as fold, \
                open('spottedNew.tsv', 'r', encoding='utf-8') as fnew,\
                open('spottedDiff.tsv', 'wb') as fdiff:
                    diff = difflib.unified_diff(fold.readlines(),fnew.readlines(),fromfile='fold',tofile='fnew',lineterm='\n', n=0)
                    lines = list(diff)[2:]
                    added = [line[1:] for line in lines if line[0] == '+']
                    for line in added:
                        fdiff.write(line.encode('utf-8',errors='strict'))
                    if len(added):
                        logging.info("Created the diff file...")
                    return len(added)


        f = open('sensitive_spreadSheet_data.txt', 'r')
        file_id= f.readline().rstrip()
        f.close()
        request = self.drive_service.files().export_media(fileId=file_id,mimeType='text/tab-separated-values')
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        logging.info("Download finished")
        #write the new file
        with open("spottedNew.tsv","wb") as f:
            wrapper = str(fh.getvalue().decode("utf-8"))
            lines = io.StringIO(wrapper).readlines()
            for line in lines:
                if (line.split("\t")[1] !=  '' ):
                    f.write(line.encode('utf-8',errors='strict'))

            f.write('\n'.encode('utf-8',errors='strict'))

        return seek_differences()




    def post_spotteds(self):
        with open("spottedDiff.tsv","r", encoding='utf-8') as fDiff, open("spottedOld.tsv","ab") as fOld:
            spotteds = fDiff.readlines()


            for spotted in spotteds:
                message = ' '.join([spotted.split("\t")[1],spotted.split("\t")[2],spotted.split("\t")[3]])
                time.sleep(1)
                self.facebook_post(message)

                fOld.write(spotted.encode('utf-8',errors='strict'))

            fOld.write('\n'.encode('utf-8',errors='strict'))

            time.sleep(10)

    def main(self):

        # self.page_url = 'https://www.facebook.com/SpottedUFPR3.0/'
        self.page_url = 'https://m.facebook.com/SpottedUFPR3.0/'

        self.setup_google_api()
        lines_number = self.download_posts()

        if (lines_number):
            self.firing_up_driver()
            self.sign_in()
            self.post_spotteds()
            self.close()

        logging.info("All poster were published ")


def main():
    app = Spotted_Poster()
    app.main()

if __name__ == '__main__':
    main()
