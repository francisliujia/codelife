import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_deader in enumerate(header_row):
        print(index, column_deader)

    rain_amounts, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain_amount = float(row[3])
        rain_amounts.append(rain_amount)
        dates.append(current_date)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain_amounts, c='pink')

plt.title("Daily rain drop amount, 07/2018,sitka, ca",
          fontsize=15)
plt.xlabel("date", fontsize=11)
plt.ylabel("raindrop", fontsize=11)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()