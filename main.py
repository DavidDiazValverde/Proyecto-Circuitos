import flet as ft
import os
from interfaz import logo
import sys

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        # Si no estamos en un .exe, usamos el directorio actual
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    logo_path = get_resource_path("logo.png")
    assets_dir = os.path.dirname(logo_path)
    ft.app(target=logo, assets_dir=assets_dir)

    #actualmente este documento hace lo mismo que si se corriera interfaz.py, pero es necesario para 
    #poder ejecutar la app desde un archivo .exe