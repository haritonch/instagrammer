from smartsleep import smartsleep
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagrammer:


    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        # the above 2 lines ensure that the webpages will be in english
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        smartsleep(2) # you need to wait for react to build the front end
        username_field = self.driver.find_element_by_css_selector('input')
        username_field.send_keys(self.username + '\t' + self.password + '\n')
        smartsleep(3)


    def visit(self, some_username):
        self.driver.get('https://www.instagram.com/' + some_username + '/')
        smartsleep(2)


    def visitMyProfile(self):
        visit(self.username)
        smartsleep(2)


    def follow(self, some_username):
        if some_username == self.username:
            print("You can't follow yourself! :P")
            return
        self.visit(some_username)
        smartsleep(2)
        try:
            follow_button = self.driver.find_element_by_css_selector('button')
            if follow_button.text == 'Follow':
                follow_button.click()
                print('I followed', some_username)
                smartsleep(2)
            else:
                print('You are already following', some_username)
        except:
            print("I can't find the follow button")
            self.quit()


    def unfollow(self, some_username):
        if some_username == self.username:
            print("You can't unfollow yourself! :P")
            return
        self.visit(some_username)
        smartsleep(2)
        try:
            following_button = self.driver.find_element_by_css_selector('button')
            if following_button.text == 'Follow':
                print('You are not following', some_username)
                smartsleep(2)
            else:
                following_button.click()
                xpath = "//button[@class and @tabindex]"
                unfollow_button = self.driver.find_element_by_xpath(xpath)
                unfollow_button.click()
                print('I unfolllowed', some_username)
                smartsleep()
        except:
            print("I can't find the follow button")
            self.quit()


    def seePhoto(self, photo_id):
        self.driver.get('https://www.instagram.com/p/'+ photo_id +'/')
        smartsleep(2)


    def like(self, photo_id):
        self.seePhoto(photo_id)
        try:
            xpath = "//span[@aria-label='Like' or @aria-label='Unlike']"
            heart = self.driver.find_element_by_xpath(xpath)
            if heart.get_attribute('aria-label') == 'Unlike':
                print("You have already liked the photo with id", photo_id)
                smartsleep()
            else:
                heart.click()
                smartsleep()
        except:
            print("can't find or click the heart button")
            self.quit()


    def unlike(self, photo_id):
        self.seePhoto(photo_id)
        try:
            xpath = "//span[@aria-label='Like' or @aria-label='Unlike']"
            heart = self.driver.find_elements_by_xpath(xpath)[0]
            if heart.get_attribute('aria-label') == 'Unlike':
                heart.click()
                smartsleep()
            else:
                print("You haven't liked the photo with id", photo_id)
                smartsleep()
        except:
            print("can't find or click the heart button")
            self.quit()


    def someFollowersOf(self, some_username):
        # returns a list with some followers of some_username
        self.visit(some_username)
        xpath = "//a[@href='/"  + some_username + "/followers/']"
        followers_button = self.driver.find_element_by_xpath(xpath)
        followers_button.click()
        smartsleep(2)
        xpath = "//a[@class and @title and @href]"
        followers_elements = self.driver.find_elements_by_xpath(xpath)
        followers = []
        for follower_element in followers_elements:
            followers.append(follower_element.text)
        return followers


    def myFollowers(self):
        return somefollowersOf(self.username)


    def somefolloweesOf(self, some_username):
        self.visit(some_username)
        xpath = "//a[@href='/"  + some_username + "/following/']"
        following_button = self.driver.find_element_by_xpath(xpath)
        following_button.click()
        smartsleep(2)
        xpath = "//a[@class and @title and @href]"
        followees_elements = self.driver.find_elements_by_xpath(xpath)
        followees = []
        for followee_element in followees_elements:
            followees.append(followee_element.text)
        return followees


    def likeRecentsOf(self, some_username):
        self.visit(some_username)
        xpath = "//a[@href]"
        photo_elements = self.driver.find_elements_by_xpath(xpath)
        photo_elements = list(filter(lambda element: '/p/' in element.get_attribute('href') , photo_elements))
        photo_ids = list(map(lambda element: element.get_attribute('href')[28:-1], photo_elements))
        for photo_id in photo_ids:
            self.like(photo_id)
        print('I liked the', len(photo_ids),  'most recent photos of', some_username)


    def likeAllPhotosOf(self, some_username):
        for photo_id in self.getAllPhotosOf(some_username):
            self.like(photo_id)

    def unlikeRecentsOf(self, some_username):
        self.visit(some_username)
        xpath = "//a[@href]"
        photo_elements = self.driver.find_elements_by_xpath(xpath)
        photo_elements = list(filter(lambda element: '/p/' in element.get_attribute('href'), photo_elements))
        photo_ids = list(map(lambda element: element.get_attribute('href')[28:-1], photo_elements))
        for photo_id in photo_ids:
            self.unlike(photo_id)
        print('I unliked the', len(photo_ids),  'most recent photos of', some_username)


    def getAllPhotosOf(self, some_username):
        self.visit(some_username)
        self.scrollToBottom()
        xpath = "//a[@href]"
        photo_elements = self.driver.find_elements_by_xpath(xpath)
        photo_elements = list(filter(lambda element: '/p/' in element.get_attribute('href') , photo_elements))
        photo_ids = list(map(lambda element: element.get_attribute('href')[28:-1], photo_elements))
        return photo_ids


    def comment(self, comment, photo_id):
        self.seePhoto(photo_id)
        xpath = "//textarea"
        comment_element = self.driver.find_element_by_xpath(xpath)
        comment_element.click()
        smartsleep()
        comment_element = self.driver.find_element_by_xpath(xpath)
        comment_element.send_keys(comment)
        post_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        post_button.click()
        smartsleep(2)


    def scrollToBottom(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            smartsleep()
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


    def quit(self):
        self.driver.quit()
