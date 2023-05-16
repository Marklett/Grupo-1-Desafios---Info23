import random

#Mensaje de bienvenida
print("\n\n------------------------------INFORMATORIO 2023----------------------------------------")
print("---------------------------------------------------------------------------------------")
print("-----------------------Desafío 3: Adivina el número------------------------------------ \n")
print("GRUPO 1- PARTICIPARON DE LA ELABORACIÓN DEL DESAFÍO: Mercado Alejandro y Pedro Galarza.\n")
print("Integrantes del grupo: Mercado Alejandro, Quiroz Agustín, Pedro Galarza, Maciel Enzo")
print("Máximo Saleh, Marighetti José Juan, Carrazco Enzo, Brunelli Oscar Ariel, Fernández Braian")
print("Echaide Silvina, Luxen Lucas Sebastian, Mendoza Luciano Leonel, Luna Maximiliano")
print("--------------------------------------------------------------------------------------\n")

player = input("Jugador, ingresá tu nombre: \n\n")

#se establece un numero aleatorio del 1 al 100
numeroAleatorio = (random.randint(1, 100))

#se usa una variable para intentos y otra para el contador de intento realizado, seguir jugando es para el while de jugar nuevamente 
seguirJugando = 1
intentos = 8
intento = 1

print(f"\nHola {player}", end='. ')

#mientras que seguir jugando sea 1
while(seguirJugando == 1):
   # print(numeroAleatorio)
    print(f"El numero a adivinar se encuentra entre el 1 y el 100. ¡Tenés {intentos} intentos para adivinarlo! \n")
#mientras que la cantidad de intentos disponible sea mayor o igual al intento actual
    while( intentos >= intento):
        nUser = input("Ingresa un número: ")
        #si lo ingresado es un digito se convierte a entero
        if(nUser.isdigit() == True):
            nUser = int(nUser)
            #si no se supero la cantidad de intentos se realiza lo siguiente
            if(intentos >= intento):
                #si el numero es igual se imprime lo siguiente mencionando el nombre, el numero y el intento en el que se adivino, luego se corta el bucle
                if(numeroAleatorio == nUser):
                    print("\n----------------------------------------\n")
                    print(f"{player}, adivinaste el número {numeroAleatorio} en el intento {intento}.\n")
                    print("-------¡Felicitaciones, ganaste!--------")
                    print("\n----------------------------------------\n")
                    break
                #sino , se suma un intento a intentos actuales, y se avisa si el numero ingresado fue mayor o menor al numero a adivinar. Al final se invita a ingresar un nuevo numero y se avisa cuantos intentos quedan
                else:
                    intento = intento + 1
                    if(intento != intentos + 1):
                        if(numeroAleatorio > nUser):
                            print("El numero a adivinar es MAYOR al que ingresaste", end=". ")
                        if(numeroAleatorio < nUser):
                            print("El numero a adivinar es MENOR al que ingresaste", end=". ")
                        print(f"Vuelve a intentarlo, ¡Te quedan {(intentos - intento) + 1} intentos! \n")
        #si no es un digito entonces no ingreso un numero entero y se le avisa al user, sin quitarle intentos, se levuelve a pedir que ingrese un numero
        else:
            print(f"El caracter que ingresaste no es un número entero... \n")
    #si el intento es mayor a la cantidad de intentos disponibles, es decir, si se agotaron los intentos, se imprime el mensaje de game over con el numero a adivinar
    if(intento > intentos):
        print(f"\n{player} ¡Perdiste! El numero a adivinar era {numeroAleatorio}. \nÁnimos, puedes volver a intentarlo :)")
        #se pregunta al user si quiere jugar de nuevo, si dice que si se vuelve a randomizar el numero a adivinar y se repite el bucle, los intentos se reinician
    seguirJugando = int(input("\n¿Quieres volver a jugar? 1- Si, 2 - No: \n"))
    numeroAleatorio = (random.randint(1, 100))
    intento = 1
#si no se quiere jugar mas, se imprime este texto
print("\n------------------------------------------")
print("--¡Gracias por jugar! vuelvas prontos...--")
print("------------------------------------------\n")