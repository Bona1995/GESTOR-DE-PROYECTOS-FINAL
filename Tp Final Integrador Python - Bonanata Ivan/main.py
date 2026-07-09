from colorama import Fore, Back, init
init(autoreset=True)

from presentacion.presentacion import (menu, inicioDatos, agregarProductos, verProductos, buscarProductosMenu, busquedaNombre, busquedaCategoria, busquedaRango, busquedaCantidad, validarSelectorBusquedaMenu, validarSelectorMenu, validarSalirCase, salir)

print(Back.WHITE + Fore.BLACK+ 
"""-----------------------------------------------------------------------------
¡Bienvenido al sistema de gestion del emprendedor!. Por favor inicie sesion: 
-----------------------------------------------------------------------------""")

menu()

print(Back.WHITE + Fore.BLACK+ 
"""---------------------------------------------------
¡Gracias por usar este programa!. Hasta la proxima: 
----------------------------------------------------""")