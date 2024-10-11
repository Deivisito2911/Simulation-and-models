import random
moneda = ["cara","sello"]

def numeropar (num):
    if num % 2 == 0 :
        return True
    else:
        return False

def Lanzar () : #Simulacion del lanzamiento
    dado = random.randint(1,6)#Lanzamiento de dado
    monedaLanzada = random.choice(moneda)#Lanzamiento de moneda
    esPar = numeropar(dado)
    if esPar == True and monedaLanzada == "cara":
        return True#Gana el jugador
    else:
        return False#Gana la casa

def main() :
    contPerdida = 0
    contGanada = 0
    print("Bienvenido a la simulacion del lanzamiento")
    n = int(input("Introduzca el numero de veces que se lanzara : "))#Numero de lanzamientos
    for i in range(n):
        esGanador = Lanzar()
        if esGanador == False:
            contPerdida+= 1#Gana la casa
        else:
            contGanada+= 1  #Gana el jugador
    print("Ganadas : ",contGanada," Perdidas : ",contPerdida)#Estadisticas

main()