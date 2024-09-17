import numpy as np
import matplotlib.pyplot as plt

# Формируем единичный импульс длиной 20 отсчетов
n = 20
impulse = np.zeros(n)
impulse[0] = 1  # единичный импульс в нулевой точке

# Импульсная характеристика нерекурсивного фильтра по формуле:
# h(n) = (δ(n) + δ(n - 1)) / 2
def fir_impulse_response(impulse):
    h = np.zeros_like(impulse)
    # Первый отсчет: среднее между текущим импульсом (1) и нулем перед ним
    h[0] = impulse[0] / 2
    # Цикл для всех остальных отсчетов
    for i in range(1, len(impulse)):
        h[i] = (impulse[i] + impulse[i - 1]) / 2
    return h

# Импульсная характеристика рекурсивного фильтра по формуле:
# h(n) = δ(n) + a δ(n - 1)
def iir_impulse_response(impulse, alpha=0.5):
    h = np.zeros_like(impulse)
    h[0] = impulse[0]  # стартовое значение
    for i in range(1, len(impulse)):
        h[i] = impulse[i] + alpha * h[i - 1]
    return h

# Получаем импульсные характеристики для обоих фильтров
fir_response = fir_impulse_response(impulse)
iir_response = iir_impulse_response(impulse)

# Построим графики в одном окне
plt.figure(figsize=(10, 5))

# График для нерекурсивного фильтра
plt.subplot(2, 1, 1)
plt.title("Нерекурсивный фильтр")
plt.plot(impulse, 'bo-', label='Импульс')
plt.plot(fir_response, 'r.-', label='Фильтр')
plt.legend()
plt.axis([-0.1, len(impulse), -0.1, 1.2])

# График для рекурсивного фильтра
plt.subplot(2, 1, 2)
plt.title("Рекурсивный фильтр")
plt.plot(impulse, 'bo-', label='Импульс')
plt.plot(iir_response, 'g.-', label='Фильтр')
plt.legend()
plt.axis([-0.1, len(impulse), -0.1, 1.2])

# Проверяем корректность фильтров
assert impulse.shape[0] == 20, "Bad impulse shape"
assert (fir_response[0:2] == 0.5).all() and (fir_response[2:] == 0).all(), "Bad FIR."
assert iir_response.sum().round() == 2 and iir_response.sum() < 2 and (iir_response != 0).all(), "Bad IIR."
assert iir_response[1:].sum().round() == 1 and iir_response[1:].sum() < 1 and iir_response[2:].sum() < 0.5, "Bad IIR."
print("All ok!")

# Отображаем графики
plt.tight_layout()
plt.show()
