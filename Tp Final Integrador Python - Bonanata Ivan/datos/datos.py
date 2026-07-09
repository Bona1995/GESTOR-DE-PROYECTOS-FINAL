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
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    cantidad REAL NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT NOT NULL
                    )
                    """)
        if cursor.fetchone()[0] == 0:
            tuplaProductoInicial1= tuple(productoInicial1.values())
            cursor.execute("""
                        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)
                        """, (tuplaProductoInicial1))
            tuplaProductoInicial2= tuple(productoInicial2.values())
            cursor.execute("""
                        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)
                        """, (tuplaProductoInicial2))
            conexion.commit()
            centinelaInfo= ("Inicializada exitosamente la base de datos")
    except sqlite3.Error as e:
        centinelaInfo= (f"Error en la base de datos {e}")
        conexion.rollback()
    finally:
        conexion.close()
    return centinelaInfo


def agregarProductosDB(productoAgregar):
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    tupla_productoAgregar= tuple(productoAgregar.values())
    
    try:
        cursor.execute("""
                    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)
                    """, (tupla_productoAgregar,))  
        conexion.commit() 
        centinelaInfo=  (f" Producto" + Fore.GREEN + f" {productoAgregar.get("Nombre")} añadido exitosamente.")       
    except sqlite3.Error as e:
        print (f"Error en la base de datos {e}")
        conexion.rollback()
    finally:
        conexion.close()
        return centinelaInfo


def verProductoNombreDB(nombreBuscar):
    import sqlite3 
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    buscarProducto= nombreBuscar

    try:   
        conexion.execute("""BEGIN TRANSACTION""")
        cursor.execute("""
                    SELECT * FROM productos WHERE nombre = ?""", (buscarProducto,))
        productoNombre= cursor.fetchone()       
        conexion.commit()

    except sqlite3.Error as e:
        conexion.rollback()
        print (f"Error de busqueda en la base de datos {e}. \n")

    finally:
        conexion.close()
    return productoNombre


def verProductoCategoriaDB(categoriaBuscar):
    import sqlite3 
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    buscarTipo = categoriaBuscar
    centinelaInfo= []

    try:    
        conexion.execute("""BEGIN TRANSACTION""")
        cursor.execute("""
                    SELECT * FROM productos WHERE categoria = ?""", (buscarTipo,))
        productosCategoria = cursor.fetchall()
        centinelaInfo= productosCategoria
        conexion.commit()

    except sqlite3.Error as e:
        conexion.rollback()
        print (f"Error de búsqueda en la base de datos: {e}\n")

    finally:
        conexion.close()
    return centinelaInfo


def verProductoRangoPreciosDB(rangoBuscarMin, rangoBuscarMax):
    import sqlite3 
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    rangoBuscarMin= int(precio_max)
    rangoBuscarMax= int(precio_max)
    centinelaInfo= []

    try:    
        conexion.execute("""BEGIN TRANSACTION""")
        cursor.execute("""
                    SELECT * FROM productos 
                    WHERE precio BETWEEN ? AND ? 
                    ORDER BY precio ASC""", (precio_min, precio_max))
        productosRango = cursor.fetchall()
        centinelaInfo= productosRango
        conexion.commit()

    except ValueError:
        print("Error: Por favor, ingrese numeros validos para los precios.\n")
        conexion.rollback()

    except sqlite3.Error as e:
        conexion.rollback()
        print(f"Error de busqueda en la base de datos: {e}\n")

    finally:
        conexion.close()
    
    return centinelaInfo


def verProductoCantidadDB(cantidadBuscar):
    import sqlite3 
    conexion = sqlite3.connect("Inventario.db")
    cursor = conexion.cursor()
    cantidad_min_min=  float(cantidadBuscar)
    centinelaInfo= []

    try:    
        conexion.execute("""BEGIN TRANSACTION""")
        cursor.execute("""
                    SELECT * FROM productos 
                    WHERE cantidad <= ?
                    ORDER BY cantidad ASC""", (cantidad_min_min,))
        productosStock = cursor.fetchall()
        centinelaInfo= productosStock
        conexion.commit()

    except ValueError:
        print("Error: Por favor, ingrese numeros validos para los precios.\n")
        conexion.rollback()

    except sqlite3.Error as e:
        conexion.rollback()
        print(f"Error de busqueda en la base de datos: {e}\n")

    finally:
        conexion.close()

    return centinelaInfo


def verProductosDB():
    import sqlite3 
    conexion= sqlite3.connect("Inventario.db")
    cursor= conexion.cursor()
    
    try:   
        cursor.execute("""
                    SELECT * FROM productos ORDER BY id ASC""")
        productoVer= cursor.fetchall()
        centinelaInfo= productoVer
    
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"Error de busqueda en la base de datos {e}. \n")

    finally:
        conexion.close()
        
    return centinelaInfo
