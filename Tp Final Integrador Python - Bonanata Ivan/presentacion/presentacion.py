import time
from colorama import Fore, Back, init
init(autoreset=True)

from negocio.negocio import (iniciarDatos, agregarProducto, verProducto, obtenerNombre, obtenerCategoria, obtenerRango, obtenerCantidad,)

def menu():
    """Menu general del sistema"""
    #sesion=login(usuarioAdmin, contraseAdmin)
    inicioDatos()
    while True: # Bucle iterativo hasta BREAK, permite seleccionar opciones con MATCH, vuelve si se selecciona menos de 1 o mas de 5.
        print(Back.WHITE + Fore.BLACK+
        """
        --- MENU ---\n1. Agregar producto\n2. Ver productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir
        """)
        opcionMenu= validarSelectorMenu()
        match opcionMenu: #Selector de menu de opciones
            case 1: 
                while True:
                    print("AGREGAR PRODUCTO")
                    resultadoAgregar= agregarProductos()
                    print(f"{resultadoAgregar}")
                    selector= validarSalirCase() 
                    if selector=="s":
                        continue
                    else:
                        print(f"Finalizando carga de productos.\n....\n...\n..\n.")
                        break                
            case 2:
                while True:
                    print("VER PRODUCTO")
                    resultadoVer= verProductos()
                    print(f"{resultadoVer}")
                    if selector=="s":
                        continue
                    else:
                        print(f"Finalizando visualziacion de productos.\n....\n...\n..\n.")
                        break 
            case 3:
                while True:   
                    print("BUSCAR PRODUCTO")
                    resultadoBuscar= buscarProductosMenu()
                    print(f"Finalizando busqueda de productos.\n....\n...\n..\n.")
                    break 
            case 4:
                while True:
                    print("ELIMINAR PRODUCTOS")
                    resultadoEliminar= eliminarProducto(productoLista)
                    print(f"{resultadoEliminar}")
                    if selector=="s":
                            continue
                    else:
                        print(f"Finalizando carga de productos.\n....\n...\n..\n.")
                        break 
            case 5:
                print("SALIR")
                while True:
                    selectorSalida= validarSalirCase()
                    if selectorSalida == "s":
                        continue
                    else:
                        print("Finalizando programa.\n....\n...\n..\n.")
                        break
                resultadoSalir=salir()
                if resultadoSalir==True:
                    break

def inicioDatos():
    print("Inicializando la base de datos, aguarde un instante")
    for n in range (3, 0, -1):
        print(".")
        time.sleep(1)
    centinelaInfo= iniciarDatos()
    print(centinelaInfo)

def agregarProductos():
    """Agregar diccionario de productos a la matriz y base de datos"""
    print("1. Agregar producto: Indique su nombre, descripcion, cantidad, precio(sin centavos), y categoria.\nPara salir inserte un valor vacio en nombre [enter].")
    while True:
        productoAgregar= {} # Diccionario reutilizable de ingreso de nuevos productos
        _agregarNombre= input("Ingrese el nombre: ").strip().title() # Varibles reutilizables para ingreso de cada datos y tipo de productos nuevos
        _agregarDescripcion= input("Ingrese su descripcion: ").strip().title()
        _agregarCantidad= input("Ingrese la cantidad: ").strip() 
        _agregarPrecio= input("Ingrese el precio: ").strip()
        _agregarCategoria= input("Ingrese la categoria: ").strip().title()
        
        if _agregarNombre == "" or _agregarDescripcion == "" or _agregarCantidad == "" or _agregarPrecio == "" or _agregarCategoria == "":
            print("Error: Todos los campos son obligatorios. Intente nuevamente.")
            continue            
        if (_agregarNombre.isdigit() or _agregarDescripcion.isdigit() or _agregarCategoria.isdigit() or 
            not _agregarCantidad.isdigit() or not _agregarPrecio.isdigit()):
            print("Error de tipeo: Verifique letras y números. Intente nuevamente.")    
            continue           
       
        _agregarNumCantidad= int(_agregarCantidad) # Se castea la variable a int despues de corroborar la logica del dato
        _agregarNumPrecio= int(_agregarPrecio) # Se castea la variable a int despues de corroborar la logica del dato       
        productoAgregar= {
            "Nombre": _agregarNombre,
            "Descripcion": _agregarDescripcion,
            "Cantidad": _agregarNumCantidad,
            "Precio": _agregarNumPrecio,
            "Categoria": _agregarCategoria
        }

        break
    return cargaDato


