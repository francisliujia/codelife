favorite_languages = {
    'francis': 'python',
    'amanda': 'C',
    'jannifer': 'ruby',
    'philip': 'python'
}

friends = ['amanda', 'francis', 'jamison', 'renton', 'lawrence']

for friend in friends:
    if friend in favorite_languages.keys():
        print("Thank you for taking the pool, " + friend.title() + "!")
    else:
        print(friend.title() + ", what is your favorite language?")