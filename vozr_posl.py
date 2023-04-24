import copy
import random
n = int(input('Введите длину массива: '))
N = [random.randint(-100, 100) for i in range(n)]
print(f'Сгенерированный массив: {N}')
max_len = [N[0]]
tek_len = [N[0]]
for i in range(1, n):
    if N[i] > N[i - 1]:
        tek_len.append(N[i])
        if len(tek_len) > len(max_len):
            max_len = copy.deepcopy(tek_len)
    else:
        tek_len = [N[i]]

print(f'Наибольшая непрерывная возрастающая последовательность: {max_len}')
  
