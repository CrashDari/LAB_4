#начальные данные(цикл для ввода)
#[1, 10], [2, 15], [3, 20], [4, 25], [5, 30], [6, 35]
exhibits = []
m = int(input('количество проходов:  '))
k = int(input('допустимый вес за проход:  '))
n = ''
cont = 1
while n != ' ':
    print(f'экспонат: {cont}')
    cont+=1
    exhibits.append([int(input('вес:  ')),int(input('ценность:  '))])
    n = input('ещё экспонаты:  ')

def stealer(museum,steps,weight):
    museum = sorted(museum, key=lambda x: x[1]/x[0], reverse=True)# сортировка по ценности за килограмм
    stolen = [] #украденное
    for i in range(steps):
        stolen_step = []
        w = weight # вес, который может унести вор
        for exp in museum:
            if exp[0] <= w:
                stolen_step.append(exp) #2 списка чтобы избежать ошибки, когда удаляем после каждого прохода
                stolen.append(exp)
                w-= exp[0] #вычитаем вес спёртого предмета(вдруг что-то еще можно взять )
        for exp in stolen_step:
            museum.remove(exp) #удаляем всё, что вынесли за этот проход
    print('то, что удалось вынести:  ', stolen)
stolen = stealer(exhibits, m, k)



             
