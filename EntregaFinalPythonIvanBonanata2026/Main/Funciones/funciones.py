import time

def validarSelectorMenu(minimo=1, maximo=5): # Parametros predefinidos, se pueden pasar los argumentos al ser llamada para usar en otro menu o seleccion conn numero entero.
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

def login(usuario, contraseña):
    """Validar el inicio de sesion, usuario y contraseña en archivo main"""
    while True:
        passOk=False #Centinela de cambio de estado. Permite romper el bucle ya que en el for no se puede
        for n in range (3, 0, -1): # Inicio de sesion con bucle for, se itera 3 veces y se validan los datos. 
            _usuarioIngreso= input("Nombre de usuario: ")
            _contraseIngreso= input("Contraseña: ")
            if n!=1:
                if _usuarioIngreso == usuario:
                    if _contraseIngreso == contraseña:
                        passOk=True
                        print("Bienvenido!")
                        break          
                    else:
                        print(f"Contraseña invalida, le quedan {n-1} intentos ")    
                else:
                    print(f"Usuario inexistente, le quedan {n-1} intentos")
            else:             
                for i in range (5, 0, -1): # Debera esperar 5 segundos para volver a ingresar sus credenciales, se intera con time.sleep
                    time.sleep(1)
                    print(f"Se bloqueo su acceso, vuelva a intentar en: {i}")  
        if passOk: # Hasta no tener un inicio de sesion exitosos no supera el bucle de ingreso.
            break 
    return passOk          

def validarSalirCase():
    """Se valida el correcto tipeo"""
    _selector=input(f"Desea continuar en esta seccion? (S/N): ").strip().lower()
    while _selector.isdigit() or (_selector!= "s" and _selector!= "n"):
        print("Error de tipeo, solo S para continuar o N para salir ")
        _selector=input(f"Desea continuar en esta seccion? (S/N): ").strip().lower()
    return _selector

def agregarProductos(productoLista):
    """Agregar listas de productos a la matriz"""
    print("1. Agregar producto: Indique su nombre, tipo, valor (sin centavos).\nPara salir inserte un valor vacio en nombre [enter].")
    while True:
        _productoAgregar= [] # Lista reutilizable de ingreso de nuevos productos
        _agregarNombre= input("Ingrese el nombre: ").strip().title() # Varibles reutilizables para ingreso de cada datos y tipo de productos nuevos
        _agregarTipo= input("Ingrese el tipo: ").strip().title()
        _agregarPrecio= input("Ingrese el precio: ").strip()
        if _agregarNombre== "" or _agregarTipo== "" or _agregarPrecio== "": # Validamos el ingreso de datos, si desea salir o si tipeo correctamente.
            print(f"Finalizando carga de productos.\n....\n...\n..\n.")
            break
        elif (_agregarNombre.isdigit()) or (_agregarNombre.isdigit()) or (not _agregarPrecio.isdigit()):
            print("Error de tipeo, vuelva a intentarlo")    
            continue
        else:
            _agregarNumPrecio= int(_agregarPrecio) # Se castea la variable a int despues de corroborar la logica del dato
            _productoAgregar.append(_agregarNombre)
            _productoAgregar.append(_agregarTipo)
            _productoAgregar.append(_agregarNumPrecio)# Se completa la carga de variables de la actual lista del producto nuevo
            print(f"Se agrego {_productoAgregar} con exito a la lista de productos")
            productoLista.append(_productoAgregar) # Agregamos el producto a la lista contenedora de productos
        selector= validarSalirCase() 
        if selector=="s":
            continue
        else:
            print(f"Finalizando carga de productos.\n....\n...\n..\n.")
            break
    return f" La lista esta compuesta por: {productoLista}"

def verProductos(productoLista, tupla_productoLista):
    """Ver productos ed las listas como tuplas de una matriz"""
    print("2. Ver productos: Aqui podra visualiar toda la lista de productos disponibles.")
    while True:               
        for tupla in productoLista:
            _subtupla= tupla
            _subtupla= tuple(_subtupla)  # Casteamos en tupla las listas contenidas que se fueron agregando en la opcion 1
            tupla_productoLista.append(_subtupla) # Incorporacion, seria la version nueva de productoLista, pero que se convertira a tupla
        tupla_productoLista= tuple(tupla_productoLista) # Convertimos al final en tupla toda la lista, fuera del bucle para que no se sobreescriba.
        centinelaInfo= (f"Contenido de la lista {tupla_productoLista}. En total son {len(tupla_productoLista)}")
        print(f"{centinelaInfo}")
        selector= validarSalirCase() 
        if selector=="s":
            continue
        else:
            print(f"Finalizando vista de productos.\n....\n...\n..\n.")
            break
    return centinelaInfo

