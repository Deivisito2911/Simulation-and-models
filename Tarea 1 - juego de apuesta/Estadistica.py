import random
moneda = ["cara","sello"]

def numeropar (num):
    if num % 2 == 0 :
        return True
    else:
        return False

def Lanzar () :
    dado = random.randint(1,6)
    monedaLanzada = random.choice(moneda)
    esPar = numeropar(dado)
    if esPar == True and monedaLanzada == "cara":
        return True
    else:
        return False

def main() :
    contPerdida = 0
    contGanada = 0
    print("Bienvenido a la simulacion del lanzamiento")
    n = int(input("Introduzca el numero de veces que se lanzara : "))
    for i in range(n):
        esGanador = Lanzar()
        if esGanador == False:
            contPerdida+= 1
        else:
            contGanada+= 1
    print("Ganadas : ",contGanada," Perdidas : ",contPerdida)

main()