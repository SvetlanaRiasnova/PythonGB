# # Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# # *Пример:*

# # 5
# #     1 2 3 4 5
# #     3
# #     -> 1

N = int(input("Введите количество элементов списка А: "))
A_elem = []
for i in range(0, N):
    A = int(input(f'введите элемент массива {i} // '))
    A_elem.append(A)
print(A_elem)
X = int(input('Введите число X, которое необходимо найти в списке: '))
count = 0
for i in range(N):
        if A_elem[i] == X:
            count += 1
print(f'Число {X} встречается в списке A {count} раз') 