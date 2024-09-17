import numpy as np
import matplotlib.pyplot as plt

# Параметры для расчета
n = 20
alpha = 0.5
impulse = np.zeros(n)
impulse[0] = 1  # единичный импульс для фильтров

# Функции для расчета импульсной характеристики
def fir_impulse_response(impulse):
    h = np.zeros_like(impulse)
    h[0] = impulse[0] / 2
    for i in range(1, len(impulse)):
        h[i] = (impulse[i] + impulse[i - 1]) / 2
    return h

def iir_impulse_response(impulse, alpha=0.5):
    h = np.zeros_like(impulse)
    h[0] = impulse[0]
    for i in range(1, len(impulse)):
        h[i] = impulse[i] + alpha * h[i - 1]
    return h

# Получаем импульсные характеристики для обоих фильтров
fir_impulse = fir_impulse_response(impulse)
iir_impulse = iir_impulse_response(impulse)

# Вычисляем амплитудно-частотную характеристику через FFT
fir_response = np.abs(np.fft.fft(fir_impulse))[:10]
iir_response = np.abs(np.fft.fft(iir_impulse))[:10]

# Построим графики
plt.figure(figsize=(10, 5))

# График для КИХ-фильтра
plt.subplot(2, 1, 1)
plt.title("КИХ-фильтр (FIR): Амплитудно-частотная характеристика")
plt.plot(fir_response, 'r.-')
plt.ylabel("Амплитуда")
plt.xlabel("Частота (рад/с)")

# График для БИХ-фильтра
plt.subplot(2, 1, 2)
plt.title("БИХ-фильтр (IIR): Амплитудно-частотная характеристика")
plt.plot(iir_response, 'g.-')
plt.ylabel("Амплитуда")
plt.xlabel("Частота (рад/с)")

# Проверяем корректность амплитудно-частотной характеристики
assert fir_response.shape[0] == iir_response.shape[0] == 10, f"Bad FR shape. Must be N//2."
_ideal_fir_fr = np.array([1., 0.98768834, 0.95105652, 0.89100652, 0.80901699, 
                          0.70710678, 0.58778525, 0.4539905, 0.30901699, 0.15643447])
assert np.allclose(fir_response, _ideal_fir_fr, atol=0.01), f"Bad fir FR. diff is {np.abs(fir_response - _ideal_fir_fr).sum()}"

_ideal_iir_fr = np.array([1.99999809, 1.82896351, 1.50587408, 1.22885364, 
                          1.03088138, 0.89442634, 0.80089238, 0.73765316, 0.69689865, 0.67403739])
assert np.allclose(iir_response, _ideal_iir_fr, atol=0.01), f"Bad iir FR. diff is {np.abs(iir_response - _ideal_iir_fr).sum()}"

print("All ok!")

# Отображаем графики
plt.tight_layout()
plt.show()
