import random
from array import *
# Массив а)
n = int(10)
sm = int(1)
array1 = [random.randint(1, 10) for i in range(n)]
for i in array1:
    sm = sm * i
print(array1)
print('Cреднее геометрическое одномерного массива:', pow(sm, 1 / n))
# Массив б)
N = 5
M = 5
array2 = []
for i in range(N):
    array2.append([0] * M)
for i in range(N):
    for j in range(M):
        array2[i][j] = random.randint(-10, 10)
for i in range(len(array2)):
    for j in range(len(array2[i])):
        print(array2[i][j], end=' ')
    print()
k = int(0)
for i in range(N):
    for j in range(M-1):
        if array2[i][j] > 0 and array2[i][j-1] < 0 or array2[i][j] < 0 and array2[i][j-1] > 0:
            k = k + 1
print('Элементы меняют знак', k, 'раз')

