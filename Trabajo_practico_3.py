
a = input("cual es tu nombre?")
print("hola", a)

b = int(input("Hasta que numero quieres que cuente?"))

contador = 0

while contador <= b:
  print(contador)
  contador +=1




def menu():
  seleccion = 0
  while seleccion != 5:
    print("seleccione una opcion: \n 1:sumar \n 2: restar \n 3: multiplicar \n 4: dividir \n 5: salir")
    seleccion = int(input("digite su opcion: "))

    if (seleccion == 1):
      suma()
    elif(seleccion == 2):
      resta()
    elif (seleccion == 3):
      multiplicacion()
    elif(seleccion == 4):
      division()
    else:
      print("gracias por usar la sumadora LEAD!")


def suma():
  num1= int(input ("ingresa el primer numero: "))
  num2= int(input ("ingresa el segundo numero: "))
  print(num1+num2)

def resta():
  num1= int(input ("ingresa el primer numero: "))
  num2= int(input ("ingresa el segundo numero: "))
  print(num1-num2)

def multiplicacion():
  num1= int(input ("ingresa el primer numero: "))
  num2= int(input ("ingresa el segundo numero: "))
  print(num1*num2)

def division():
  num1= int(input ("ingresa el primer numero: "))
  num2= int(input ("ingresa el segundo numero: "))
  print(num1/num2)

menu()