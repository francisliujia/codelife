favorite_pizzas = ["margherita pizza", "peperoni pizza", "bbq chichen pozza"]
friend_pizas = favorite_pizzas[:]
print(friend_pizas)
favorite_pizzas.append("meat lover's")
friend_pizas.append("pesto")

print("my favorite pizzas are:")
for pizza in favorite_pizzas:
    print("\t" + pizza.title())


print("My friend's favorite pizzas are:")
for pizza in favorite_pizzas:
    print("\t" + pizza.title())
