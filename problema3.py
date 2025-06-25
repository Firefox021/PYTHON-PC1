#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado.

nro_payasos = float (input ("Ingrese el N° de Payasos: "))
nro_munecas = float (input ("Ingrese el N° de Muñecas: "))

peso_payasos = (nro_payasos * 112)
peso_munecas = (nro_munecas * 75)
peso_total = (peso_payasos + peso_munecas)

print (f"Peso Total paquete en Gr. es : {peso_total:.2f}")

