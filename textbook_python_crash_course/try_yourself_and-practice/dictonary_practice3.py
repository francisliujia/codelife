'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print(aliens)
for alien in aliens:
    print(alien)
''
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['points'] == 10
        alien['speed'] == 'medium'
        print(alien)
''
pizza = {
    'crust': 'thick',
    'topplings': ['mushroons', 'extra cheese'],
}
print("You ordered a" + pizza['crust'] +
      "-crust pizza with the following topplings:")

for topping in pizza['topplings']:
    print("\t" + topping)
''

favorite_languages = {
    'francis': ['python', 'ruby'],
    'amanda': ['C'],
    'jannifer': ['ruby', 'go'],
    'philip': ['python', 'java'],
}
for name, languages in favorite_languages.items():
    print(f"\n {name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")
'''


users = {
    'fransdcis': {
        'first': 'francis',
        'last': 'lee',
        'location': 'stirling'
    },

    'gg': {
        'first': 'plamena',
        'last': 'kolewa',
        'location': 'plovdiv'
    },
}

for username, user_info in users.items():
    print(f"\nUsernames: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print("Full name: " + full_name.title())
    print("Location: " + location.title())
