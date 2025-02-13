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

    print("####################################")
    print("####---Bienvenido a movistar---####")
    print("####################################")
    print("¿Que te gustaria hacer?")
    print("1.Ver Servicios Actuales")
    print("2.Ver Usuarios")
    print("3.Modificar Usuarios")
    print("4.Cerrar Programa")
    opt=input(":")



Servicios=abrirJSON()
opt2=int(input(":"))
if(opt2==1):
    print("Servicios Disponibles")
    for i in range (len(Servicios[opt]["servicios"])):
        print(Servicios[opt]["servicios"][i])
