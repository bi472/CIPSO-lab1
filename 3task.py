
import numpy as np
import matplotlib.pyplot as plt

# Глобальные параметры
COEFF = 0.4  # Коэффициент для фильтров
FREQUENCY_RANGE = np.linspace(0, 25, num=1200)  # Диапазон частот

# Функция для расчета амплитудной характеристики FIR фильтра
def calculate_fir_response(frequencies):
    return np.sqrt((1 + np.cos(2 * np.pi * frequencies)) / 2)


# Функция для расчета амплитудной характеристики IIR фильтра
def calculate_iir_response(frequencies):
    return 1 / np.sqrt(1 - 2 * COEFF * np.cos(2 * np.pi * frequencies) + COEFF**2)

# Функция для отображения графиков
def plot_responses(frequencies, fir_response, iir_response):
    plt.figure(figsize=(20, 6))

    # FIR фильтр
    plt.subplot(2, 1, 1)
    plt.plot(frequencies, fir_response, label='FIR фильтр', color='blue')
    plt.title('Амплитудно-частотная характеристика FIR фильтра')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.ylim(0, 2)
    plt.grid(True)
    plt.legend()

    # IIR фильтр
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, iir_response, label='IIR фильтр', color='green')
    plt.title('Амплитудно-частотная характеристика IIR фильтра')
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.ylim(0, 2)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Главная функция, объединяющая расчет и построение графиков
def main():
    # Расчет характеристик для FIR и IIR фильтров
    fir_response = calculate_fir_response(FREQUENCY_RANGE)
    iir_response = calculate_iir_response(FREQUENCY_RANGE)

    # Построение графиков
    plot_responses(FREQUENCY_RANGE, fir_response, iir_response)

if __name__ == "__main__":
    main()
