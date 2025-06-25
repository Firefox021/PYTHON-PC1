#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
#puede ser calculada de la siguiente forma:

N = int (input("Ingrese Numero Entero: "))
if N <=0:
 print ("error: numero debe ser entero")
else:
 suma= N * (N + 1) //2
 print (f"suma de todos los numeros de 1 hasta {N} es: {suma}")
