rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'frazer': 'canada',
    'amazon': 'brazil',
    'volga': 'russia',
}
for river, country in rivers.items():
    print(river.title() + " runs through " + country.title() + ".")
print("The following river are included in this database.")
for river in rivers:
    print("-" + river.title())

print("\n The following countries are includede in this database.")
for country in rivers.values():
    print("-" + country.title())
