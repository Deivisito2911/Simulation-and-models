import random
from os import system
moneda = ["cara","sello"]
repeticiones = 2
Inicial = 1000

def numeropar (num): #Funcion para identificar numero par
    if num % 2 == 0 :
        return True
    else:
        return False

def Juego (monedas,apuesta) :#Funcion que simula el lanzamiento
    dado = random.randint(1,6)#Dado de 1 a 6
    monedaLanzada = random.choice(moneda) #cara o sello
    esPar = numeropar(dado)
    if esPar == True and monedaLanzada == "cara":
        return (monedas + apuesta) #Gana el jugador
    else:
        return (monedas - apuesta) #Gana la casa

def main() :
    meta = 2000 #Meta para ganar
    contGanada = 0
    contPerdida = 0
    print("Bienvenido al juego de apuestas")
    apuestaInicial = float(input("Introduzca su apuesta inicial : "))#apuesta que se usara
    for i in range(100): #Cantidad de juegos que se simularan
        cantMoneda = Inicial
        apuesta = apuestaInicial
        while cantMoneda < meta and cantMoneda > 0:
            inicial = cantMoneda
            cantMoneda = Juego(cantMoneda,apuesta)
            if cantMoneda < inicial:#Al ganar se dobla la apuesta
                apuesta*=2
            else:
                apuesta = apuestaInicial#Al perder volvemos a apostar lo incial
            if apuesta > cantMoneda :
                apuesta = cantMoneda#Si la apuesta supera la cantidad de monedas se apuesta todo
            #print("monedas : ",cantMoneda," apuesta : ",apuesta)
        if int(cantMoneda) == 0:
            contPerdida+= 1#Gana la casa
        elif int(cantMoneda) >= meta:
            contGanada+= 1#Gana el jugador
    print("Ganadas : ",contGanada," Perdidas : ",contPerdida)#Totalizacion

main()