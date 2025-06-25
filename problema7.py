#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta

n1 = int(input ("Ingrese Primer Nro.: "))
n2 = int(input ("Ingrese Segundo Nro.: "))

print ("\n Seleccione una opcion del Menu: ")
print ("1. Mostrar una suma de los dos numeros")
print ("2. Mostrar una resta de los dos numeros")
print ("3. Mostrar una multiplicacion de los dos numeros")

opcion = int(input ("\n Seleccione una opcion entre (1-3): "))

if opcion == 1:
    suma = n1 + n2
    print (f"\n La suma entre {n1} y {n2} es: {suma}")
elif opcion == 2:
    resta = n1-n2
    print (f"\n La resta entre {n1} y {n2} es: {resta}")
elif opcion == 3:
    multiplica = n1 * n2
    print (f"\n La multiplicacion entre {n1} y {n2} es: {multiplica}")
else:
    print (f"\n opcion invalida")
