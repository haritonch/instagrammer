from getpass import getpass
from IGBot import *
from sys import argv

if __name__ == '__main__':

    if len(argv) == 3:
        username, password = argv[1:3]
    else:
        username = input('Username: ')
        password = getpass('Password: ')

    bot = IGBot(username, password)

    bot.login()
    #bot.follow('hazoviolis') # that's me :P
    #bot.like('B4a2BKep5h-') # that's a photo of mine :P
    bot.getFollowersOf('hazoviolis')

    bot.quit()
