
# validación de expresiones regulares
import re
# de tipo datetime
import datetime

# variable de paso(que permite preguntar y validar)
captura=""

# si el dato es correcto lo captura y si no sigue preguntando
def askandcheck(_patron,_pregunta="Dame un dato: "):
  global captura
  while True:
    _fxvalor = input(_pregunta)
    coincide = re.search(_patron, _fxvalor)
    if (coincide):
      captura= _fxvalor
      break
    else:
      print("El dato no es correcto. Intenta de nuevo.")

#  YYYY-MM-DD a datetime
def strtodate(_dtoconv):
    return datetime.datetime(int(_dtoconv[0:4]), int(_dtoconv[5:7]), int(_dtoconv[-2:]))


def main():
  # sólo acepta 4 digitos
  askandcheck("^[0-9]{4}$", "ID (4 dígitos): ")
  numeroID=captura
  # palabra, de 1 a 20 letras mayúsculas, o espacio.
  askandcheck("^([A-Z ]){1,20}$", "Nombre: ")
  nombre=captura
  # Si o No
  askandcheck("^[S|N]$", "Acepta (S/N): ")
  acepta=captura
  # date
  askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$", "Dame una fecha (YYYY-MM-DD): ")
  fecha=captura

  print(numeroID)
  print(nombre)
  print(acepta)
  print(fecha)