def verProductos():
    """Muestra todos los productos disponibles"""
    print("A continuacion poda ver todos lo productos diponibles")
    while True:        
        centinelaInfo= ""
        if resultadoVer:
            for datos in resultadoVer:
                    centinelaInfo+= (f"ID: {datos[0]}, NOMBRE: {datos[1]}, DESCRIPCION: {datos[2]}, CANTIDAD: {datos[3]}, PRECIO: ${datos[4]:.2f}, CATEGORIA: {datos[5]}. \n")               
        else: 
            centinelaInfo= (f"No hay productos cargados en la base de datos.\n")

        return centinelaInfo


def buscarProductosMenu():
    """Selecciona que buscar de un producto"""
    while True:   
        print("Como desea buscar?.\n")
        print("1: Nombre")
        print("2: Categoria")
        print("3: Rango de precio")
        print("4: Minimo stock")
        print("5: Salir a menu principal")
        selector= validarSelectorMenuBusqueda()
        match selector:
            case 1: 
                print("BUSCAR POR NOMBRE")
                while True:
                    centinelaInfo= busquedaNombre()
                    print (f"{centinelaInfo}")

                    selectorSalida= validarSalirCase()
                    if selectorSalida == "s":
                        continue
                    else:
                        print("Finalizando busqueda de productos.\n....\n...\n..\n.")
                        break 
            case 2:   
                print("BUSCAR POR CATEGORIA")
                while True: 
                    centinelaInfo= busquedaCategoria()
                    print (f"{centinelaInfo}")

                    selectorSalida= validarSalirCase()
                    if selectorSalida == "s":
                        continue
                    else:
                        print("Finalizando busqueda de productos.\n....\n...\n..\n.")
                        break
            case 3: 
                print("BUSCAR POR CATEGORIA")
                while True: 
                    centinelaInfo= busquedaRango()
                    print (f"{centinelaInfo}")

                    selectorSalida= validarSalirCase()
                    if selectorSalida == "s":
                        continue
                    else:
                        print("Finalizando busqueda de productos.\n....\n...\n..\n.")
                        break 
            case 4:
                print("BUSCAR POR STOCK INFERIOR")
                while True: 
                    centinelaInfo= busquedaCantidad()
                    print (f"{centinelaInfo}")

                    selectorSalida= validarSalirCase()
                    if selectorSalida == "s":
                        continue
                    else:
                        print("Finalizando busqueda de productos.\n....\n...\n..\n.")
                        break 
            case 5:
                print("VOLVIENDO AL MENU PRINCIPAL.")
                for n in range (1,3):
                    time.sleep(1)
                    print(".")
                break


def busquedaNombre():
    while True:
        nombreBuscar= input("Ingrese el nombre a buscar").strip().title()           
        if nombreBuscar == "" or nombreBuscar.isdigit():
            print("Error de tipeo, vuelva a intentarlo")
            continue
        else:
            break

    resultadoNombre= obtenerNombre(nombreBuscar)
    if resultadoNombre:           
        centinelaInfo= (f"El producto que busco: ID: {resultadoNombre[0]}, NOMBRE: {resultadoNombre[1]}, DESCRIPCION: {resultadoNombre[2]}, CANTIDAD: {resultadoNombre[3]}, PRECIO: {resultadoNombre[4]}, CATEGORIA: {resultadoNombre[5]}.\n")
    else:
        centinelaInfo= (f"No se encontraron datos que coincidan con el nombre: {nombreBuscar}")

    return centinelaInfo  


