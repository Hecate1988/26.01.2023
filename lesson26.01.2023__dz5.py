#Разделить один список на два списка
#Случай 1: в списке четное количество элементов
lst1 = [10, 15, 6, 8, 13, 14, 9, 2, 9, 7]
size = int(len(lst1)/2)
lst2 = [lst1[:size], lst1[size:]]
print(lst2)

#Случай 2: в списке нечетное количество єлементов
lst3 = [3, 8, 6, 12, 5 ]
size = int(len(lst3)/2) + 1
lst4 = [lst3[:size], lst3[size:]]
print(lst4)

#Универсальное решение как для четных так и для нечетных
lst = [10, 15, 6, 8, 13, 14, 9, 2, 9, 7,4, 9]
middle = int(len(lst)/2)
if middle % 2 != 0:
    middle += 1
lstNew = [lst[:middle], lst[middle:]]
print(lstNew)

#Случай 3: список пустой
lst6 = []
middle = int(len(lst6)/2)
if middle % 2 != 0:
    middle += 1
lstN = [lst6[:middle], lst6[middle:]]
print(lstN)

