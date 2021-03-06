import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# c - RGB в диапазоне от 0 до 1
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

plt.show()
