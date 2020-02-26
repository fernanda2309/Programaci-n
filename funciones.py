# El codigo de la funcion es obligatorio. Si no hay codigo por el momento, usar pass
def pendiente():
 pass

# Si una variable se declara fuera de procedimiento se dice que es global 
variableglobal="Soy global"

def norecibeargumentos():
  variableglobal=4
  print ("no recibe argumentos")
  print(variableglobal)

# Si se comenta la siguiente linea, usar la variable equivale a declarar una version local de la variable; si no se comenta, usar la variable implica usar la global
def recibeargumentos(fname, lname):
    print(fname + " " + lname)
    print("variableglobal")

# Un argumento es opcional cuando le asignas un valor  al momento de su declaracion.
def argumentosopcionales(city, country = "USA"):
  print("I am from " + city + ", " + country)

# Si se especifica return, la funcion retorna valores 
def elevoalcuadrado(x):
  return x * x

def main():
 print(elevoalcuadrado(4))