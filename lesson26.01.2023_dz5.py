#Разделить один список на два списка
#Случай 1: в списке четное количество элементов
lst1 = [10, 15, 6, 8, 13, 14, 9, 2]
lst2 = [lst1[:4], lst1[4:]]
print(lst2)

#Случай 2: в списке нечетное количество єлементов
lst3 = [3, 8, 6, 12, 5 ]
lst4 = [lst3[:3], lst3[3:]]
print(lst4)

#Случай 3: список пустой
lst5 = [ ]
lst6 = [lst5, lst5]
print(lst6)
