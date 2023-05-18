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
print("--------------------------Desafío 4: La inmobiliaria----------------------------------- \n")
print("GRUPO 1- INTEGRANTES: Mercado Alejandro, Quiroz Agustín, Pedro Galarza, Maciel Enzo\n")
print("Máximo Saleh, Marighetti José Juan, Carrazco Enzo, Brunelli Oscar Ariel, Fernández Braian\n")
print("Echaide Silvina, Luxen Lucas Sebastian, Mendoza Luciano Leonel, Luna Maximiliano\n")
print("--------------------------------------------------------------------------------------\n")

#lista de muestra, se puede probar con otra lista que tenga el mismo formato, o bien, partir de una lista vacia

listaInmobiliaria = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


#declaracion de la funcion principal que llama a las demas

def inmobiliariaApp(dic):
    seguir = 1
    while(seguir != 2):
        accion = int(input("\nIngrese la accion que desea realizar, siendo: \n1- Agregar, editar y eliminar inmuebles. \n2- Cambiar el estado de un inmueble. \n3- Hacer búsqueda de inmuebles en función de un presupuesto. \n4- Mostrar lista de inmuebles.\n"))
        if(accion == 1):
            editarInmuebles(dic)
        elif(accion ==2):
            cambiarEstadoInmueble(dic)
        elif(accion == 3):
            numero = int(input("ingresa un monto: \n$"))
            busquedaInmueble(dic, numero)
        elif(accion == 4):
            mostrarListaInmuebles(dic)
        else:
            print("No ingresaste una opcion valida, ingrese una opcion valida, para salir ingrese 9: \n")
        seguir = int(input("\n¿Quiere realizar otra operación? 1 - SI, 2 - NO: \n"))
    print("---------------------------------------------------------------------------------------")
    print("------------------Gracias por usar nuestra app. Hasta pronto...------------------------")
    print("---------------------------------------------------------------------------------------")

#funcion para validar si un nuevo inmueble cumple con las condiciones(La validacion al editar un inmueble se hace localmente, al igual que en el cambio de estado)

def validacionOperaInmueble(dic):
    return((dic['año'] >= 2000) & (dic['metros'] >= 60) & (dic['habitaciones'] >= 2))

#funcion para crear, editar y eliminar propiedades de inmuebles    

def agregarInmueble(dic):
    nuevoInmueble = {}
    anio = int(input("Ingrese el año del inmueble: "))
    metros = int(input("Ingrese metros cuadrados: "))
    habitaciones = int(input("Ingrese habitaciones: "))
    garaje = int(input("Tiene garaje? 1 - Si, 2 - No\n"))
    if(garaje == 1):
        garaje = True
    elif(garaje == 2):
        garaje = False
    zonaq = 0
    while((zonaq != 1) or (zonaq != 2) or (zonaq != 3)):
        zonaq = int(input("Ingrese zona. 1 - A, 2 - B, 3 - C: "))
        if(zonaq == 1):
            zona = 'A'
            break
        elif(zonaq == 2):
            zona = 'B'
            break
        elif(zonaq == 3):
            zona = 'C'
            break
        else:
            print("Ingresaste un valor no valido")
    estadoq = 0
    while((estadoq != 1) or (estadoq != 2) or (estadoq != 3)):
        estadoq = int(input("Determine el estado del inmueble. 1 - Disponible, 2 - Reservado, 3 - Vendido: \n"))
        if(estadoq == 1):
            estado = 'Disponible'
            break
        elif(estadoq == 2):
            estado = 'Reservado'
            break
        elif(estadoq == 3):
            estado = 'vendido'
            break
        else:
            print("Ingresaste un valor no valido")
    nuevoInmueble['año'] = anio
    nuevoInmueble['metros'] = metros
    nuevoInmueble['habitaciones'] = habitaciones
    nuevoInmueble['garaje'] = garaje
    nuevoInmueble['zona'] = zona
    nuevoInmueble['estado'] = estado
    if(validacionOperaInmueble(nuevoInmueble) == True):
        print(nuevoInmueble)
        agregar = int(input("Desea agregar el inmueble a la lista? 1 - Si, 2 - No: \n"))
        if(agregar == 1):
            dic.append(nuevoInmueble)
        print("La lista de inmuebles actualizada es la siguiente: \n")
        x = 0    
        for e in dic:
            print(dic[x])
            x = x + 1
    else:
        print("Lo sentimos, no se opera con inmuebles: \n> Anteriores al año 2000.\n> Menores de 60 metros cuadrados.\n> Menores de 2 habitaciones.")

