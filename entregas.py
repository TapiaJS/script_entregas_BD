"""
Script de Automatización de Entregas - Fundamentos de Bases de Datos
Equipo: Hotline
"""

import os
import shutil

print("--- Generador de Entregas (Hotline) ---")

# Bucle principal para validación de datos. 
# Permite al usuario revisar y corregir la configuración antes de realizar cambios en el disco.
while True:
    
    # 1. Captura y normalización de datos principales
    # Se eliminan espacios en blanco laterales y se convierte a minúsculas para 
    # hacer la entrada insensible a mayúsculas/minúsculas.
    tipo_input = input("Tipo de entrega (Tarea, Practica, ProyectoFinal): ").strip().lower()

    # Mapeo estricto para forzar la capitalización correcta exigida por los lineamientos.
    if tipo_input == "tarea":
        tipo = "Tarea"
    elif tipo_input in ["practica", "práctica"]:
        tipo = "Práctica"
    elif tipo_input in ["proyectofinal", "proyecto final", "proyecto"]:
        tipo = "ProyectoFinal"
    else:
        print("Vuelve a intentarlo.")
        continue 

    # Captura del número de entrega.
    numero_input = input("Numero de la entrega (ej. 01, 2): ").strip()
    # zfill(2) asegura que el número tenga siempre dos dígitos, agregando un cero a la izquierda si es necesario.
    numero = numero_input.zfill(2)

    # 2. Definición de nombres exactos de carpetas y archivos base.
    nombre_carpeta = f"{tipo}{numero}_Hotline"
    readme_nombre = "README_Hotline.pdf"
    doc_nombre = f"{tipo}{numero}.pdf"

    # 3. Captura de requerimientos de subcarpetas opcionales.
    resp_diagramas = input("¿Necesitas la carpeta Diagramas? (s/n): ").strip().lower()
    resp_sql = input("¿Necesitas la carpeta SQL? (s/n): ").strip().lower()
    resp_src = input("¿Necesitas la carpeta SRC (para codigos)? (s/n): ").strip().lower()

    # Evaluación de las respuestas. Se aceptan múltiples variaciones de "sí".
    crear_diagramas = resp_diagramas in ['s', 'si', 'y', 'yes']
    crear_sql = resp_sql in ['s', 'si', 'y', 'yes']
    crear_src = resp_src in ['s', 'si', 'y', 'yes']

    # 4. Resumen y confirmación de la estructura a generar.
    print("\n--- Resumen de la entrega ---")
    print(f"Carpeta principal: {nombre_carpeta}")
    print(f"Archivos esperados: {readme_nombre}, {doc_nombre}")
    print("Subcarpetas a crear:")
    print(" - Doc (Obligatoria)") # La carpeta Doc siempre es obligatoria.
    
    if crear_diagramas:
        print(" - Diagramas")
    if crear_sql:
        print(" - SQL")
    if crear_src:
        print(" - SRC")

    # Confirmación final del usuario.
    confirmacion = input("\n¿Son correctos estos datos? (s/n para corregir y volver a empezar): ").strip().lower()
    if confirmacion in ['s', 'si', 'y', 'yes']:
        break  # Los datos son correctos, se rompe el bucle para proceder a la creación.
    else:
        print("\nReiniciando captura de datos...\n")

# 5. Creación física de la estructura de directorios en el sistema operativo.
print(f"\nCreando estructura estricta para: {nombre_carpeta}...")

# os.path.join asegura la compatibilidad de las rutas independientemente del sistema operativo.
# exist_ok=True previene que el programa falle si el directorio ya existe.
os.makedirs(os.path.join(nombre_carpeta, "Docs"), exist_ok=True)

if crear_diagramas:
    os.makedirs(os.path.join(nombre_carpeta, "Diagramas"), exist_ok=True)
if crear_sql:
    os.makedirs(os.path.join(nombre_carpeta, "SQL"), exist_ok=True)
if crear_src:
    os.makedirs(os.path.join(nombre_carpeta, "SRC"), exist_ok=True)

# 6. Reubicación de los archivos requeridos hacia la nueva estructura.
try:
    # Mover el README_Hotline.pdf a la raíz de la carpeta principal.
    shutil.move(readme_nombre, os.path.join(nombre_carpeta, readme_nombre))
    print(f"[OK] {readme_nombre} movido correctamente.")
    
    # Mover el PDF principal (ej. Practica02.pdf) dentro de la subcarpeta Doc/.
    shutil.move(doc_nombre, os.path.join(nombre_carpeta, "Doc", doc_nombre))
    print(f"[OK] {doc_nombre} movido a la carpeta Doc/ correctamente.")
except FileNotFoundError as e:
    # Manejo de excepción si los archivos no se encuentran en el directorio actual 
    # o si sus nombres no coinciden exactamente.
    print(f"\n[ERROR] No se encontro el archivo {e.filename}.")
    print("Recuerda que si el archivo no se llama EXACTAMENTE asi, habra penalizacion de 10 puntos.")

# 7. Empaquetado final de la entrega.
print("\nComprimiendo la entrega...")
# shutil.make_archive genera el archivo .zip comprimiendo todo el contenido de 'nombre_carpeta'.
shutil.make_archive(nombre_carpeta, 'zip', root_dir='.', base_dir=nombre_carpeta)

print(f"[EXITO] Tu archivo {nombre_carpeta}.zip esta preparado y listo para subirse a Classroom.")