def printMax(a, b):
    if a == b:
        print(а, 'равно', b)
    elif a < b:
        print(b, 'максимальное')
    else:
        print(а,'максимальное')

printMax(5, 6) #прямая передача данных

#или

x = 3
y = 7
printMax(x, y) #передача данных через переменные