from os import system
cadenaMaxima = " Cadena de 20 años"
cadenaMinima = " Cadena de 1 año"
cadenaIntermedia = " Cadena de 5 años"
#cantPrisioneros = 2

def interaccion(nombrePrisionero):
    system("cls")
    print("Turno del prisionero: ",nombrePrisionero)
    system("pause"); system("cls")
    print("Hola Prisionero ",nombrePrisionero)
    print("Tienes la opcion de confesar o callar ")
    confesion = 0
    while confesion == 0:
        confesion = int(input(" 1- Confesar \n 2- Callar \n"))
        system("cls")
        if confesion == 1:
            return True
        elif confesion == 2:
            return False
        else:
            print("Escogio una opcion invalida")
            system("pause"); system("cls")
        system("cls")

def main():
    system("cls")
    print("Bienvenido al juego del prisionero : \nLas reglas son las siguientes:\n-Son dos prisioneros que han cometido un crimen y tienen la opcion de callar o confesar\n-Si un jugador calla y el otro confiesa el que calla tiene 20años de prision y el otro esta libre\n-Si ambos callan tienen 1 años de prision cada uno\n-Si ambos confiesan tienen 5 años de prision cada uno")
    system("cls")
    jugador1 = input("Introduzca el nombre del jugador 1 : ")
    jugador2 = input("Introduzca el nombre del jugador 2 : ")
    opcionJ1 = interaccion(jugador1)
    opcionJ2 = interaccion(jugador2)
    print("Las respectivas sentencias han sido calculadas...")
    system("pause");system("cls")
    if opcionJ1 == True and opcionJ2 == True:
        print("Prisionero: ",jugador1,cadenaIntermedia,"\nPrisionero: ",jugador2,cadenaIntermedia,)
    elif opcionJ1 == True and opcionJ2 == False:
        print("Prisionero: ",jugador1," Libre  \nPrisionero: ",jugador2,cadenaMaxima)
    elif opcionJ1 == False and opcionJ2 == True:
        print("Prisionero: ",jugador1,cadenaMaxima,"\nPrisionero: ",jugador2," Libre")
    else:
        print("Prisionero: ",jugador1,cadenaMinima,"\nPrisionero: ",jugador2,cadenaMinima)

main()