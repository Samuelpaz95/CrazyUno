
from carta import *

class Mesa():

	def __init__(self):
		self.mazo = Carta.cargar_cartas()
		self.cartas_mesa = None

	def mezclar(self):
		self.mazo = Carta.mezcla(self.mazo)

	def mostrar(self):
		return self.mazo[0].etiqueta

	def mostrar_todo(self):
		for i in range(len(self.mazo)):
			print(self.mazo[i].etiqueta)

	def servir_mesa(self, carta):
		self.cartas_mesa = carta
		return self.cartas_mesa.etiqueta

	def imprimir_mesa(self):
		print(self.cartas_mesa[0].etiqueta)
