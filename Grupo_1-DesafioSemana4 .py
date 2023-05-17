'''
Desafío 4: La inmobiliaria
Requisitos técnicos:
- Operadores.
- Estructuras de datos.
- Estructuras de control de flujo.
- Funciones
Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
Se te pide construir un programa que permita:
 Agregar, editar y eliminar inmuebles a la lista.
Las funciones deben ajustarse al formato de lista y reglas de validación.
 Cambiar el estado de un inmueble, sin modificar sus demás datos.
Las funciones deben ajustarse al formato de lista y reglas de validación.
 Hacer búsqueda de inmuebles en función de un presupuesto dado.
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
reglas de precio en función de la zona.
Formato de lista
[{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
Reglas de validación
 Inmuebles solo de zona: A, B o C.
 Inmuebles con estado: Disponible, Reservado o Vendido.
 No opera con inmuebles:
 Anteriores al año 2000.
 Menores de 60 metros cuadrados.
 Menores de 2 habitaciones.
Reglas de precio
 Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
 Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
 Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2
'''
#Mensaje de bienvenida
print("\n\n------------------------------INFORMATORIO 2023----------------------------------------")
print("---------------------------------------------------------------------------------------")
print("-----------------------Desafío 4: La inmobiliaria--------------------------------- \n")
print("GRUPO 1- INTEGRANTES: Mercado Alejandro, Quiroz Agustín, Pedro Galarza, Maciel Enzo\n")
print("Máximo Saleh, Marighetti José Juan, Carrazco Enzo, Brunelli Oscar Ariel, Fernández Braian\n")
print("Echaide Silvina, Luxen Lucas Sebastian, Mendoza Luciano Leonel, Luna Maximiliano\n")
print("--------------------------------------------------------------------------------------\n")

#lista de muestra, se puede probar con otra lista supongo

inmobiliaria = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

'''
Crear tres funciones, una para el punto uno, otra para el dos, y una ultima para el tres. Necesitariamos una funcion principal que ordene las otras tres y solicite
al usuario que quiere hacer.
'''

#declaracion de la funcion principal que llama a las demas

def inmobiliariaApp():
    seguir = 1
    while(seguir != 2):
        accion = int(input("\nIngrese la accion que desea realizar, siendo: \n1- Agregar, editar y eliminar inmuebles \n2- Cambiar el estado de un inmueble \n3- Hacer búsqueda de inmuebles en función de un presupuesto. \n"))
        if(accion == 1):
            editarInmuebles()
        elif(accion ==2):
            cambiarEstadoInmueble()
        elif(accion == 3):
            numero = int(input("ingresa un monto: \n$"))
            busquedaInmueble(numero)
        else:
            print("No ingresaste una opcion valida, ingrese una opcion valida, para salir ingrese 9: \n")
        seguir = int(input("\n¿Quiere realizar otra operación? 1 - SI, 2 - NO: \n"))
    print("Gracias por usar nuestra app. Hasta pronto...")

#funcion para calcular el precio de las propiedades

def calculoPrecio(n1):
    return(inmobiliaria[n1]['metros'] * 100) + (inmobiliaria[n1]['habitaciones'] * 500) + (inmobiliaria[n1]['garaje'] * 1500) * (1 - (2023 - inmobiliaria[n1]['año']) / 100)

#funcion para buscar inmuebles por valor(punto 3)

def busquedaInmueble(n1):
    i = 0
    print("La lista de propiedades en el rango de valor ingresado es: \n")
    for e in inmobiliaria:
        if(calculoPrecio(i) <= n1):
            inmobiliaria[i]['precio'] = calculoPrecio(i)
            print(inmobiliaria[i])
        i = i + 1

#llamado a la funcion principal

inmobiliariaApp()