# All your code goes here!!!
print("SKILLS FOR WOMEN IN TECH")
students = []

def registro(n,e,t,m):
  student = {}
  student['Nombre'] = n
  student['Edad'] = e
  student['Temas'] = t
  student['Estado'] = m
  return student


while True:
  print("1. Añadir estudiante")
  print("2. Directorio")
  print("3. Salir")

  opcion = int(input()) 
  if opcion == 1:
    nom =input('Nombre:  ')
    ed =int(input('Edad:  '))
    tem =input('Temas:  ')
    if ed < 18:
      me='Menor de edad'
    else:
      me='Mayor de edad'
    student = registro(nom,ed,tem,me)
    students.append(student)
  elif opcion == 2:
    for student in students:
      for key in student:
        print(f'{key}: {student[key]}')    
  elif opcion == 3:
    break
  else:
    print("Vuelve a intentarlo")
