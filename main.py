import flet as ft
import os
from interfaz import logo

if __name__ == "__main__":
    # Directorio donde se encuentra este archivo (para los assets)
    carpeta_recursos = os.path.dirname(__file__)
    
    # Ejecutamos la aplicación con la función logo como punto de entrada
    ft.app(target=logo, assets_dir=carpeta_recursos)

    #actualmente este documento hace lo mismo que si se corriera interfaz.py, pero es necesario para 
    #poder ejecutar la app desde un archivo .exe