import os
import shutil

print("--- Generador de Entregas (Hotline) ---")

# 1. Pedir y limpiar los datos (Insensible a mayúsculas/minúsculas)
tipo_input = input("Tipo de entrega (Tarea, Practica, ProyectoFinal): ").strip().lower()

# Mapeo estricto para cumplir con el formato exacto del profesor y evitar penalizaciones
if tipo_input == "tarea":
    tipo = "Tarea"
elif tipo_input in ["practica", "práctica"]:
    tipo = "Practica"
elif tipo_input in ["proyectofinal", "proyecto final", "proyecto"]:
    tipo = "ProyectoFinal"
else:
    # Por si escribes algo inesperado, al menos pone la primera en mayúscula
    tipo = tipo_input.capitalize()

# Asegurar que el número tenga siempre dos dígitos (ej. "2" -> "02")
numero_input = input("Número de la entrega (ej. 01, 2): ").strip()
numero = numero_input.zfill(2)

# 2. Nombres exactos de carpetas y archivos
nombre_carpeta = f"{tipo}{numero}_Hotline"
readme_nombre = "README_Hotline.pdf"
doc_nombre = f"{tipo}{numero}.pdf"

# 3. Crear la estructura base
print(f"\nCreando estructura estricta para: {nombre_carpeta}...")
os.makedirs(os.path.join(nombre_carpeta, "Doc"), exist_ok=True)

# 4. Preguntas opcionales robustas (acepta s, si, SÍ, yes, etc.)
resp_diagramas = input("¿Necesitas la carpeta Diagramas? (s/n): ").strip().lower()
if resp_diagramas in ['s', 'si', 'sí', 'y', 'yes']:
    os.makedirs(os.path.join(nombre_carpeta, "Diagramas"), exist_ok=True)

resp_sql = input("¿Necesitas la carpeta SQL? (s/n): ").strip().lower()
if resp_sql in ['s', 'si', 'sí', 'y', 'yes']:
    os.makedirs(os.path.join(nombre_carpeta, "SQL"), exist_ok=True)

resp_src = input("¿Necesitas la carpeta SRC (para códigos)? (s/n): ").strip().lower()
if resp_src in ['s', 'si', 'sí', 'y', 'yes']:
    os.makedirs(os.path.join(nombre_carpeta, "SRC"), exist_ok=True)

# 5. Mover los archivos a sus lugares correspondientes
try:
    # Mueve el README a la raíz de la nueva carpeta
    shutil.move(readme_nombre, os.path.join(nombre_carpeta, readme_nombre))
    print(f"{readme_nombre} movido correctamente.")
    
    # Mueve el PDF de la tarea a la carpeta Doc/
    shutil.move(doc_nombre, os.path.join(nombre_carpeta, "Doc", doc_nombre))
    print(f"{doc_nombre} movido a la carpeta Doc/ correctamente.")
except FileNotFoundError as e:
    print(f"\nADVERTENCIA: No se encontró el archivo {e.filename}.")
    print(f"Recuerda que si el archivo no se llama EXACTAMENTE así, habrá penalización de 10 puntos.")

# 6. Crear el archivo .zip final
print("\nComprimiendo la entrega...")
shutil.make_archive(nombre_carpeta, 'zip', root_dir='.', base_dir=nombre_carpeta)

print(f"¡Listo! Tu archivo {nombre_carpeta}.zip está preparado.")