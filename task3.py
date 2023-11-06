import numpy as np

colum_1 = np.array([0, 1, 3, 1, 0])
colum_2 = np.array([1, 3, 1, 4, 1])
colum_3 = np.array([4, 1, 3, 5, 4])
colum_4 = np.array([4, 8, 4, 8, 5])
colum_5 = np.array([7, 1, 3, 1, 0])

colum_1.sort()
colum_2.sort()
colum_3.sort()
colum_4.sort()
colum_5.sort()

array = np.column_stack((colum_1, colum_2, colum_3, colum_4, colum_5))
np.fill_diagonal(array, 5)

random_array = np.random.randint(-10, 1, array.shape)
result_array = np.dstack((array, random_array))

print("Исходный массив:")
print(array)
print("Случайный массив:")
print(random_array)
print("Результат объединения:")
print(result_array)