import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Se especifico que pueda buscar en todas las carpetas
from Funciones.funciones import (validarSelectorMenu, login, validarSalirCase, menu, verProductos, agregarProducto)
help(validarSelectorMenu)
help(menu)
help(agregarProducto)
help(verProductos)
help(validarSalirCase)
help(login)
