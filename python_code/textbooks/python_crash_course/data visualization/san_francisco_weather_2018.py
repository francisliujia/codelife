import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'weather_2018_san_francisco_all.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperature, 2018 \nsan francisco,ca", fontsize=17)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(10, 130)


plt.show()