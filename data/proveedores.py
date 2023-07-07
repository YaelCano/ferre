import core
import os
diccProveedores = {"data":[]}
def LoadInfoProveedores():
    global diccProveedores
    if (core.checkFile("proveedores.json")):
        diccCliente = core.LoadInfo("proveedores.json")
    else:
        core.crearInfo("proveedores.json",diccProveedores)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE PROVEEDORES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar proveedores")
    print("3. Editar proveedores")
    print("4. Eliminar proveedores")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        data ={
            "id":input("Ingrese el Id del proveedores :"),
            "nombre":input("Ingrese el Nombre del proveedores :"),
            "email":input("Ingrese el Email del proveedores :"),
        }

        core.crearInfo("proveedores.json",data)

    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()