def busquedaCategoria():
    while True:
        categoriaBuscar= input("Ingrese la categoria a buscar").strip().title()           
        if categoriaBuscar == "" or categoriaBuscar.isdigit():
            print("Error de tipeo, vuelva a intentarlo")
            continue
        else:
            break
    resultadoCategoria= obtenerCategoria(categoriaBuscar)
    centinelaInfo= ""
    if resultadoCategoria:
        for datos in resultadoCategoria:
                centinelaInfo+= (f"ID: {datos[0]}, NOMBRE: {datos[1]}, DESCRIPCION: {datos[2]}, CANTIDAD: {datos[3]}, PRECIO: ${datos[4]:.2f}, CATEGORIA: {datos[5]}. \n")               
    else: 
        centinelaInfo= (f"No se encontro ningun producto en la categoria: {categoriaBuscar}.\n")
    
    return centinelaInfo

def busquedaRango():
    while True:
        rangoBuscarMin= input("Ingrese el rango minimo de precio").strip().title()   
        rangoBuscarMax= input("Ingrese el rango minimo de precio").strip().title()         
        if not rangoBuscarMin.isdigit() or not rangoBuscarMax.isdigit():
            print("Error de tipeo: Ambos campos deben ser numeros enteros positivos. Vuelva a intentarlo.")
            continue
        if rangoBuscarMin > rangoBuscarMax:
            print("Error: El precio minimo no puede ser mayor que el precio maximo. Vuelva a intentarlo.")
            continue
        else:
            break

    resultadoRango= obtenerRango(rangoBuscarMin, rangoBuscarMax)
    centinelaInfo= ""
    if resultadoRango:
        for datos in resultadoRango:
                centinelaInfo+= (f"ID: {datos[0]}, NOMBRE: {datos[1]}, DESCRIPCION: {datos[2]}, CANTIDAD: {datos[3]}, PRECIO: ${datos[4]:.2f}, CATEGORIA: {datos[5]}. \n")               
    else: 
        centinelaInfo= (f"No se encontro ningun producto en la categoria con esos parametros: {rangoBuscarMin} y {rangoBuscarMax}.\n")
    
    return centinelaInfo


def busquedaCantidad():
    while True:
        cantidadBuscar= input("Ingrese el stock minimo a buscar").strip().title()           
        if cantidadBuscar == "" or (not cantidadBuscar.isdigit()):
            print("Error de tipeo, vuelva a intentarlo")
            continue
        else:
            break
    resultadoCantidad= obtenerCantidad(cantidadBuscar)
    centinelaInfo= ""
    if resultadoCantidad:
        for datos in resultadoCantidad:
                centinelaInfo+= (f"ID: {datos[0]}, NOMBRE: {datos[1]}, DESCRIPCION: {datos[2]}, CANTIDAD: {datos[3]}, PRECIO: ${datos[4]:.2f}, CATEGORIA: {datos[5]}. \n")               
    else: 
        centinelaInfo= (f"No se encontro ningun producto en la categoria: {categoriaBuscar}.\n")
    
    return centinelaInfo


def validarSelectorBusquedaMenu(minimo=1, maximo=5): # Parametros predefinidos, se pueden pasar los argumentos al ser llamada para usar en otro menu o seleccion conn numero entero.
    """Validar la seleccion ingresada por el usuario, deben ser numero enteros entre el maximo y minimo del menu. Luego castea a entero"""
    while True:
        opciones= input(f"Seleccionar una opción del {minimo} al {maximo}: ")
        if not opciones.isdigit():
            print("Ingreso de opcion invalido, vuelva a intentarlo.")
            continue 
        opcion_int= int(opciones) # Casteamos el ingreso de opcion a entero para validar la opcion
        if (opcion_int < minimo  or opcion_int > maximo): # Validamos solo rangos entre los paramatros 1 a 5
            print("Ingreso de opcion fuera de rango, vuelva a intentarlo.")
            continue
        else:
            break
    return opcion_int


def validarSalirCase():
    """Se valida el correcto tipeo"""
    _selector=input(f"Desea continuar en esta seccion? (S/N): ").strip().lower()
    while _selector.isdigit() or (_selector!= "s" and _selector!= "n"):
        print("Error de tipeo, solo S para continuar o N para salir ")
        _selector=input(f"Desea continuar en esta seccion? (S/N): ").strip().lower()
    return _selector


def salir():
    """Muestra mensajes de despedida al cerrar el programa"""
    print("Finalizando, aguarde. \n")
    for n in range(3, 0, -1):
        time.sleep(1)
        print(Back.RED + f"Cerrando programa {n}.")
    return True







