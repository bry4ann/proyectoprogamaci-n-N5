#Proyecto número 5 del ramo Fundamentos de Programación.
#Por Bryan Nilo y Javiera Barraza.
#Ingeniería Civil Informática UV 1°año sección 2.

import matplotlib.pyplot as plt
print("\n\n-Bienvenido al programa donde podrá visualizar la información dada por el Ministerio de Salud sobre el avance de la Tasa de Incidencia del COVID-19 en las últimas 7 fechas desde el día 14/06/2021 hasta 05/07/2021.\n\nMENÚ:")
print("---------------------------------------------------------------------------------------------------------------\n1)Ingrese '1' para visualizar las regiones con su respectivo código.\n2)Escriba '2' para ingresar un código de región y desplegar las comunas de la región respectivamente.\n3)Escriba '3' para ingresar una comuna y desplegar el gráfico de la Tasa de Incidencia de las últimas 7 fechas.\n4)Escriba '4' para ingresar una región y desplegar el gráfico de la Tasa de Incidencia de las últimas 7 fechas.\n5)Escriba '5' para seleccionar el grafico de la región con mayor y menor densidad de Tasa de Incidencia, respectivamente.\n6)Escriba '6' para ver el gráfico de la métrica de comparación de la Tasa de Incidencia entre regiones.\n7)Escriba '7' para salir del menú.\n---------------------------------------------------------------------------------------------------------------")
opc=input("INGRESO: ")
opc=int(opc)

