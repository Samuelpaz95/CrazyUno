
import random

class Carta:
	
	def __init__(self, valor, palo):
		self.valor = valor
		self.palo = palo
		self.etiqueta = str(valor + ' ' + palo)

	@staticmethod
	def cargar_cartas():
		baraja = []
		''' 	
		'''
		palos = ['rojo', 'azul', 'amarillo', 'verde']
		valores = ['2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverso', '+2']
		for p in palos:
			for v in valores:
				baraja.append(Carta(v, p)) # v + " " + p, 
			
		especiales = ['+4', 'Ginyu', 'Joker']
		for e in especiales:
			baraja.append(Carta(e, 'negro')) # e + " " + 'negro',

		return baraja

	@staticmethod
	def mezcla(baraja):
		random.shuffle(baraja)
		return baraja

	def imprimir_carta(self, numeracion = None):
		print((str(numeracion) + '. ' if numeracion != None else '') + self.etiqueta)
