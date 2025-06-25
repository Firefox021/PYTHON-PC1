#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']

lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

lista_muestra.pop(5)
lista_muestra.pop(4)
lista_muestra.pop(0)
print (lista_muestra)