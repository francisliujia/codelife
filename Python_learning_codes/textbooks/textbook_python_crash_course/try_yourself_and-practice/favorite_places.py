favorite_places = {
    'plamena kolewa': ['sophia', 'stirling', 'ediburgh'],
    'jelmer van ginkel': ['armsterdan', 'rotterdam', 'berlin'],
    'helen kepelian': ['athen', 'glasgow', 'inverness'],
}
for name, places in favorite_places.items():
    print("\n" + name.title() + " likes these places:")
    for place in places:
        print("\t -" + place.title())
