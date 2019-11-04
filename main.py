from getpass import getpass
from IGBot import *
from sys import argv

if __name__ == '__main__':

    if len(argv) == 2:
        username = argv[0]
        password = argv[1]
    else:
        username = input('Username: ')
        password = getpass('Password: ')


    bot = IGBot(username, password)

    bot.login()

    bot.like('B4WAnf5BbRl')

    bot.quit()
