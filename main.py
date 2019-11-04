from getpass import getpass
from instagrammer import Instagrammer
from sys import argv

if __name__ == '__main__':

    if len(argv) == 3:
        username, password = argv[1:3]
    else:
        username = input('Username: ')
        password = getpass('Password: ')

    bot = Instagrammer(username, password)

    bot.login()

    bot.unfollow('bucks')
    bot.follow('bucks')

    print('some accounts the bucks follow:')
    for account in bot.followeesOf('bucks'):
        print('   ', account)

    for i in range(3):
        bot.likeRecentsOf('bucks')
        bot.unlikeRecentsOf('bucks')

    bot.quit()
