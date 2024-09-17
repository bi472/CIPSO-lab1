import numpy as np
import matplotlib.pyplot as plt

# Формируем единичный импульс длиной 20 отсчетов
n = 20
impulse = np.zeros(n)
impulse[0] = 1  # единичный импульс в нулевой точке

# Импульсная характеристика нерекурсивного фильтра по формуле:
# h(n) = (δ(n) + δ(n - 1)) / 2
def non_recursive_impulse_response(impulse):
    h = np.zeros_like(impulse)
    for i in range(1, len(impulse)):
        h[i] = (impulse[i] + impulse[i - 1]) / 2
    return h

# Импульсная характеристика рекурсивного фильтра по формуле:
# h(n) = δ(n) + a δ(n - 1)
def recursive_impulse_response(impulse, alpha=0.5):
    h = np.zeros_like(impulse)
    h[0] = impulse[0]  # стартовое значение
    for i in range(1, len(impulse)):
        h[i] = impulse[i] + alpha * h[i - 1]
    return h

# Получаем импульсные характеристики для обоих фильтров
impulse_response_non_recursive = non_recursive_impulse_response(impulse)
impulse_response_recursive = recursive_impulse_response(impulse)

# Строим графики импульсных характеристик
plt.figure(figsize=(10, 5))

# Нерекурсивный фильтр
plt.subplot(1, 2, 1)
plt.stem(range(n), impulse_response_non_recursive, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Импульсная характеристика нерекурсивного фильтра')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')

# Рекурсивный фильтр
plt.subplot(1, 2, 2)
plt.stem(range(n), impulse_response_recursive, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Импульсная характеристика рекурсивного фильтра')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')

# Отображаем графики
plt.tight_layout()
plt.show()
