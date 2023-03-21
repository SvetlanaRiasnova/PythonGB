# # На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

num = int(input('Введите количество монет' ))
count_heads  = 0
count_tails = 0
for i in range (num):
    x = int(input())
    if x == 0:
        count_heads+=1
    else:
        count_tails+=1

if count_heads > count_tails:
    print("меньшее количество монет со стороной решка", count_tails)
else:
    print("меньшее количество монет со стороной орел", count_heads)