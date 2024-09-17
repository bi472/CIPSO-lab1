import numpy as np
import matplotlib.pyplot as plt

# Определяем единичный скачок длиной 20 отсчетов
n = 20
step = np.ones(n)

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

# Применяем фильтры к единичному скачку

# Импульсная характеристика для нерекурсивного фильтра на единичном скачке
step_response_non_recursive = non_recursive_impulse_response(step)

# Импульсная характеристика для рекурсивного фильтра на единичном скачке
step_response_recursive = recursive_impulse_response(step)

# Строим графики для единичного скачка
plt.figure(figsize=(10, 5))

# Нерекурсивный фильтр
plt.subplot(1, 2, 1)
plt.stem(range(n), step_response_non_recursive, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Переходная характеристика нерекурсивного фильтра (единичный скачок)')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')

# Рекурсивный фильтр
plt.subplot(1, 2, 2)
plt.stem(range(n), step_response_recursive, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Переходная характеристика рекурсивного фильтра (единичный скачок)')
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')

# Отображаем графики
plt.tight_layout()
plt.show()
