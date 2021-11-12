from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# create two D6 dice
die_1, die_2 = Die(), Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(1, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

frequencies = [results.count(value) for value in range(2, max_results +1)]

x_values = list(range(2, max_results+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of results'}
my_layout = Layout(title='Results of rolling 3 D6 dice 1000 times',
                   xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
print(frequencies)