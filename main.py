import csv
import sys

def prueba(row):
    #variables serparadas
    estado_actual= row[0]
    char_string=row[1]
    char_escribir=row[2]
    movimiento=row[3]
    estado_nuevo=row[4]
    print(estado_actual, char_string , char_escribir , movimiento ,estado_nuevo)


#recibe el archivo csv
archivo = sys.argv[1]

try:
    with open(archivo, 'r') as csvfile:
        csv_file_reader = csv.reader(csvfile, delimiter=';')        
        next(csv_file_reader) 
        for row in csv_file_reader:
            prueba(row) #lo puse asi en caso de tener mas de una linea de estados, si lo necesitan cambienlo

except FileNotFoundError:
    print(f"Error: El archivo {archivo} no se encontro.")
except Exception as e:
    print(f"Error inesperado: {e}")


