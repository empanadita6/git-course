#Importando las librerias
from math import trunc
import random, winsound, os

def playsound(flags):
    if flags == 2:
        os.system('aplauso.mp3')
    else:
        winsound.PlaySound("*", winsound.SND_ASYNC)
    return

def adivina():
    #Declarando todas las variables
    vida = 10
    secret_num = random.randrange(1,100)
    won = False
    entrada_usuario = ""

    print("El numero secreto es {}".format(secret_num))

    #Bucle para mantener el juego
    while(not won and vida >= 1):

        #Validando la entrada
        try:
            entrada_usuario = int(input("Entre número..:"))
        except ValueError:
            print("Debe entrar un valor entre 1 y 100")
            continue
        if entrada_usuario == secret_num:
            won = True
            print("¡Usted Ganó!")
            playsound(2)
        elif entrada_usuario < secret_num:
            print("¡Entre un # mayor!")
            playsound(1)
        if entrada_usuario > secret_num:
            print("¡Entre un # menor!")
            playsound(1)
        vida -= 1
        if vida < 1 and not won:
            print("USTED PERDIÓ")

if __name__ == "__main__":
    adivina()