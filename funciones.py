# Si no hay codigo por el momento, usar pass
def pendiente():
 pass

# Si una variable se define fuera  es global 
variableglobal="Soy global"

def norecibeargumentos():
  variableglobal=4
  print ("no recibe argumentos")
  print(variableglobal)

# Si se escribe la siguiente linea, usarla implica usar la global
def recibeargumentos(fname, lname):
    print(fname + " " + lname)
    print("variableglobal")

 
def argumentosopcionales(city, country = "USA"):
  print("I am from " + city + ", " + country)

# la funcion retorna valores 
def elevoalcuadrado(x):
  return x * x

def main():
 print(elevoalcuadrado(4))