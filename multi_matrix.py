
def MatrixMinMultipli(dims, i, j):
    if j <= i + 1:
        return 0
    minim = float('inf')
    for k in range(i + 1, j):
        left_min = MatrixMinMultipli(dims, i, k)
        right_min = MatrixMinMultipli(dims, k, j)
        cost = left_min + right_min + dims[i] * dims[k] * dims[j]
        if cost < minim:
            minim = cost
    return minim

dims = list(map(int, input('Введите через пробел размеры матриц: ').split()))
print(f'Минимальное количество скалярных операций равно: {MatrixMinMultipli(dims, 0, len(dims) - 1)}')






