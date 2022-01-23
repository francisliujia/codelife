import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/weather_2018_san_francisco_all.csv'
place_name = ''

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    dates, highs, lows = [], [], []
    for row in reader:
        if not place_name:
            place_name = row[name_index]
            print(place_name)

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing date for{row[date_index]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='pink', alpha=0.4)
ax.plot(dates, lows, c='purple', alpha=0.4)
plt.fill_between(dates, highs, lows, facecolor='violet', alpha=0.3)

title = f"daily high and low temperature - 2018\n{place_name}"
plt.title(title.title(), fontsize=23)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=11)

plt.show()