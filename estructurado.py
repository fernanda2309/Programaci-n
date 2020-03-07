import re
import datetime

def askandcheck(_ask,_type="int",_check="^([+-]?[1-9]\d*|0)$"):
  _captura=""
    # Procesamiento para int
  if _type=="int":
    while True:
      _captura=input(_ask)
      if re.search(_check,_captura):
        return int(_captura)
        break
  else:
    print("El dato no tiene el tipo correcto")

if _type=="float":
  _check="^[-+]?\d*\.?\d*$"
  while True:
    _captura=input(_ask)
    if re.search(_check,_captura):
      return float(_captura)
       break
else:
  print("El dato no tiene el tipo correcto")

# email
if _type=="email":
  _check="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  while True:
    _captura=input(_ask)
  if re.search(_check,_captura):
    return _captura
    break
else:
  print("El dato no tiene formato de correo")

def main():
  personal=askandcheck("Dame tu RFC:","custom","^[A-Z]{3,4}-[0-9]{6}-[A-Z0-9]{3}")
  print(personal)
  print(type(personal))

correo=askandcheck("Dame tu correo:","email")
print(correo)
print(type(correo))

edad=askandcheck("Dame tu edad:")
print(edad)
print(type(edad))

dinero=askandcheck("Cuánto dinero tienes:","float")
print(dinero)
print(type(dinero))

fechanacimiento=askandcheck("Qué fecha naciste:","date")
print(fechanacimiento)
print(type(fechanacimiento))