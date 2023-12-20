import csv
import sys

def cargarFila(row, reglas):
    #variables serparadas
    estado_actual= row[0]
    char_string=row[1]
    char_escribir=row[2]
    movimiento=row[3]
    estado_nuevo=row[4]
    reglas.append(Regla(estado_actual, char_string , char_escribir , movimiento ,estado_nuevo))

def printReglas(reglas):
    for regla in reglas:
        regla.toString()

def cargarArchivo(archivo, reglas): 
    try:
        with open(archivo, 'r') as csvfile:
            csv_file_reader = csv.reader(csvfile, delimiter=';')        
            next(csv_file_reader) 
            for row in csv_file_reader:
                cargarFila(row, reglas) #lo puse asi en caso de tener mas de una linea de estados, si lo necesitan cambienlo
            print("Archivo cargado con éxito!")
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no se encontro.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    #recibe el archivo csv

class Regla: 
    #constructor
    def __init__(self, estado_actual, char_string , char_escribir , movimiento ,estado_nuevo):
        self.estado_actual = estado_actual
        self.char_string = char_string
        self.char_escribir = char_escribir
        self.movimiento = movimiento
        self.estado_nuevo = estado_nuevo

    def toString(self):
        texto = self.estado_actual + ", " + self.char_string + ", " + self.char_escribir + ", " + self.movimiento + ", " + self.estado_nuevo
        print(texto)

def procesarPalabra(palabra, reglas):
    seguir = True
    head = 3
    word = "###" + palabra + "###"
    estado_actual = "q0"
    estadoHalt = False
    while seguir: 
        seguir = False
        char_actual = word[head]
        print(f"Cabezal: {head}, Estado actual: {estado_actual},  Palabra: {word}")
        for regla in reglas:
            if estado_actual == regla.estado_actual:
                if char_actual == regla.char_string:
                    word = word[:head] + regla.char_escribir + word[head+1:]
                    if regla.movimiento.lower() == "r":
                        head += 1
                    elif regla.movimiento.lower() == "l":
                        head -= 1
                    elif regla.movimiento.lower() == "h":
                        estadoHalt = True
                        break
                    estado_actual = regla.estado_nuevo
                    seguir = True
                    break
        if not seguir:
            if estadoHalt: 
                print("La palabra no pertenece al Lenguaje.")
            else:
                print("La palaba pertenece al Lenguaje")

def main():
    archivo = input("Ingrese el nombre del archivo: ")
    reglas = []
    cargarArchivo(archivo, reglas)
    #printReglas(reglas)
    seguir = 1
    while seguir:
        palabra = input("\nIngrese la palabra a validar: ")
        procesarPalabra(palabra, reglas)

        seguirInput = input("Seguir validando palabras (s/n): ")
        if seguirInput == 'S' or seguirInput == 's':
            seguir = 1
        else:
            seguir = 0

if __name__ == "__main__":
    main()