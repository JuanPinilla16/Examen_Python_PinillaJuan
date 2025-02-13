import json
def abrirJSON():
    dicFinal={}
    with open("Servicios.JSON","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal        

def guardarJSON(dic):
    with open("Servicios.JSON","w") as outfile:
        json.dump(dic,outfile)

Servicios={}

booleanito = True
while (booleanito==True):

    print("############################")
    print("#####---Bienvenido A Movistar---#######")
    print("############################")
    print("¿A que te gustaria Ingresar?")
    print("1. Coordinador")
    print("2. Usuario")
    print("3. Registrarse")
    print("4. Cerrar programa")
    opt=input(":")
    ##Leer archivo JSON y pasarlo a dic
    Servicios=abrirJSON()
    if(opt=="1"):
        print("¿Qué te gustaría hacer?")
        print("1.Servicios")
        opt2=int(input(":"))
        if (opt2==1):
            print("¿Qué te gustaría hacer?")
            print("1.Verlos")
            print("2.Agregar uno nuevo")
            print("3.Modificar uno")
            print("4.Eliminar uno")
            opt3=int(input(":"))
            if(opt3==1):
                print("############################")
                print("#####---Servicios Disponibles---#######")
                print("############################")
                for i in range(len(Servicios[opt]["Megas"])):
                    print(Servicios[opt]["Megas"][i+1])
                print("############################")
            elif(opt3==2):
                nuevoServicio=input("¿Como se llama el nuevo Servicio?:")
                Servicios[opt]["servicio"].append(nuevoServicio)
                #Guardar diccionario en el archivo JSON
                guardarJSON(Servicios)
                print("Servicio Agregado")
    elif(opt=="4"):
        booleanito = False
        break
            