#funcion para editar elementos de un inmueble

def editInmueble(dic):
    i = 0
    print("Los inmuebles son los siguientes: ")
    for e in dic:
        print(f"{i + 1}) {dic[i]}")
        i = i + 1
    seleccion = int(input("Elija el numero de inmueble al que desea cambiar el estado: "))-1
    print(f"El inmueble seleccionado es la siguiente: \n {dic[seleccion]}")
    atributo = int(input("Elija el atributo del inmueble que desea editar: \n1 - Año\n2 - Metros \n3 - Habitaciones \n4 - Garaje \n5 - Zona \n"))
    if(atributo == 1):
        anioq = int(input("Ingrese el nuevo valor de 'año': \n"))
        if(anioq >= 2000):
            dic[seleccion]['año'] = anioq
        else: 
            print("Lo sentimos, no se opera con inmuebles: \n> Anteriores al año 2000.\n> Menores de 60 metros cuadrados.\n> Menores de 2 habitaciones.")
    elif(atributo == 2):
        metrosq = int(input("Ingrese el nuevo valor de 'metros': \n"))
        if(metrosq >= 60): 
            dic[seleccion]['metros'] = metrosq
        else: 
            print("Lo sentimos, no se opera con inmuebles: \n> Anteriores al año 2000.\n> Menores de 60 metros cuadrados.\n> Menores de 2 habitaciones.")
    elif(atributo == 3):
        habitacionesq = int(input("Ingrese el nuevo valor de 'habitaciones': \n"))
        if(habitacionesq >= 2):
            dic[seleccion]['habitaciones'] = habitacionesq
        else: 
            print("Lo sentimos, no se opera con inmuebles: \n> Anteriores al año 2000.\n> Menores de 60 metros cuadrados.\n> Menores de 2 habitaciones.")
    elif(atributo == 4):
        dic[seleccion]['garaje'] = int(input("Ingrese el nuevo valor de 'garaje': 1 - Si, 2 - No"))
        if(dic[seleccion]['garaje'] == 1):
            dic[seleccion]['garaje'] = True
        elif(dic[seleccion]['garaje'] == 2):
            dic[seleccion]['garaje'] = False
    elif(atributo == 5):
        zonaq = 0
        while((zonaq != 1) or (zonaq != 2) or (zonaq != 3)):
            zonaq = int(input("Ingrese zona. 1 - A, 2 - B, 3 - C: "))
            if(zonaq == 1):
                dic[seleccion]['zona'] = 'A'
                break
            elif(zonaq == 2):
                dic[seleccion]['zona'] = 'B'
                break
            elif(zonaq == 3):
                dic[seleccion]['zona'] = 'C'
                break
            else:
                print("Ingresaste un valor no valido")  
    print(f"\nEl estado del inmueble es el siguiente: \n {dic[seleccion]}")

#funcion para eliminar inmuebles

def eliminarInmueble(dic):
    j = 0
    print("Los inmuebles son los siguientes: ")
    for e in dic:
        print(f"{j + 1}) {dic[j]}")
        j = j + 1
    opcionEliminar = int(input("Elija el numero del inmueble que desea eliminar: "))-1
    print(f"El inmueble seleccionado es la siguiente: \n {dic[opcionEliminar]}")
    confirmarEliminar = int(input("Esta seguro de que quiere eliminar el inmueble?. 1 - Si, 2 - No: \n"))
    if(confirmarEliminar == 1):
        del dic[opcionEliminar]
        print("La lista de inmuebles actualizada es la siguiente: \n")
        x = 0    
        for e in dic:
            print(dic[x])
            x = x + 1
    elif(confirmarEliminar == 2):
        print("Eliminacion cancelada...")

