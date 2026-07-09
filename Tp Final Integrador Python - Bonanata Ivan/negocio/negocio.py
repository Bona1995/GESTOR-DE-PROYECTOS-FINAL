import time
from colorama import Fore, Back, init
init(autoreset=True)

from datos.datos import (crearTablaYDatosIniciales, agregarProductosDB, verProductoNombreDB, verProductoCategoriaDB, verProductoRangoPreciosDB, verProductoCantidadDB, verProductosDB)

productoLista=[]
productoInicial1= {
        "nombre": "Notebook Gadget X",
        "descripcion": "Laptop 15 pulgadas, 16GB RAM, 512GB SSD",
        "cantidad": 10,
        "precio": 850000.00,
        "categoria": "Electrónica"
    }
productoInicial2=  {
        "nombre": "Teclado Mecánico RGB",
        "descripcion": "Teclado switch red con cable removible",
        "cantidad": 25,
        "precio": 45000.50,
        "categoria": "Accesorios"
    }
productoLista.extend([productoInicial1, productoInicial2])

def iniciarDatos():
    centinela= crearTablaYDatosIniciales(productoInicial1,productoInicial2)
    return centinela

def agregarProducto(productoAgregar):
    productoLista.append(productoAgregar) 
    centinela= agregarProductosBdd(productoAgregar) 
    return centinela

def verProducto():
    centinela= verProductosDB()
    return centinela

def obtenerNombre(nombreBuscar):
    """Actua como puente intermedio entre presentacion y datos"""
    centinela= verProductoNombreDB(nombreBuscar)
    return centinela

def obtenerCategoria(categoriaBuscar):
    """Actua como puente intermedio entre presentacion y datos"""
    centinela= verProductoCategoriaDB(categoriaBuscar)
    return centinela

def obtenerRango(rangoBuscarMin, rangoBuscarMax):
    """Actua como puente intermedio entre presentacion y datos"""
    centinela= verProductoRangoPreciosDB(rangoBuscarMin, rangoBuscarMax)
    return centinela

def obtenerCantidad(cantidadBuscar):
    """Actua como puente intermedio entre presentacion y datos"""
    centinela= verProductoCantidadDB(cantidadBuscar)
    return centinela





