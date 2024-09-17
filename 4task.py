# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Глобальные параметры
COEFF = 0.5  # Коэффициент для фильтров
FREQUENCY_RANGE = np.linspace(0, 20, num=1000)  # Диапазон частот

# Функция для расчета фазо-частотной характеристики нерекурсивного FIR фильтра
def calculate_fir_phase_response(frequencies):
    return -np.arctan2(np.sin(2 * np.pi * frequencies), 1 + np.cos(2 * np.pi * frequencies))

# Функция для расчета фазо-частотной характеристики рекурсивного IIR фильтра
def calculate_iir_phase_response(frequencies, a1):
    return -np.arctan2(a1 * np.sin(2 * np.pi * frequencies), 1 + a1 * np.cos(2 * np.pi * frequencies))

# Функция для отображения фазо-частотных характеристик
def plot_phase_responses(frequencies, fir_phase, iir_phase):
    plt.figure(figsize=(20, 6))

    # FIR фильтр
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, fir_phase, label='FIR фильтр', color='blue')
    plt.title('Фазо-частотная характеристика FIR фильтра')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Фаза (рад)')
    plt.ylim(-2*np.pi, np.pi)
    plt.grid(True)
    plt.legend()

    # IIR фильтр
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, iir_phase, label='IIR фильтр', color='green')
    plt.title('Фазо-частотная характеристика IIR фильтра')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Фаза (рад)')
    plt.ylim(-2*np.pi, np.pi)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Главная функция, объединяющая расчет и построение графиков
def main():
    # Расчет фазо-частотных характеристик для FIR и IIR фильтров
    fir_phase = calculate_fir_phase_response(FREQUENCY_RANGE)
    iir_phase = calculate_iir_phase_response(FREQUENCY_RANGE, COEFF)

    # Построение графиков
    plot_phase_responses(FREQUENCY_RANGE, fir_phase, iir_phase)

if __name__ == "__main__":
    main()
