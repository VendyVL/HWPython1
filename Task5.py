#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print(f'Введите координаты')
x1 = int(input('X1 = '))
y1 = int(input('Y1 = '))
x2 = int(input('X2 = '))
y2 = int(input('Y2 = '))

a = x1-x2
b = y1-y2
res = round(((a**2)+(b**2))**0.5, 3)

print(f'Расстояние между точками А ({x1},{y1}) и В ({x2},{y2}) равно {res}')