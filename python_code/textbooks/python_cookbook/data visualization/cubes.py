import matplotlib.pylab as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=2)
ax.set_title("Cube numbers", fontsize=23)
ax.set_xlabel("Values", fontsize=12)
ax.set_ylabel("Cubes of value", fontsize=12)
ax.tick_params(axis='both', labelsize=12)
ax.axis([0, 5000, 0, 140000000000])


plt.show()