def Palindromo():
    palabra = str(input("Digite una palabra:")) #Declaro la variable y pongo al usuario a introducir la palabra o frase
    caracteres = "!?-_.,:; " #Estos son los caracteres que quiero que elimine de la palabra o frase, incluso espacio
    valorPalabra = ''.join(x for x in palabra if x not in caracteres) #Almaceno la palabra o frase en otra variable y le elimino todos los caracteres especiales y espacios
    palabra = ''.join(x for x in palabra if x not in caracteres) #Hago lo mismo en la variable -palabra- que utilicé al comienzo
    if(valorPalabra[::-1].lower() == palabra.lower()): #Hago la comparacion entre la palabra/frase invertida y la palabra/frase original
        print("Es palindromo")
    else:
        print("No es palindromo")
if __name__ == "__main__": #Método main
    Palindromo()