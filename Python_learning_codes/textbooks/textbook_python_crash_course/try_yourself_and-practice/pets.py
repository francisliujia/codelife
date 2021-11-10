pets = []
pet = {
    'animal type': 'python',
    'name': 'francis',
    'owner': 'lee',
    'weight': 100,
    'eats': 'meat',
}
pets.append(pet)
pet = {
    'animal type': 'cat',
    'name': 'plamena',
    'owner': 'francis',
    'weight': 70,
    'eats': 'vegetables',
}
pets.append(pet)
pet = {
    'animal type': 'dog',
    'name': 'kaite',
    'owner': 'jelmer',
    'weight': 30,
    'eats': 'carrot',
}
pets.append(pet)

for pet in pets:
    print("\nHere is what i know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ":" + str(value))
