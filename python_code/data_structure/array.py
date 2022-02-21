# exercise1
exp = [2200, 2350, 2600, 2130, 2190]


print(exp[1] - exp[0])

print(exp[0] + exp[1] + exp[2])

print(2000 in exp)

exp.append(1980)
print(exp)

print(exp[3] - 200)


# exercise2
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))

heros.append('black panther')
print(heros)

heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)

heros[1: 3] = ['doctor strange']
print(heros)

print(dir(heros))
heros.sort()
print(heros)


# exercise 3
max = int(input('enter a number:'))

odd_list = []
for i in range(1, max):
	if i % 2 == 1:
		odd_list.append(i)

print(odd_list)






