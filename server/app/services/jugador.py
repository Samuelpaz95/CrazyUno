
from utilities import *

jugadores = []

class Jugador:
	
	def __init__(self, nombre, bot):
		self.nombre = nombre
		self.bot = bot
		self.mano = []

	@staticmethod
	def iniciar_jugadores(jugadores_totales):
		# num_jugadores = int(input("¿Cuántos jugadores humanos serán? [0, " + str(jugadores_totales) + "] "))
		num_jugadores = Utilities.pregunta(("¿Cuántos jugadores humanos serán? [0, " + str(jugadores_totales) + "] "), 0, jugadores_totales, -1)
		for i in range(num_jugadores):
		    nombre = input("Nombre del Jugador " + str(1 + i) + ": ")
		    jugadores.append(Jugador(nombre, False))

		for i in range(jugadores_totales - num_jugadores):
		    bot = 'Bot_' + str(i)
		    jugadores.append(Jugador(bot, True))

		'''print('\n')

		for i in range(len(jugadores)):
		print(jugadores[i].nombre)'''

	def poner_mano(self, mano):
		self.mano = mano

	def tomar_carta(self, carta):
		self.mano.append(carta)

	def imprimir_mano(self, selection = True):
		for i, carta in enumerate(self.mano):
			carta.imprimir_carta(((i + 1) if selection else None))
