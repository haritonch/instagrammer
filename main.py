from getpass import getpass
from IGBot import Instagrammer
from sys import argv

if __name__ == '__main__':

    if len(argv) == 3:
        username, password = argv[1:3]
    else:
        username = input('Username: ')
        password = getpass('Password: ')

    bot = IGBot(username, password)

    bot.login()

    bot.unfollow('bucks')
    bot.follow('bucks')

    print('some people the bucks follow:')
    for account in bot.followeesOf('bucks'):
        print(' ', account)

    bot.likeRecentsOf('bucks')
    bot.unlikeRecentsOf('bucks')

    bot.quit()
