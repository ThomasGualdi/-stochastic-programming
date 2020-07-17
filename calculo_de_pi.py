import random
import math
from estadistica import media, varianza, desvio
import time
def aventar_agujas(numero_de_agujas):
    dentro_del_circulo = 0 
    fuera_del_circulo = 0 
    for _ in range(numero_de_agujas):
        # la funcion random escoge un valor entre 0 y 1
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distancia_al_centro = math.sqrt(x**2 + y**2)
        if distancia_al_centro < 1: 
            dentro_del_circulo +=1 
        else:
            fuera_del_circulo += 1
    area_estimada_circulo = dentro_del_circulo
    area_estimada_cuadrado = dentro_del_circulo + fuera_del_circulo
    pi = 4 * (area_estimada_circulo/area_estimada_cuadrado)
    return pi
def estimador (numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimado = aventar_agujas(numero_de_agujas)
        estimados.append(estimado)
    return estimados
    #mu = media(estimados)
    #desvio_estimados = desvio(estimados)
   # return mu, desvio_estimados
if __name__=='__main__':
    numero_de_intentos = int(input('intentos: '))
    numero_de_agujas = int(input('numero de agujas: '))
    inicio = time.time()
    pi = aventar_agujas(numero_de_agujas)
    estadistica_de_pi = estimador(numero_de_agujas, numero_de_intentos)
    print(pi)
    print(estadistica_de_pi)
    final = time.time()
    tiempo = final - inicio 
    print(tiempo)