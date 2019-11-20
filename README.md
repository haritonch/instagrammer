# instagrammer
## Yet Another Instagram Bot.

You will need the right version of [chromedriver](https://chromedriver.chromium.org/downloads) in the same directory/folder as Instagrammer.py and main.py.

To initialize a bot you have to `import Instagrammer` in your main.py and run

`bot = Instagrammer('my_username', 'my_password')`



A few things you can currently do using my bot are:
* Follow someone: `bot.follow('username')`
* Like a photo/video: `bot.like('photo_id')`
* Get a list of all photo/video ids from a user's uploads: `bot.getAllPhotosOf('username')`
* Like all photos of a user: `bot.likeAllPhotosOf('username')`
* Comment on a photo/video: `bot.comment('this is my comment', 'photo_id')`
* Get a list with some followers of someone: `bot.someFollowersOf('username')`
* Unfollow someone: `bot.unfollow('username')`
* Like the 24 most recent photos of someone: `bot.likeRecentsOf`

etc.
