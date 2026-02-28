import os
import shutil

# 1. Pedir los datos principales
tipo = input("Tipo de entrega (Tarea, Practica, ProyectoFinal): ")
numero = input("Número de la entrega (ej. 01, 02): ")

# 2. Nombres de carpetas y archivos
nombre_carpeta = f"{tipo}{numero}_Hotline"
readme_nombre = "README_Hotline.pdf"
doc_nombre = f"{tipo}{numero}.pdf"

# 3. Crear la estructura base
print(f"\nCreando estructura para: {nombre_carpeta}...")
os.makedirs(f"{nombre_carpeta}/Doc", exist_ok=True)

# 4. Preguntar por carpetas opcionales
if input("¿Necesitas la carpeta Diagramas? (s/n): ").lower() == 's':
    os.makedirs(f"{nombre_carpeta}/Diagramas", exist_ok=True)

if input("¿Necesitas la carpeta SQL? (s/n): ").lower() == 's':
    os.makedirs(f"{nombre_carpeta}/SQL", exist_ok=True)

if input("¿Necesitas la carpeta SRC (para códigos)? (s/n): ").lower() == 's':
    os.makedirs(f"{nombre_carpeta}/SRC", exist_ok=True)

# 5. Mover los archivos a sus lugares correspondientes
try:
    # Mueve el README a la raíz de la nueva carpeta
    shutil.move(readme_nombre, os.path.join(nombre_carpeta, readme_nombre))
    print(f"{readme_nombre} movido correctamente.")
    
    # Mueve el PDF de la tarea a la carpeta Doc/
    shutil.move(doc_nombre, os.path.join(nombre_carpeta, "Doc", doc_nombre))
    print(f"{doc_nombre} movido a la carpeta Doc/ correctamente.")
except FileNotFoundError as e:
    print(f"ERROR: No se encontró el archivo {e.filename}.")
    print("Asegúrate de que los PDFs estén en la misma carpeta que este script y tengan el nombre exacto.")

# 6. Crear el archivo .zip final
print("\nComprimiendo la entrega...")
# Esto crea un archivo .zip que contiene la carpeta principal, tal como lo piden los lineamientos
shutil.make_archive(nombre_carpeta, 'zip', root_dir='.', base_dir=nombre_carpeta)

print(f"¡Listo! Tu archivo {nombre_carpeta}.zip está preparado para subirse a Classroom.")