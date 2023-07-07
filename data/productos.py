import core
import os
diccProductos = {"data":[]}
def LoadInfoProductos():
    global diccProductos
    if (core.checkFile("productos.json")):
        diccProduct = core.LoadInfo("productos.json")
    else:
        core.crearInfo("productos.json",diccProductos)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE PRODUCTOS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar ")
    print("3. Editar")
    print("4. Eliminar ")
    print("5. Activar o inactivar producto")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        data ={
            "codigo":input("Ingrese el codigo del producto: "),
            "nombre_product":input("Ingrese el Nombre del producto: "),
        }

        core.crearInfo("productos.json",data)

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