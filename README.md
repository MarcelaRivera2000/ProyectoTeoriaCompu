## Validación de Palabras con máquina de Turing implementada en Python

### Uso del Programa
1. Ejecuta el programa `main.py`.
2. Ingresa el nombre del archivo: `igual01.csv`.
   - Se cargará el archivo con éxito.
   
3. Ingresa la palabra a validar: `01`.
   - El programa mostrará la validación detallada paso a paso:
   
   ```plaintext
   Cabezal: 3, Estado actual: q0,  Palabra: ###01###
   Cabezal: 4, Estado actual: q1,  Palabra: ###X1###
   Cabezal: 3, Estado actual: q2,  Palabra: ###XX###
   Cabezal: 2, Estado actual: q2,  Palabra: ###XX###
   Cabezal: 3, Estado actual: q0,  Palabra: ###XX###
   Cabezal: 4, Estado actual: q0,  Palabra: ###XX###
   Cabezal: 5, Estado actual: q0,  Palabra: ###XX###
   Cabezal: 4, Estado actual: q4,  Palabra: ###XX###
   Cabezal: 3, Estado actual: q4,  Palabra: ###XX###
   Cabezal: 2, Estado actual: q4,  Palabra: ###XX###
   Cabezal: 3, Estado actual: q6,  Palabra: ###XX###
   La palabra pertenece al Lenguaje

## Formato Válido para el CSV

El formato válido para el archivo CSV debería seguir la estructura:
Donde:
- `Estado actual`: El estado actual del programa.
- `char en string`: El carácter que lee.
- `char a escribir`: El carácter a escribir en la posición actual.
- `movimiento`: La acción/movimiento a realizar.
- `estado nuevo`: El nuevo estado después del movimiento.

Este formato proporciona la estructura necesaria para representar los estados, caracteres y movimientos dentro de un archivo CSV para su uso con el programa correspondiente.

### Notas adicionales
   Se incluyeron dos ejemplos.
   1. El archivo abcd.csv es un lenguaje de la forma a^n b^n c^n d^n, donde n>0.
   2. El archivo igual01.csv es un lenguaje para las palabras que contienen misma cantidad de 0s y 1s.


