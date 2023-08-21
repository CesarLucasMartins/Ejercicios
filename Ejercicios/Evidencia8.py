
#Ejercicios Estructuras Condicionales:

#Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea
#correspondiente:

#1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha
#ganado el sorteo!

#2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco,
#seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

"""numero = int(input ("ingrese un numero "))

if numero == 10:
    print("¡Usted ha ganado el sorteo!")


elif numero < 10:
    print ("¡Falto un poco,seguí participando!")

else:
    print ("¡Te pasaste, a seguir intentando!")"""
    




#3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
#mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
#ingresado no es ninguno de esos, imprimir otro mensaje.

"""dia = input("ingrese un dia de la semana ").lower()

if dia == "lunes":
    print("Arranca la semana!")

elif dia== "viernes":
    print("Es viernes y tu cuerpo lo sabe!")

elif dia == "sabado" or dia == "domingo":
    print("A disfrutar el finde!")

else:
    print("vamos!,un dia a la vez!")"""



#4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
#“es vocal”.

"""letra = input("ingrese una letra ").lower()

if letra in {"a", "e", "i", "o", "u"}:
    print("la letra es una vocal")

else:
    print("la letra es una consonante")"""





#Ejercicios Estructuras Repetitivas:
#Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea
#correspondiente:

#1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
#hasta que se ingrese -1.

"""suma = 0 

while True:
    numero = float(input ("ingrese un numero o -1 para finalizar "))

    if numero == -1:
        print("sistema finalizado")
        break
    suma += numero

print("la sumatoria total es" , suma) """


#2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
#introducir). El programa debe informar de cuantos números introducidos son mayores que
#0, menores que 0 e iguales a 0.

"""cantidad = int(input("introduzca la cantidad de numeros que va a ingresar "))

mayor_a_cero = 0
menor_a_cero = 0
igual_a_cero = 0

for i in range (cantidad):
    numeros_introducidos = float (input ("introduzca los numeros separados con enter "))

    mayor_a_cero += numeros_introducidos > 0
    menor_a_cero += numeros_introducidos < 0
    igual_a_cero += numeros_introducidos == 0

print(f"cantidad de numeros mayores a cero {mayor_a_cero}, cantidad de numeros menores a cero {menor_a_cero}, cantidad de numeros iguales a cero  {igual_a_cero}") """


#3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
#contrario, el programa termina cuando se introduce un cero.
while True:
    letra = input("ingrese una letra o 0 para finalizar el programa ").lower()
    if letra == "0":
        print("ha finalizado el programa ")
        break

    if letra in {"a", "e", "i", "o", "u"}:
        print("la letra es una vocal")

    else:
        print ("la letra no es una vocal ")

    

   




#4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
#media de todos los números introducidos.