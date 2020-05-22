# estructura de archivo texto plano
#modulo para usar el sistema
import os

# modulo para usar archivos csv
import csv

#se declara la clase contacto
# <contacto> sirve para pobalr una lista.


class contacto():
    def _init_(self, usuario, nombre, correo):
        self.usuario = usuario
        self.nombre = nombre
        self.correo = correo


#lsita para usar los contactos
contactos = []

# se cargan dos valores
contactos.append(contacto('master', 'Ramon Tamez', 'ramon.tamez@hotmail.com'))
contactos.append(contacto('student', 'Emily Cantu', 'emily.cantu@hotmail.com'))

#se va a guardar en la variable <ruta>
# la ruta absoluta del directorio de trabajo
ruta = os.path.abspath(os.getcwd())
archivo_trabajo = ruta + "\\contactos.csv"
archivo_respaldo = ruta + "\\contactos.bak"

#preguntar si el archivo existe
if os.path.exists(archivo_trabajo):
    # si el archivo exist, entonces verifica si hay respaldo y lo borra
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)

# establecemos el archivo de datos, como respaldo
os.rename(archivo_trabajo, archivo_respaldo)

# generamos archivo csv
f = open(archivo_trabajo, "w+")

# estructura de encabezados del archivo csv
f.write("usuatio | nombre | correo\n")
for elemento in contactos:
    f.write(f'{elemento.usuario}|{elemento.nombre}|{elemento.correo}\n')

# se cierra archivo csv
f.close()
