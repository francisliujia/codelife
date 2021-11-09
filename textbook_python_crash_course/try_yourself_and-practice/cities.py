cities = {
    'stirling': {
        'country': 'scotland',
        'population': 36_000,
        'near_cities': 'edinburgh',
    },
    'charlotte': {
        'country': 'usa',
        'population': 885_000,
        'near_cities': 'wilmington',
    },
    'seattle': {
        'country': 'usa',
        'population': 753_000,
        'near_cities': 'kirkland',
    },
}
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = str(city_info['population'])
    near_cities = city_info['near_cities'].title()
    print(f"\n{city.title()} is in {country}: ")
    print(f"It has a population of about {population}.")
    print(f"The near city is {near_cities}.")
