#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

import math

arrCoord = ["x1", "y1", "x2", "y2"]
arr = []
for i in range(4):
    arr.append(int(input(f"Введите {arrCoord[i]}: ")))
distance = round((math.sqrt((arr[2] - arr[0])**2 + (arr[3] - arr[1])**2)), 2)
print(f" A ({arr[0]},{arr[1]}); B ({arr[2]},{arr[3]}) -> {distance}")

