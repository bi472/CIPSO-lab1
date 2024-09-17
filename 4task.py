import numpy as np
import matplotlib.pyplot as plt

# Параметры синусоидальных сигналов
A = 1  # амплитуда синусоиды
frequencies = np.logspace(0, 2, 500)  # частоты от 1 до 100 Гц (логарифмическая шкала)
t = np.linspace(0, 1, 1000)  # временная шкала для синусоидальных сигналов
phi = 0  # начальная фаза (нулевая)

# ФЧХ нерекурсивного фильтра по формуле:
# arg(H(e^{jω})) = -arctan(sin(ω) / (1 + cos(ω)))
def non_recursive_phase_response(omega):
    return -np.arctan(np.sin(omega) / (1 + np.cos(omega)))

# ФЧХ рекурсивного фильтра по формуле:
# arg(H(e^{jω})) = -arctan(a sin(ω) / (1 + a cos(ω)))
def recursive_phase_response(omega, alpha=0.5):
    return -np.arctan(alpha * np.sin(omega) / (1 + alpha * np.cos(omega)))

# Рассчитываем фазо-частотные характеристики
phase_non_recursive = non_recursive_phase_response(2 * np.pi * frequencies)
phase_recursive = recursive_phase_response(2 * np.pi * frequencies)

# Строим графики фазо-частотных характеристик
plt.figure(figsize=(10, 6))

# Нерекурсивный фильтр
plt.plot(frequencies, phase_non_recursive, label='Нерекурсивный фильтр', color='blue')

# Рекурсивный фильтр
plt.plot(frequencies, phase_recursive, label='Рекурсивный фильтр', color='green')

# Оформление графика
plt.xscale('log')  # логарифмическая шкала частоты
plt.xlabel('Частота (Гц)')
plt.ylabel('Фаза (рад)')
plt.title('Фазо-частотная характеристика фильтров')
plt.grid(True)
plt.legend()

# Отображаем график
plt.tight_layout()
plt.show()
