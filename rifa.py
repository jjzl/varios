#! /usr/bin/env python

"""
Rifa.py

Programa simple para seleccionar el ganador de una lista 
en un archivo en formato csv de la forma "id,nombre,escuela"

"""
__author__= "Jose Zapata"
__author_email__="jjzapata@gmail"
__copyright__=""
__license__=""

import random, csv

filename = 'participantes.csv'

def result(iteration):
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		first = 1
		last = 0 
		numbers = []
		names = []
		schools = []
		for row in csv_reader:
			number = row[0]
			name = row[1]
			school = row[2]
			numbers.append(number)
			names.append(name)
			schools.append(school)
			last+=1

		winner = random.randrange(first, last)
		print('El numero ganador de la iteración: {} es: {} y corresponde a: {} de la escuela: {}'
			.format(iteration+1, numbers[winner-1],names[winner-1],schools[winner-1]))

#Entry point for program
if __name__ == '__main__':
	iterations = int(input("¿Cuantas iteraciones desea realizar para obtener al ganador? "))
	for i in range(iterations):
		result(i)



    
    
