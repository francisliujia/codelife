import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_date(filename, dates, lows, highs,
                     date_index, high_index, low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"missing date for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_date(filename, dates, highs, lows, date_index=2,
                 high_index=5, low_index=6)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates, highs, c='pink', alpha=0.3)
ax.plot(dates, highs, c='purple', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='violet', alpha=0.5)

filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_date(filename, dates, highs, lows, date_index=2,
                 high_index=4, low_index=5)

ax.plot(dates, highs, c='pink', alpha=0.5)
ax.plot(dates, highs, c='purple', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

title = "Dealy high and low temperature, 2018"
title += "\nsitka, AK, death valley, ca"
plt.title(title, fontsize=14)
plt.xlabel('', fontsize=11)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=11)
plt.ylim(10, 130)

plt.show()