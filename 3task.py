import numpy as np
import matplotlib.pyplot as plt

# Параметры синусоидальных сигналов
A = 1  # амплитуда синусоиды
frequencies = np.logspace(0, 2, 500)  # частоты от 1 до 100 Гц (логарифмическая шкала)
t = np.linspace(0, 1, 1000)  # временная шкала для синусоидальных сигналов

# Импульсная характеристика нерекурсивного фильтра
def non_recursive_filter(x):
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = (x[i] + x[i - 1]) / 2
    return y

# Импульсная характеристика рекурсивного фильтра
def recursive_filter(x, alpha=0.5):
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = x[i] + alpha * y[i - 1]
    return y

# Рассчитаем амплитудные характеристики для обоих фильтров
amp_non_recursive = []
amp_recursive = []

for f in frequencies:
    signal = A * np.sin(2 * np.pi * f * t)  # генерируем синусоиду
    
    # Нерекурсивный фильтр
    output_non_recursive = non_recursive_filter(signal)
    amp_non_recursive.append(np.max(np.abs(output_non_recursive)))  # находим максимальную амплитуду
    
    # Рекурсивный фильтр
    output_recursive = recursive_filter(signal)
    amp_recursive.append(np.max(np.abs(output_recursive)))

# Строим графики амплитудно-частотной характеристики
plt.figure(figsize=(10, 6))

# Нерекурсивный фильтр
plt.plot(frequencies, amp_non_recursive, label='Нерекурсивный фильтр', color='blue')

# Рекурсивный фильтр
plt.plot(frequencies, amp_recursive, label='Рекурсивный фильтр', color='green')

# Оформление графика
plt.xscale('log')  # логарифмическая шкала частоты
plt.yscale('log')  # логарифмическая шкала амплитуды
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.title('Амплитудно-частотная характеристика фильтров')
plt.grid(True)
plt.legend()

# Отображаем график
plt.tight_layout()
plt.show()
