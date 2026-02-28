import os
import shutil

print("--- Generador de Entregas (Hotline) ---")

while True:
    # 1. Pedir y limpiar los datos
    tipo_input = input("Tipo de entrega (Tarea, Practica, ProyectoFinal): ").strip().lower()

    # Mapeo estricto
    if tipo_input == "tarea":
        tipo = "Tarea"
    elif tipo_input in ["practica", "práctica"]:
        tipo = "Practica"
    elif tipo_input in ["proyectofinal", "proyecto final", "proyecto"]:
        tipo = "ProyectoFinal"
    else:
        print("Vuelve a interarlo.")
        continue 

    numero_input = input("Numero de la entrega (ej. 01, 2): ").strip()
    numero = numero_input.zfill(2)

    # 2. Nombres exactos de carpetas y archivos
    nombre_carpeta = f"{tipo}{numero}_Hotline"
    readme_nombre = "README_Hotline.pdf"
    doc_nombre = f"{tipo}{numero}.pdf"

    # 3. Preguntas opcionales
    resp_diagramas = input("¿Necesitas la carpeta Diagramas? (s/n): ").strip().lower()
    resp_sql = input("¿Necesitas la carpeta SQL? (s/n): ").strip().lower()
    resp_src = input("¿Necesitas la carpeta SRC (para codigos)? (s/n): ").strip().lower()

    crear_diagramas = resp_diagramas in ['s', 'si', 'y', 'yes']
    crear_sql = resp_sql in ['s', 'si', 'y', 'yes']
    crear_src = resp_src in ['s', 'si', 'y', 'yes']

    # 4. Resumen y confirmacion
    print("\n--- Resumen de la entrega ---")
    print(f"Carpeta principal: {nombre_carpeta}")
    print(f"Archivos esperados: {readme_nombre}, {doc_nombre}")
    print("Subcarpetas a crear:")
    print(" - Doc (Obligatoria)")
    
    if crear_diagramas:
        print(" - Diagramas")
    if crear_sql:
        print(" - SQL")
    if crear_src:
        print(" - SRC")

    confirmacion = input("\n¿Son correctos estos datos? (s/n para corregir y volver a empezar): ").strip().lower()
    if confirmacion in ['s', 'si', 'y', 'yes']:
        break  # Rompe el bucle y procede a crear los archivos
    else:
        print("\nReiniciando captura de datos...\n")

# 5. Creacion de la estructura
print(f"\nCreando estructura estricta para: {nombre_carpeta}...")
os.makedirs(os.path.join(nombre_carpeta, "Doc"), exist_ok=True)

if crear_diagramas:
    os.makedirs(os.path.join(nombre_carpeta, "Diagramas"), exist_ok=True)
if crear_sql:
    os.makedirs(os.path.join(nombre_carpeta, "SQL"), exist_ok=True)
if crear_src:
    os.makedirs(os.path.join(nombre_carpeta, "SRC"), exist_ok=True)

# 6. Mover los archivos a sus lugares correspondientes
try:
    shutil.move(readme_nombre, os.path.join(nombre_carpeta, readme_nombre))
    print(f"[OK] {readme_nombre} movido correctamente.")
    
    shutil.move(doc_nombre, os.path.join(nombre_carpeta, "Doc", doc_nombre))
    print(f"[OK] {doc_nombre} movido a la carpeta Doc/ correctamente.")
except FileNotFoundError as e:
    print(f"\n[ERROR] No se encontro el archivo {e.filename}.")
    print("Recuerda que si el archivo no se llama EXACTAMENTE asi, habra penalizacion de 10 puntos.")

# 7. Crear el archivo .zip final
print("\nComprimiendo la entrega...")
shutil.make_archive(nombre_carpeta, 'zip', root_dir='.', base_dir=nombre_carpeta)

print(f"[EXITO] Tu archivo {nombre_carpeta}.zip esta preparado.")