def validarIngreso():
    """Validacion de ingreso de busqueda"""
    _selector=input(f"Por favor, elija el ingreso: nombre del producto (1), su posicion (2) o solo enter para salir: (1/2/): ").strip()
    while _selector!="" and not _selector.isdigit():
        print("Error de tipeo, solo numeros o espacio en blanco para continuar o salir ")
        _selector=input(f"Por favor, elija el ingreso: nombre del producto (1), su posicion (2) o nada para salir: (1/2/)").strip()
    if _selector=="":
        print(f"Finalizando busqueda de productos.\n....\n...\n..\n.")
        return False
    else: 
        opcion_int= int(_selector) # Solo cuando se valida que se ingreso un numero permite continuar con la carga         
    return opcion_int

def validarIngreso2():
    """Valir ingreso de selector"""
    _selector = input("Por favor, elija el ingreso: nombre del producto (1), su posicion (2) o solo enter para salir: (1/2): ").strip()   
    while _selector != "" and not _selector.isdigit():
        print("Error de tipeo, solo numeros o espacio en blanco para salir ")
        _selector = input("Por favor, elija el ingreso: nombre del producto (1), su posicion (2) o nada para salir: (1/2): ").strip()        
    if _selector == "":
        print("Finalizando eliminacion de productos.\n....\n...\n..\n.")
        return False
    opcion_int = int(_selector)
    return opcion_int

def buscarProducto(tupla_productoLista):
    """Buscar productos segun nombre o indice"""
    print("3. Buscar producto: Busque segun el producto o su posicion en la lista.")
    while True:
        opcion_int = validarIngreso()   
        centinelaInfo= (f"\nLa lista actual es: {tupla_productoLista}") 
        if opcion_int is False: 
            break    
        match opcion_int:
            case 1:
                busquedaNombre = input("Ingrese nombre de producto: ").strip().title()
                if busquedaNombre == "" or busquedaNombre.isdigit():
                    print("Error de tipeo, vuelva a intentarlo")    
                    continue                                   
                centinela = False 
                for n in range(len(tupla_productoLista)):
                    if tupla_productoLista[n][0] == busquedaNombre: 
                        centinelaInfo = (f"{busquedaNombre} se encuentra en la posicion {n}.\n Tipo: {tupla_productoLista[n][1]}.\n Precio: {tupla_productoLista[n][2]}.") 
                        print(f"Elemento encontrado. {centinelaInfo}")
                        centinela = True 
                        break
                    else:
                        print("Buscando\n...\n..\n.")  
                if not centinela: 
                    print(f"El producto {busquedaNombre} no se encuentra en la lista.")                                                                                                         
            case 2:
                busquedaPosicion = input("Ingrese posicion de producto: ").strip() 
                if not busquedaPosicion.isdigit():
                    print("Error de tipeo, vuelva a intentarlo")    
                    continue                
                busquedaNumPosicion = int(busquedaPosicion) 
                if busquedaNumPosicion < 0 or busquedaNumPosicion >= len(tupla_productoLista): 
                    print("La posicion excede o se encuentra or debajo de la lista, vuelva a intentarlo.")
                    continue              
                for n in range(len(tupla_productoLista)):
                    if n == busquedaNumPosicion: 
                        centinelaInfo = (f"La posicion {n} contiene {tupla_productoLista[n][0]}.\nTipo: {tupla_productoLista[n][1]}.\n Precio: {tupla_productoLista[n][2]}.") 
                        print(f"Elemento encontrado. {centinelaInfo}")
                        break
                    else:
                        print("Buscando\n...\n..\n.")                               
            case _: 
                print(f"La opcion elegida fue {opcion_int}, solo puede ser 1 o 2, vuelva a intentarlo")
                continue
        selector = validarSalirCase()
        if selector == "s":
            continue
        else:
            print("Finalizando vista de productos.\n....\n...\n..\n.")
            break        
    return centinelaInfo 

def eliminarProducto(productoLista):
    """Eliminar productos segun nombre o indice"""
    print("4. Eliminar producto: Elimine segun el producto o su posicion en la lista.")
    while True:
        opcion_int= validarIngreso2()
        centinelaInfo= (f"\nLa lista actual es: {productoLista}")
        if opcion_int is False: 
            break
        match opcion_int:
            case 1:
                centinela = False
                eliminarNombre = input("Ingrese nombre de producto: ").strip().title()                            
                if eliminarNombre == "" or eliminarNombre.isdigit():
                    print("Error de tipeo, vuelva a intentarlo")    
                    continue                     
                for n in range(len(productoLista)):
                    if productoLista[n][0] == eliminarNombre: 
                        productoEliminado = productoLista.pop(n) 
                        centinelaInfo= (f"Se elimino {productoEliminado}. La lista actual es {productoLista}")
                        print(f"Elemento eliminado. {centinelaInfo}")
                        centinela = True 
                        break
                    else:
                        print("Buscando\n...\n..\n.")                       
                if not centinela:
                    print(f"El producto '{eliminarNombre}' no se encuentra en la lista.")            
            case 2:                   
                eliminarIndice = input("Ingrese la posicion del producto: ").strip()
                if not eliminarIndice.isdigit():
                    print("Error de tipeo, vuelva a intentarlo")    
                    continue                    
                eliminarNumIndice = int(eliminarIndice)                
                if eliminarNumIndice < 0 or eliminarNumIndice >= len(productoLista):
                    print("La posicion no coincide con la lista, vuelva a intentarlo.")
                    continue
                centinela=False
                for n in range(len(productoLista)):
                    if n==eliminarNumIndice:
                        productoEliminado= productoLista.pop(n)                         
                        centinelaInfo= (f"Se elimino {productoEliminado}. La lista actual es {productoLista}")
                        print(f"Elemento eliminado. {centinelaInfo}")
                        centinela=True
                        break
                    else:
                        print("Buscando\n...\n..\n.")
                if centinela==False:
                    print(f"El producto {eliminarNumIndice} no se encuentra en la lista.")          
            case _:
                print(f"La opcion elegida fue {opcion_int}, solo puede ser 1 o 2, vuelva a intentarlo.\n")
                continue
        selector = validarSalirCase()
        if selector == "s":
            continue
        else:
            print("Finalizando eliminacion de productos.\n....\n...\n..\n.")
            break        
    return centinelaInfo

