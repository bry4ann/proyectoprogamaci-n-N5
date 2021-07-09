import matplotlib.pyplot as plt


print("ingrese la funcion que desea utilizar:")
print("1) mostrar comuna filtrada por región")
print("2) ingresar comuna por código o nombre y desplegar gráfica de la tasa de incidencia  de las ultimas 7 fechas")
print("3) ingresar una region por código o nombre y desplegar una grafica  de la tasa de incidencia de los últimos 7 fechas")
print("4) desplegar un grafico a elección con la región con mayor y menor densidad de tasa de insidencia respectivamente")
print("5) metrica de comparación")

opc=input("-")
while(not opc.isnumeric()):
 opc=input("-")
opc=int(opc)  
if opc==1 :
 codigo=int(input("seleccione número de región:"))

