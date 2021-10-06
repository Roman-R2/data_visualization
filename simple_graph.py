import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Применить стиль
# Узнать доступные стили:
#       import matplotlib.pyplot as plt
#       plt.style.available
plt.style.use('bmh')
fig, ax = plt.subplots()
# Нанести точку на диаграмму. s - размер точки
ax.scatter(2, 4, s=200)
ax.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
