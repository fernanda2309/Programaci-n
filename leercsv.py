# programa para leer csv
import csv
#cuando se escriba archivo_csv se trabaja con el contenido del archivo 
AnalisisCOVID19.csv
with open('AnalisisCOVID19.csv') as archivo_csv:
#archivo csv es el puente entre el programa y archivo

lector_csv = csv.reader (archivo_csv, delimiter='\')
#contador de lineas
contador_lineas = 0
for linea_datos in lector_csv:
if contador_lineas == 0:
print (f'Los nombres de columnas son {",".join(linea_datos)}')
else:
#mostrar dato por dato
print (f'\tFecha:{linea_datos[0]}.')
print (f'\tNuevos Contagios: {linea_datos[1]}.')
print (f'\tNuevos Fallecimientos: {linea_datos[2]}.')
print (f'\tPaís: {linea_datos[3]}.')
print(f'\t----------------')
#se incrementa el numero de lineas sin importar las condiciones
contador_lineas += 1
print (f'Procesadas {contador_lineas}lineas.')