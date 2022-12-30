
class Utilities:

    @staticmethod
    def opciones(texto, opciones):
        valor = "".upper()
        while not valor in opciones:
            valor = input(texto + '(Por favor, seleccione una de las opciones dadas). ').upper()
        return valor
    
    @staticmethod
    def pregunta(texto, min, max, key):
        valor = key
        while (valor < min) or (valor > max):
            valor = int(input(texto + '(Por favor, seleccione una de las opciones dadas). '))
        return valor