#funcion general para agregar, editar y borrar inmuebles

def editarInmuebles(dic):
    opcion = int(input("\nIngrese la accion que desea realizar, siendo: \n1- Agregar inmueble \n2- Editar inmueble \n3- Eliminar inmueble"))
    if(opcion == 1):
        agregarInmueble(dic)
    elif(opcion == 2):
        editInmueble(dic)
    elif(opcion == 3):
        eliminarInmueble(dic)

#funcion para editar el estado de un inmueble(punto 2)

def cambiarEstadoInmueble(dic):
    i = 0
    print("Los inmuebles son los siguientes: ")
    for e in dic:
        print(f"{i + 1}) {dic[i]}")
        i = i + 1
    propiedadnumero = int(input("Elija el numero de inmueble al que desea cambiar el estado: "))
    print(f"El inmueble seleccionado es la siguiente: \n {dic[propiedadnumero-1]}")
    estadoq = 0
    while((estadoq != 1) or (estadoq != 2) or (estadoq != 3)):
        estadoq = int(input("Seleccione el nuevo estado del inmueble. 1 - Disponible, 2 - Reservado, 3 - Vendido: \n"))
        if(estadoq == 1):
            dic[propiedadnumero-1]['estado'] = 'Disponible'
            break
        elif(estadoq == 2):
            dic[propiedadnumero-1]['estado'] = 'Reservado'
            break
        elif(estadoq == 3):
            dic[propiedadnumero-1]['estado'] = 'Vendido'
            break
        else:
            print("Ingresaste un valor no valido")
    print(f"El nuevo estado del inmueble es el siguiente: \n {dic[propiedadnumero-1]}")

#funcion para calcular el precio de los inmuebles

def calculoPrecio(dic, indice):
    if(dic[indice]['zona'] == 'A'):
        return(dic[indice]['metros'] * 100) + (dic[indice]['habitaciones'] * 500) + (dic[indice]['garaje'] * 1500) * (1 - (2023 - dic[indice]['año']) / 100)
    elif(dic[indice]['zona'] == 'B'):
        return(((dic[indice]['metros'] * 100) + (dic[indice]['habitaciones'] * 500) + (dic[indice]['garaje'] * 1500) * (1 - (2023 - dic[indice]['año']) / 100)) * 1.5)
    elif(dic[indice]['zona'] == 'C'):
        return(((dic[indice]['metros'] * 100) + (dic[indice]['habitaciones'] * 500) + (dic[indice]['garaje'] * 1500) * (1 - (2023 - dic[indice]['año']) / 100)) * 2)


#funcion para buscar inmuebles por valor(punto 3)

def busquedaInmueble(dic, presupuesto):
    listaPrecios = []
    i = 0
    w = 0
    propiedades = 0
    for e in dic:
        if(int(calculoPrecio(dic, i) <= presupuesto) & (dic[i]['estado'] != 'Vendido')):
            #aca si no pones el copy() todos los cambios que hagas los va a agregar a la lista original
            listaPrecios.append(dic[i].copy())
            propiedades = propiedades + 1
            listaPrecios[w]['precio'] = calculoPrecio(dic, i)
            w = w + 1
        i = i + 1
    x = 0    
    for h in listaPrecios:
        print(listaPrecios[x])
        x = x + 1   
    print(f"\nLa busqueda termino con {propiedades} inmuebles encontados.")

#funcion para mostrar la lista de inmuebles

def mostrarListaInmuebles(dic):
    print("La lista de inmuebles es la siguiente: \n")
    x = 0    
    for e in dic:
        print(dic[x])
        x = x + 1

#llamado a la funcion principal

inmobiliariaApp(listaInmobiliaria)