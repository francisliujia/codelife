import random

# value = random.random()
# value = random.uniform(1, 10)
# value = random.randint(1, 6)


# greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
# value = random.choice(greetings)

# print(value + ', Corey!')


# colors = ['red', 'black', 'green']
# # results = random.choices(colors, k=10)
# results = random.choices(colors, weights=[18, 18, 2], k=10)
# print(results)



deck = list(range(1, 53))


hand = random.sample(deck, k=5)

# random.shuffle(deck)
# print(deck)

print(hand)