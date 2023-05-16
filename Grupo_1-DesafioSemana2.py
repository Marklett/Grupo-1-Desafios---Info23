"""

Desafío 2: Analizador de textos
Requisitos técnicos:
Se te pide crear un programa que le pida al usuario que ingresar un texto
cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
elección.
Nuestro código va a procesar esa información para realizar los análisis
necesarios para devolverle al usuario la siguiente información:
1- Cantidad de veces que aparece cada una de letras que eligió.
Tip 1: almacenar las letras en una lista para usar algún método de contar 
un substring en un string
Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar 
que se encuentren todas las letras, pasa tanto el texto original como las letras 
a buscar a minúscula.
2- Cuantas palabras hay en total en todo el texto.
Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular
su longitud.
3- Cual es la primera letra y cuál es la última. (Indexación)
4- Mostrar el texto en orden inverso.
5- Decir si la palabra "python" aparece en el texto.
Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el
booleano con un
string para mostrar al usuario.

"""

#Mensaje de bienvenida
print("\n\n------------------------------INFORMATORIO 2023----------------------------------------")
print("---------------------------------------------------------------------------------------")
print("-----------------------Desafío 2: Analizador de textos--------------------------------- \n")
print("GRUPO 1- INTEGRANTES: Mercado Alejandro, Quiroz Agustín, Pedro Galarza, Maciel Enzo\n")
print("Máximo Saleh, Marighetti José Juan, Carrazco Enzo, Brunelli Oscar Ariel, Fernández Braian\n")
print("Echaide Silvina, Luxen Lucas Sebastian, Mendoza Luciano Leonel, Luna Maximiliano\n")
print("--------------------------------------------------------------------------------------\n")

#Inputs del user, tanto texto como letras, en el mismo input se establece que se convertiran los caracteres en minuscula

texto = input("Ingresar un texto cualquiera, por ejemplo, un artículo o una frase: \n\n")
letras = input("\nIngresa 3 letras de tu eleccion: \n")
texto = texto.lower()
letras = letras.lower()

#1) cantidad de veces que una letra aparece en el texto

letra1 = texto.count(letras[0])
letra2 = texto.count(letras[1])
letra3 = texto.count(letras[2])

#2) cantidad de palabras que aparecen en el texto

textoEnPalabras = texto.split(" ")
cantidadPalabrasTexto = len(textoEnPalabras)

#3) Primera palabra y ultima

primeraLetra = texto[0]
ultimaLetra = texto[-1]

#4) Mostrar el texto en orden inverso.

textoEnReversa = texto[::-1]

#mostrar texto con palabras en orden inverso

copiaLista = textoEnPalabras.copy()
copiaLista.reverse()
textoReversa = ' '.join(copiaLista)

#5) Decir si la palabra 'python' aparece, usando un booleano y un diccionario asociado. Se definio una funcion para ello

pythonDic = {'Python' : ['La palabra -Python- SI se encuentra dentro del texto','La palabra -Python- NO se encuentra dentro del texto']}
pythonBool = texto.count("python")
def python():
	if (pythonBool):
		return (pythonDic['Python'][0])
	else: 
		return(pythonDic['Python'][1])

#Prints de todos los resultados

print("\n---------------------------------\n")
print(f"1)La cantidad de veces que aparece la '{letras[0]}' es {letra1}.")
print(f"  La cantidad de veces que aparece la '{letras[1]}' es {letra2}.")
print(f"  La cantidad de veces que aparece la '{letras[2]}' es {letra3}.")
print(f"2)El Texto ingresado tiene {cantidadPalabrasTexto} palabras.")
print(f"3)La primera letra del texto ingresado es:'{primeraLetra}'.")
print(f"  La ultima letra del texto ingresado es: '{ultimaLetra}'.")
print(f"4)Asi se leeria el texto al reves: \n'{textoEnReversa}'.")
print(f"  Asi se leeria el texto con palabras en orden inverso: \n'{textoReversa}'.")
print(f"5)¿Aparece la palabra 'Python'?': {python()}.\n")



