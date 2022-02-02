#Ejemplo 5
from datetime import datetime

def ValidarFecha(d,m,a):
  try:
    datetime.strptime(d,'%d')
    datetime.strptime(m,'%m')
    datetime.strptime(a,'%Y')
    return True

  except ValueError:
    return False

while True:
  print("1. Validar fecha")
  print("2. Salir")

  opcion = int(input()) 
  if opcion == 1:
    dia = str(input("Día:"))
    mes = str(input("Mes:"))
    aa = str(input("Año:"))
    print("¿Fecha válida?", ValidarFecha(dia, mes, aa))

  elif opcion == 2:
    break
  else:
    print("Opción incorrecta")
