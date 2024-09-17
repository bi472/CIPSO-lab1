import numpy as np

# Пример значений частот (ω)
omega_values = np.linspace(0, np.pi, 5)  # частоты от 0 до Пи (для примера)

# Амплитудно-частотная характеристика нерекурсивного фильтра:
def amplitude_non_recursive(omega):
    return np.sqrt((1 + np.cos(omega)) / 2)

# Фазо-частотная характеристика нерекурсивного фильтра:
def phase_non_recursive(omega):
    return -np.arctan(np.sin(omega) / (1 + np.cos(omega)))

# Амплитудно-частотная характеристика рекурсивного фильтра (с a = 0.5):
def amplitude_recursive(omega, a=0.5):
    return 1 / np.sqrt(1 - 2 * a * np.cos(omega) + a**2)

# Фазо-частотная характеристика рекурсивного фильтра (с a = 0.5):
def phase_recursive(omega, a=0.5):
    return -np.arctan(a * np.sin(omega) / (1 + a * np.cos(omega)))

# Рассчитаем вручную для нескольких частот
amp_non_recursive = amplitude_non_recursive(omega_values)
phase_non_recursive_result = phase_non_recursive(omega_values)

amp_recursive = amplitude_recursive(omega_values, a=0.5)
phase_recursive_result = phase_recursive(omega_values, a=0.5)

# Выведем результаты
print("Амплитудно-частотная характеристика нерекурсивного фильтра:", amp_non_recursive)
print("Фазо-частотная характеристика нерекурсивного фильтра:", phase_non_recursive_result)
print("Амплитудно-частотная характеристика рекурсивного фильтра:", amp_recursive)
print("Фазо-частотная характеристика рекурсивного фильтра:", phase_recursive_result)
