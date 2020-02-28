# Pregunta diferentes tipos de datos, sin validación.

import datetime

#   str   string
#   i     int
#   f     float
#   dt    date

def main():
 strDato = input("Dame un dato string: ")
 # Los datos numéricos se especifica su notación
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # Los datos date se especifica su notación
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 
 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))