def salir():
    """Muestra mensajes de despedida al cerrar el programa"""
    print("5. Salir: ")
    print("\nFinalizando el sistema de gestión de productos.")
    print("¡Gracias por volver. Hasta la próxima!")
    print("Cerrando programa\n...\n..\n.")


"""
def buscarProductos(productoLista, tupla_productoLista):
        print("3. Buscar producto: Busque segun el producto o su posicion en al lista.")
        while True:
            opcion_int= validarIngreso() 
            if opcion_int==1:
                busquedaNombre= input("Ingrese nombre de producto: ").strip().title()
                if (busquedaNombre.isdigit()) or (not busquedaNombre.isalpha()) or busquedaNombre=="":
                    print("Error de tipeo, vuelva a intentarlo")    
                    continue                    
                centinela=False # Centinela de cambio de estado. Permite imprimir una situacion unica
                for n in range(len(tupla_productoLista)):
                    if tupla_productoLista[n][0]==busquedaNombre: # Como es una lista de listas, se busca el indice y su posicion (dato) que coincida con el nombre a buscar (dato)
                        centinelaInfo= (f"{busquedaNombre} se encuentra en la posicion {n}.\n Tipo: {tupla_productoLista[n][1]}.\n Precio: {tupla_productoLista[n][2]}.") # Se imprime cada posicion en la sublista
                        print(f"Elemento encontrado")
                        centinela=True # Se cambia de estado el centinela 
                        break
                    else:
                        print("Buscando\n...\n..\n.")
                if centinela==False: 
                    print(f"El producto {busquedaNombre} no se encuentra en la lista.")                                                                                                         
            elif opcion_int==2:
                busquedaPosicion= input("Ingrese posicion de producto: ") 
                if (not busquedaPosicion.isdigit()) or busquedaNombre=="":
                    print("Error de tipeo, vuelva a intentarlo")    
                    continue 
                busquedaNumPosicion= int(busquedaPosicion) # Se castea a entero para validar el rango ingresado
                if busquedaNumPosicion>len(tupla_productoLista):
                    print("La posicion no coincide a la lista, vuelva a intentarlo.")
                    continue
                for n in range (len(tupla_productoLista)):
                    if n==busquedaNumPosicion: # Se busca solo el indice que coincida con el ingresado. 
                        centinelaInfo= (f"La posicion {n} contine {tupla_productoLista[n][0]}.\nTipo: {tupla_productoLista[n][1]}.\n Precio: {tupla_productoLista[n][2]}.") 
                        print(f"Elemento encontrado")
                        break
                    else:
                        print("Buscando\n...\n..\n.")                    
            else:
                print(f"La opciones elegida fue {opcion_int}, solo puede ser 1 o 2, vuelva a intenarlo")
            selector= validarSalirCase()
            if selector=="s":
                continue
            else:
                print(f"Finalizando vista de productos.\n....\n...\n..\n.")
                break
        return f"{centinelaInfo}" # Siempre devuelve la info guardada antes de salir del bucle While     
"""
def menu(usuario, contraseña, productoLista, tupla_productoLista):
    """Menu general del sistema"""
    while True: # Bucle iterativo hasta BREAK, permite seleccionar opciones con MATCH, vuelve si se selecciona menos de 1 o mas de 5.
        print("\n--- MENU ---")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("")
        opcionMenu= validarSelectorMenu()
        match opcionMenu: #Selector de menu de opciones
            case 1: 
                print("AGREGAR PRODUCTO")
                resultadoAgregar= agregarProductos(productoLista)
                print(f"{resultadoAgregar}")
            case 2:
                print("VER PRODUCTO")
                resultadoVer= verProductos(tupla_productoLista)
                print(f"{resultadoVer}")
            case 3:
                print("BUSCAR PRODUCTO")
                resultadoBuscar= buscarProductos(tupla_productoLista)
                print(f"{resultadoBuscar}")
            case 4:
                print("ELIMINAR PRODUCTOS")
                resultadoEliminar= eliminarProducto(productoLista)
                print(f"{resultadoEliminar}")
            case 5:
                print("SALIR")
                salir()





