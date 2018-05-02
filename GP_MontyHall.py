import numpy as np
import matplotlib.pyplot as plt
from numpy import random

#Crea las 3 puertas con los premios en orden aleatorio
def sort_doors():
	lista = ['goat', 'goat', 'car']
	random.shuffle(lista)
	return lista

#Simula una eleccion aleatoria entre las 3 puertas
def choose_door():
	choice = [0,1,2]
	return random.choice(choice)

#Se revela una puerta con cabra, que no es la elegida por choose_door
def reveal_door(lista, choice):

	for i in range(0,len(lista)):
  		elemento = lista[i]
		if((choice != i) and (elemento == 'goat')):
			lista[i] = 'GOAT_MONTY'
			break

	return lista

#Pregunta si se quiere cambiar de puerta despues de saber donde habia una
#cabra, y termina el juego revelando la puerta escogida
def finish_game(lista,choice,change):

	if(change == False):
		return lista[choice]
	else:
		
		for j in range(0,len(lista)):
			if((lista[j] != 'GOAT_MONTY') and (j != choice)):
				return lista[j]

#Corre UN juego completo
def un_juego(change):
 
	inicial = sort_doors()
	choice = choose_door()
	nueva = reveal_door(inicial,choice)
	revelacion = finish_game(nueva,choice,change)
	return revelacion


#probabilidades empiezan en 0//contadores
prob_True = 0.0
prob_False= 0.0

#Corre 100 juegos para cada eleccion
for i in range(0,100):
   
	choice_true = un_juego(True)
	choice_false= un_juego(False)
	
	if(choice_true == 'car'):
		prob_True += 1

	if(choice_false == 'car'):
		prob_False += 1

print 'La probabilidad de obtener el carro si no se cambia la eleccion de puerta es: '
print prob_False

print 'Y la probabilidad de obtener el carro si se hace el cambio de puerta: '
print prob_True

	
	

	
			







