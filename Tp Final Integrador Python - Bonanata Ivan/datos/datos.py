from colorama import Fore, Style, init
init(autoreset=True)

import sqlite3


def crearTablaYDatosIniciales(productoInicial1, productoInicial2):
    """ Crea tabla de propductos """
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
   
    try:
        conexion.execute("BEGIN TRANSACTION") 
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    descripcion TEXT NOT NULL,
                    cantidad REAL NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT NOT NULL
                    )
                    """)
        tuplaProductoInicial1= tuple(productoInicial1.values())
        cursor.execute("""
                    INSERT OR IGNORE INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)
                    """, (tuplaProductoInicial1))
        tuplaProductoInicial2= tuple(productoInicial2.values())
        cursor.execute("""
                    INSERT OR IGNORE INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)
                    """, (tuplaProductoInicial2))
        conexion.commit()
        centinelaInfo= (Fore.YELLOW + "Inicializada exitosamente la base de datos")
    except sqlite3.Error as e:
        centinelaInfo= (Fore.RED + f" Error en la base de datos {e}")
        conexion.rollback()
    finally:
        conexion.close()
    return centinelaInfo


def agregarProductosDB(productoAgregar):
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    tupla_productoAgregar= tuple(productoAgregar.values())
    centinelaInfo= None
    
    try:
        cursor.execute("""
                    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)
                    """, (tupla_productoAgregar))  
        conexion.commit() 
        centinelaInfo=  (f"Producto" + Fore.GREEN + f" {productoAgregar.get("Nombre")} añadido exitosamente!. \n")       
    except sqlite3.Error as e:
        print (Fore.RED  + f"Error en la base de datos {e}")
        conexion.rollback()
    finally:
        conexion.close()

    return centinelaInfo


def verProductoNombreDB(nombreBuscar):
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    buscarProducto= nombreBuscar

    try:   
        cursor.execute("""
                    SELECT * FROM productos WHERE nombre = ?""", (buscarProducto,))
        productoNombre= cursor.fetchone()       
        conexion.commit()

    except sqlite3.Error as e:
        conexion.rollback()
        print (Fore.RED + f"Error de busqueda en la base de datos {e}. \n")

    finally:
        conexion.close()
    return productoNombre


def verProductoCategoriaDB(categoriaBuscar):
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    buscarTipo = categoriaBuscar
    centinelaInfo= []

    try:    
        cursor.execute("""
                    SELECT * FROM productos WHERE categoria = ?""", (buscarTipo,))
        productosCategoria = cursor.fetchall()
        centinelaInfo= productosCategoria
        conexion.commit()

    except sqlite3.Error as e:
        conexion.rollback()
        print (Fore.RED + f"Error de búsqueda en la base de datos: {e}\n")

    finally:
        conexion.close()
    return centinelaInfo


def verProductoRangoPreciosDB(rangoBuscarMin, rangoBuscarMax):
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    precio_min= int(rangoBuscarMin)
    precio_max= int(rangoBuscarMax)
    centinelaInfo= []

    try:    
        cursor.execute("""
                    SELECT * FROM productos 
                    WHERE precio BETWEEN ? AND ? 
                    ORDER BY precio ASC""", (precio_min, precio_max))
        productosRango = cursor.fetchall()
        centinelaInfo= productosRango
        conexion.commit()

    except ValueError:
        print(Fore.RED + "Error: Por favor, ingrese numeros validos para los precios.\n")
        conexion.rollback()

    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error de busqueda en la base de datos: {e}\n")

    finally:
        conexion.close()
    
    return centinelaInfo


def verProductoCantidadDB(cantidadBuscar):
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    cantidad_min_min=  int(cantidadBuscar)
    centinelaInfo= []

    try:    
        cursor.execute("""
                    SELECT * FROM productos 
                    WHERE cantidad <= ?
                    ORDER BY cantidad ASC""", (cantidad_min_min,))
        productosStock = cursor.fetchall()
        centinelaInfo= productosStock
        conexion.commit()

    except ValueError:
        print(Fore.RED + "Error: Por favor, ingrese numeros validos para los precios.\n")
        conexion.rollback()

    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error de busqueda en la base de datos: {e}\n")

    finally:
        conexion.close()

    return centinelaInfo


def verProductosDB():
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    
    try:   
        cursor.execute("""
                    SELECT * FROM productos 
                    ORDER BY id ASC""")
        productoVer= cursor.fetchall()
        centinelaInfo= productoVer
        conexion.commit()
    
    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error de busqueda en la base de datos {e}. \n")

    finally:
        conexion.close()

    return centinelaInfo

def eliminarRegistroDB(segunPosicion):
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    posicion= int(segunPosicion)
    centinelaInfo= None

    try:
        cursor.execute("""
                    SELECT nombre FROM productos 
                    WHERE id=?""", (posicion,))
        productoEliminado= cursor.fetchone()
        centinelaInfo= productoEliminado
        print(centinelaInfo)
        if productoEliminado:
            cursor.execute("""
                    DELETE FROM productos
                    WHERE id=?""", (posicion,)) 
        conexion.commit()
    except ValueError:
        print(Fore.RED + "Error: Por favor, datos validos.\n")
        conexion.rollback()
    
    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error de busqueda en la base de datos {e}. \n")
    
    finally:
        conexion.close()
    
    return centinelaInfo


def modificarCantidadProductosDB(modificCantidad, segunPosicion):
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    nuevaCantidad= int(modificCantidad)
    posicion= int(segunPosicion)
    centinelaInfo= None

    try:
        cursor.execute("""
                    SELECT nombre FROM productos 
                    WHERE id=?""", (posicion,))
        productoCantidad= cursor.fetchone()
        centinelaInfo= productoCantidad
        print(centinelaInfo)
        if productoCantidad:
            cursor.execute("""
                        UPDATE productos 
                        SET cantidad= ? WHERE id= ?""", (nuevaCantidad, posicion))
        conexion.commit()
    
    except ValueError:
        print(Fore.RED + "Error: Por favor, datos validos.\n")
        conexion.rollback()
    
    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error de busqueda en la base de datos {e}. \n")
    
    finally:
        conexion.close()
    
    return centinelaInfo


def modificarPrecioProductosDB(nuevoPrecio, segunPosicion):
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    nuevoIntPrecio= int(nuevoPrecio)
    posicion= int(segunPosicion)
    centinelaInfo= None

    try:
        cursor.execute("""
                    SELECT nombre FROM productos 
                    WHERE id=?""", (posicion,))
        productoPrecio= cursor.fetchone()
        centinelaInfo= productoPrecio
        print(centinelaInfo)
        if productoPrecio:               
            cursor.execute("""
                        UPDATE productos 
                        SET precio= ? WHERE id= ?""", (nuevoIntPrecio, posicion))
        conexion.commit()
    
    except ValueError:
        print(Fore.RED + "Error: Por favor, datos validos.\n")
        conexion.rollback()
    
    except sqlite3.Error as e:
        conexion.rollback()
        print(Fore.RED + f"Error de busqueda en la base de datos {e}. \n")
    
    finally:
        conexion.close()
    
    return centinelaInfo

        


