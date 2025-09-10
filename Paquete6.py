# PAQUETE OS
# El paquete os proporciona una interfaz portátil e independiente de la plataforma para interactuar con el sistema operativo 
# y realizar tareas como manipular archivos y directorios, gestionar procesos y acceder a variables de entorno.

# EJEMPLO
import os

archivos = os.listdir("C:/Users/Batre/Documents/INGENIERIA EN SISTEMAS/CICLO 4")
print("Archivos en la carpeta:")
for archivo in archivos:
    print(f"- {archivo}")

# Lo que me muestra a mi como resultado
"""
Archivos en la carpeta:
- Administración de Bases de Datos II
- Estadística Computacional
- Estructura y Diseño de Circuitos Digitales
- Inglés Básico
- Programación Computacional III
"""