import re

def main():
  # para hasta que se presenta un break, estara preguntando mientras no se cumpla.
  while True:
    strRFC = input("Dame el RFC: ")
    coincide = re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)
    if (coincide):
      print("RFC Correcto!")
      break
    else:
      print("RFC incorrecto. Intenta de nuevo.")