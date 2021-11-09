favorite_numbers = {
    'jelmer': [1, 2, 3],
    'plamela': [12, 22, 123],
    'janiffer': [2, 0, 232],
}
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes these numbers:")
    for number in numbers:
        print("-" + str(number))
