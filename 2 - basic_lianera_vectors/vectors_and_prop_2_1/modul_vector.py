
import numpy as np

# Создаем вектор
v = np.array([3, 4, 5])

# Вычисляем модуль вектора
norm_v = np.linalg.norm(v)

print("Вычисояем модуль вектора ",norm_v)# 7.0710678118654755


# Создаем двумерный массив
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Вычисляем модуль каждой строки матрицы
norm_rows = np.linalg.norm(A, axis=1)

print("Вычисляем модуль вектора для каждой строки:",norm_rows) # [ 3.74165739  8.77496439 13.92838828]



# Создаемдвумерный массив
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Вычисляем модуль каждого столбца матрицы
norm_cols = np.linalg.norm(B, axis=0)
print("Вычисляем модуль для столбцов:",norm_cols) # [ 8.1240384  9.64365076 11.22497216]



test_point = np.array([6.75, 6.34])
test_point2 = np.array([2.30, 2.42])
radius_vector = test_point - test_point2
result_modul = np.linalg.norm(radius_vector)
print("Результат вычитания двух веторов = радиус вектор",radius_vector)
print("Результат вычитания двух веторов =  модуль вектора",result_modul)
