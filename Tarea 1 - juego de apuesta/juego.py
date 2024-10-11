import random
from os import system
moneda = ["cara","sello"]
repeticiones = 2
Inicial = 1000

def numeropar (num):
    if num % 2 == 0 :
        return True
    else:
        return False

def Juego (monedas,apuesta) :
    dado = random.randint(1,6)
    monedaLanzada = random.choice(moneda)
    esPar = numeropar(dado)
    if esPar == True and monedaLanzada == "cara":
        return (monedas + apuesta)
    else:
        return (monedas - apuesta)

def main() :
    meta = 2000
    contGanada = 0
    contPerdida = 0
    print("Bienvenido al juego de apuestas")
    apuestaInicial = float(input("Introduzca su apuesta inicial : "))
    for i in range(100):
        cantMoneda = Inicial
        apuesta = apuestaInicial
        while cantMoneda < meta and cantMoneda > 0:
            inicial = cantMoneda
            cantMoneda = Juego(cantMoneda,apuesta)
            if cantMoneda < inicial:
                apuesta*=2
            else:
                apuesta = apuestaInicial
            if apuesta > cantMoneda :
                apuesta = cantMoneda
            #print("monedas : ",cantMoneda," apuesta : ",apuesta)
        if int(cantMoneda) == 0:
            contPerdida+= 1
        elif int(cantMoneda) >= meta:
            contGanada+= 1
    print("Ganadas : ",contGanada," Perdidas : ",contPerdida)

main()