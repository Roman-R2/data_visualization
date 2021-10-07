import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)

    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Чтение максимальных температур
    # highs = [int(row[5]) for row in reader]

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
# получает серию значений x и две серии значений y
# и заполняет область между двумя значениями y
# alpha определяет степень прозрачности вывода
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
#  Выводит метки дат по диагонали, чтобы они не перекрывались.
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
