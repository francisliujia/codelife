'''
user_0 = {
    'username': 'elefran',
    'first': 'francis',
    'second': 'lee',
}
for key, value in user_0.items():
    print(f"\nKey:{key.title()}")
    print(f"Value: {value.title()}")

'''
favorite_languages = {
    'francis': 'python',
    'amanda': 'C',
    'jannifer': 'ruby',
    'philip': 'python'
}

friends = ['francis', 'amanda']
'''for name, language in favorite_languages.items():
    print(name.title() + " favourate language is " + language + ".")
print("\n")

for name in favorite_languages.keys():
    print("Hi " + name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(name.title() + ", i see you love " + language + "!")
'''

favorite_languages = {
    'francis': 'python',
    'amanda': 'C',
    'jannifer': 'ruby',
    'philip': 'python'
}

if 'austin' not in favorite_languages.keys():
    print("Austin, plese take our pool!\n")

for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the pool!\n")

for language in favorite_languages.values():
    print(language.title())
print("\n")
for language in set(favorite_languages.values()):
    print(language.title())
