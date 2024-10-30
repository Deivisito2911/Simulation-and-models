import random
probExito = 0.40#Creacion de varibales globales
probFallar = 1 - probExito
gananciaEmpresa = 0.60
gananciaEstado = 1 - gananciaEmpresa
cantBarriles = 300000
precioExploracion = 1000000
precioBarril = 150
cantExploraciones = 1000000

def Probabilidad():#probabilidad de fallar o no una exploracion
    return random.choices([True, False], weights=[probExito, probFallar])[0]

def exploracion(barriles,cuentaEmpresa,cuentaEstado):#Simulacion de distintas exploraciones
    exitos = 0
    for idx in range(cantExploraciones):
        cuentaEmpresa-= precioExploracion
        if Probabilidad():#Si aciertan se actualizan las variables
            exitos+=1
            barriles+= cantBarriles
            cuentaEmpresa+= ((cantBarriles*precioBarril)*gananciaEmpresa)
            cuentaEstado+= ((cantBarriles*precioBarril)*gananciaEstado)
    exito = exitos / cantExploraciones
    return barriles,cuentaEmpresa,cuentaEstado,exito#Actualizacion de variables

def main():#simulacion
    barriles = 0
    cuentaEmpresa = 0
    cuentaEstado = 0
    barriles, cuentaEmpresa, cuentaEstado, umbralExito = exploracion(barriles,cuentaEmpresa,cuentaEstado)
    print("Cantidad de exploraciones : ",cantExploraciones)
    print("Cantidad de barriles obtenidos : ",barriles)
    print("Estado de cuenta de la empresa : ",cuentaEmpresa)
    print("Total ganancias del estado : ",cuentaEstado)
    print(f"Umbral de exito : {umbralExito * 100:.2f}%")
    
main()