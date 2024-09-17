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

# Вычисляем фазо-частотную характеристику через FFT
fir_phase_response = np.angle(np.fft.fft(fir_impulse))[:10]
iir_phase_response = np.angle(np.fft.fft(iir_impulse))[:10]

# Построим графики
plt.figure(figsize=(10, 5))

# График для КИХ-фильтра
plt.subplot(2, 1, 1)
plt.title("КИХ-фильтр (FIR): Фазо-частотная характеристика")
plt.plot(fir_phase_response, 'r.-')
plt.ylabel("Фаза (рад)")
plt.xlabel("Частота (рад/с)")

# График для БИХ-фильтра
plt.subplot(2, 1, 2)
plt.title("БИХ-фильтр (IIR): Фазо-частотная характеристика")
plt.plot(iir_phase_response, 'g.-')
plt.ylabel("Фаза (рад)")
plt.xlabel("Частота (рад/с)")

# Проверяем корректность фазо-частотной характеристики
assert fir_phase_response.shape[0] == iir_phase_response.shape[0] == 10, f"Bad PR shape. Must be N//2."
_ideal_fir_pr = np.array([-0., -0.15707963, -0.31415927, -0.4712389, -0.62831853, 
                          -0.78539816, -0.9424778, -1.09955743, -1.25663706, -1.41371669])
assert np.allclose(fir_phase_response, _ideal_fir_pr), f"Bad fir PR. diff is {np.abs(fir_phase_response - _ideal_fir_pr).sum()}"

_ideal_iir_pr = np.array([-0., -0.28649379, -0.45845783, -0.52023287, -0.51233491, 
                          -0.46364761, -0.39071251, -0.30300249, -0.20627323, -0.10433379])
assert np.allclose(iir_phase_response, _ideal_iir_pr), f"Bad iir PR. diff is {np.abs(iir_phase_response - _ideal_iir_pr).sum()}"

print("All ok!")

# Отображаем графики
plt.tight_layout()
plt.show()
