import re

import datetime

captura = ""
miscontactos=[]

from clasepia import contacto

def askandcheck(_patron,_pregunta="Dame un datos: "):
    global captura
    while True:
        _fxvalor = input (_pregunta)
        coincide =re.search(_patron,_fxvalor)
        if (coincide):
            captura=_fxvalor
            break
        else:
            print ("El dato no es correcto. Intenta de nuevo.")
def strtodate (_dtconv):
    return
datetime.datetime(int(_dtocov[0:4]),int(_dtoconv[5:7]),int(_dtoconv[-2:]))

def IngresoDatos():
    askandcheck("^([A-Z ]){1,15}$","Nick en mayusculas: ")
nick =captura
askandcheck("^([A-Z ]){1,20}$", "Nombre en mayusculas: ")
nombre = captura
askandcheck('\w+@\w+', "inserta tu correo: ")
correo = captura
askandcheck('^(\d{2} \d{4}-\d{4})', "numero (99 9999-9999): ")
numero = captura
askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01]$", "Dame una fecha (YYYY-MM_DD): ")
fecha =captura
askandcheck ("^([0-9]){1,7}$", "ingresa tus gastos: ")

gastos = captura

miscontactos.append(contacto(nick, nombre, correo, numero, fecha, gastos))
