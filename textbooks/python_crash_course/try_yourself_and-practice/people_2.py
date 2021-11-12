people = []

person = {
    'first_name': 'plamena',
    'second_name': 'kolewa',
    'gender': 'female',
    'age': 26,
    'country': 'burgeria',
    'city': 'plovdiv',
}
people.append(person)
person = {
    'first_name': 'Jelmer',
    'second_name': 'van ginkel',
    'gender': 'male',
    'age': 24,
    'country': 'netherlands',
    'city': 'leiden',
}
people.append(person)
person = {
    'first_name': 'touseef',
    'second_name': 'abbass',
    'gender': 'male',
    'age': 27,
    'country': 'parkstan',
    'city': 'gilgit',
}
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['second_name'].title()
    gender = person['gender']
    age = str(person['age'])
    country = person['country'].title()
    city = person['city'].title()
    print(f"{name}, {gender}, is {age} years old, from {city}, {country}.")
    print(name + ", of " + city + ", is " + age + " years old.")
