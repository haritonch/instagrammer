from time import sleep
import requests
from selenium import webdriver


class IGBot:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        # the above 2 lines ensure that the webpages will be in english
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')

    def driver(self):
        return self.driver

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(1) # you need to wait for react to build the front end
        username_field = self.driver.find_elements_by_css_selector('input')[0]
        password_field = self.driver.find_elements_by_css_selector('input')[1]
        sleep(1)
        username_field.send_keys(self.username + '\t' + self.password + '\n')
        #password_field.send_keys(self.password + '\n')
        sleep(2)


    def visit(self, some_username):
        self.driver.get('https://www.instagram.com/' + some_username + '/')


    def visitMyProfile(self):
        visit(self.username)


    def follow(self, some_username):
        self.visit(some_username)
        sleep(2)
        try:
            follow_button = self.driver.find_element_by_css_selector('button')
            if follow_button.text == 'Follow':
                follow_button.click()
                sleep(2)
            else:
                print('You are already following', some_username)
        except:
            print("can't find the follow button")
            self.quit()


    def seePhoto(self, photo_id):
        self.driver.get('https://www.instagram.com/p/'+ photo_id +'/')


    def like(self, photo_id):
        self.seePhoto(photo_id)
        sleep(2)
        try:
            xpath = "//span[@aria-label='Like' or @aria-label='Unlike']"
            heart = self.driver.find_elements_by_xpath(xpath)[0]
            if heart.get_attribute('aria-label') == 'Unlike':
                print('You have already liked the photo with id', photo_id)
            else:
                heart.click()
                sleep(1)
        except:
            print("can't find or click the heart button")
            self.quit()


    def quit(self):
        self.driver.quit()
