#from funciones.Funciones import (validarSelectorMenu, login, validarSalirCase, menu, verProductos, agregarProducto)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Se especifico que pueda buscar en todas las carpetas

from Funciones.funciones import (validarSelectorMenu, login, validarSalirCase, validarIngreso, validarIngreso2, menu, verProductos, agregarProductos, buscarProducto, eliminarProducto, )

print("\n¡Bienvenido al sistema de gestion del emprendedor.!\nPor favor inicie sesion: ")
usuarioAdmin= "IvanBonanata"
contraseAdmin= "Practicapython2026"
productoLista= [] # Lista vacia para incorporar datos
tupla_productoLista= () # Tupla vacia para visualizar y buscar objetos y evitar modificaciones accidentales

menu(usuarioAdmin, contraseAdmin, productoLista, tupla_productoLista)

