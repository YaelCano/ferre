import core
import os
diccCliente = {"data":[]}
def LoadInfoCliente():
    global diccCliente
    if (core.checkFile("clientes.json")):
        diccCliente = core.LoadInfo("clientes.json")
    else:
        core.crearInfo("clientes.json",diccCliente)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("pause")
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input(": "))

    if (opcion == 1):
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','REGISTRO DEL CLIENTES',' '))
        print('+','-'*49,'+')
        data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
        }
        #diccCliente["data"].append(data)
        core.crearInfo("clientes.json",data)

    elif (opcion == 2):
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR EL CLIENTE',' '))
        print('+','-'*49,'+')
        codBusq = input("Ingrese el codigo del cliente a buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if codBusq in item["id"]:
                print(f'Id del cliente: {item["id"]}')
                print(f'Nombre cliente: {item["nombre"].upper()}')
                print(f'email del cliente: {item["email"]}')
        input("presione enter para continuar...")

    elif (opcion == 3):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DEL CLIENTE',' '))
        print('+','-'*49,'+')
        codBusq = input("Ingrese el codigo del cliente a buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if codBusq in item["id"]:
                item["nombre"] = input("Ingrese el nuevo nombre o presione enter para omitir: ") or item["nombre"]                
                item["email"] = input("Ingrese el nuevo email o presione enter para omitir: ") or item["nombre"]                
                core.editInfo("clientes.json",diccCliente)
    
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACIÓN DEL CLIENTE',' '))
        print('+','-'*49,'+')
        codBusq = input("Ingrese el codigo del cliente a buscar: ")
        for i,item in enumerate(diccCliente["data"]):
            if codBusq in item["id"]:
                itemDel = diccCliente["data"].pop(i)
                diccCliente["data"].pop(i)
                core.editInfo("clientes.json",diccCliente)
                input("Presione enter para continuar....")
                #core.crearInfo("clientes.json",itemdel)
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()
        

    
