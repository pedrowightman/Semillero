import numpy as np
import csv
import random

def matlock(mat, puntos):
    puntos_matlock = [np.linalg.matmul(punto, mat).tolist() for punto in puntos]
    return puntos_matlock

def matlock_inv(mat, puntos):
    mat2 = np.linalg.inv(mat)
    puntos_matlock = [np.linalg.matmul(punto, mat2).tolist() for punto in puntos]
    return puntos_matlock



def addRuido(punto, maxRuido, metros: bool = False):
    if metros:
        maxRuido = maxRuido*360/4070000
    puntor = punto.copy()
    puntor[0] += random.uniform(-maxRuido, maxRuido)
    puntor[1] += random.uniform(-maxRuido, maxRuido)
    return puntor

def generate2Points(punto, max):
    
    return punto2



#DATOS

m = [[1, 2, 3], [4, 5, -6], [-7, 2, 9]]

datos = []
with open('datos.csv', newline='') as csvfile:
    reader = csv.reader(csvfile )
    for row in reader:
        datos.append([float(i) for i in row])

puntos = matlock(m, datos)

print(puntos)

puntos2 = matlock_inv(m, puntos)

print(puntos2)