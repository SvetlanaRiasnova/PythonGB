n = int(input('Введите кол-во кустов: '))
list_1 = []
for i in range(n):
    berries = int(input(f'введите  количество ягод на {i + 1} кусте  // '))
    list_1.append(berries)
print(list_1)

res = list()
for i in range(len(list_1)- 1):
    res.append(list_1[i-1] +list_1[i] + list_1[i+1])
    res.append(list_1[-2] + list_1[-1] + list_1[0])
print(max(res))