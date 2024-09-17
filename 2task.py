import numpy as np
import matplotlib.pyplot as plt

# Определяем единичный скачок длиной 20 отсчетов
n = 20
step = np.ones(n)  # единичный скачок: все значения равны 1

# Переходная характеристика нерекурсивного фильтра
def fir_step_response(step):
    h = np.zeros_like(step)
    # Первый отсчет: среднее между текущим скачком (1) и нулем перед ним
    h[0] = step[0] / 2
    # Цикл для всех остальных отсчетов
    for i in range(1, len(step)):
        h[i] = (step[i] + step[i - 1]) / 2
    return h

# Переходная характеристика рекурсивного фильтра
def iir_step_response(step, alpha=0.5):
    h = np.zeros_like(step)
    h[0] = step[0]  # стартовое значение
    for i in range(1, len(step)):
        h[i] = step[i] + alpha * h[i - 1]
    return h

# Получаем переходные характеристики для обоих фильтров
fir_response = fir_step_response(step)
iir_response = iir_step_response(step)

# Построим графики в одном окне
plt.figure(figsize=(10, 5))

# График для нерекурсивного фильтра
plt.subplot(2, 1, 1)
plt.title("Нерекурсивный фильтр")
plt.stem(step, 'bo-', label='Скачок')
plt.stem(fir_response, 'r.-', label='Фильтр')
plt.legend()
plt.axis([-0.1, len(step), 0, 1.2])

# График для рекурсивного фильтра
plt.subplot(2, 1, 2)
plt.title("Рекурсивный фильтр")
plt.stem(step, 'bo-', label='Скачок')
plt.stem(iir_response, 'g.-', label='Фильтр')
plt.legend()
plt.axis([-0.1, len(step), 0, 2.2])

# Проверяем корректность фильтров
assert step.shape[0] == 20, "Bad step shape"
assert fir_response[0] == 0.5 and (fir_response[1:] == 1).all(), "Bad FIR."
assert iir_response[0] == 1 and iir_response[1] == 1.5 and iir_response[2] == 1.75 and \
       iir_response.mean().round() == 2 and (iir_response < 2).all(), "Bad IIR."
print("All ok!")

# Отображаем графики
plt.tight_layout()
plt.show()
 