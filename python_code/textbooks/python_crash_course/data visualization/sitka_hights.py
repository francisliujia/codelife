import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

plt.title("Daily high temperature, 2018", fontsize=14)
plt.xlabel('', fontsize=17)
fig.autofmt_xdate()
plt.ylabel('Temperature', fontsize=17)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()