import psycopg2
from psycopg2 import sql

# Conexión a la base de datos 
conn = psycopg2.connect(
    dbname='Gestorpr',
    user='postgres',
    password='PAIE8',
    host='localhost',
    port='5432'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Función para agregar un nuevo proyecto
def agregar_proyecto(usuario, nombre_proyecto, descripcion_proyecto):
    query = sql.SQL("""
        INSERT INTO proyectos_personales (usuario, nombre_proyecto, descripcion_proyecto, tarea, descripcion_tarea, fecha_creacion, fecha_limite, completada)
        VALUES (%s, %s, %s, NULL, NULL, CURRENT_DATE, NULL, FALSE)
    """)
    cursor.execute(query, (usuario, nombre_proyecto, descripcion_proyecto))
    conn.commit()

# Función para agregar una nueva tarea a un proyecto
def agregar_tarea(usuario, proyecto_id, tarea, descripcion_tarea, fecha_limite):
    query = sql.SQL("""
        INSERT INTO proyectos_personales (usuario, tarea, descripcion_tarea, fecha_creacion, fecha_limite, completada)
        VALUES (%s, %s, %s, CURRENT_DATE, %s, FALSE)
    """)
    cursor.execute(query, (usuario, tarea, descripcion_tarea, fecha_limite))
    conn.commit()

# Función para marcar una tarea como completada
def marcar_tarea_completada(usuario, tarea_id):
    query = sql.SQL("""
        UPDATE proyectos_personales
        SET completada = TRUE
        WHERE usuario = %s AND id = %s
    """)
    cursor.execute(query, (usuario, tarea_id))
    conn.commit()

# Función para mostrar tareas pendientes de un proyecto
def mostrar_tareas_pendientes(usuario, proyecto_id):
    query = sql.SQL("""
        SELECT id, tarea, descripcion_tarea, fecha_limite, completada
        FROM proyectos_personales
        WHERE usuario = %s AND id = %s AND tarea IS NOT NULL AND completada = FALSE
    """)
    cursor.execute(query, (usuario, proyecto_id))
    tareas_pendientes = cursor.fetchall()
    return tareas_pendientes

# Menú principal
while True:
    print("\n--- Planificación y Seguimiento de Proyectos Personales ---")
    print("1. Agregar Proyecto")
    print("2. Agregar Tarea a Proyecto")
    print("3. Marcar Tarea como Completada")
    print("4. Mostrar Tareas Pendientes de un Proyecto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Agregar Proyecto
        usuario = input("Ingrese el nombre de usuario: ")
        nombre_proyecto = input("Ingrese el nombre del proyecto: ")
        descripcion_proyecto = input("Ingrese la descripción del proyecto: ")
        agregar_proyecto(usuario, nombre_proyecto, descripcion_proyecto)
        print("Proyecto agregado correctamente.")

    elif opcion == "2":  # Agregar Tarea a Proyecto
        usuario = input("Ingrese el nombre de usuario: ")
        proyecto_id = input("Ingrese el ID del proyecto al que desea agregar la tarea: ")
        tarea = input("Ingrese el nombre de la tarea: ")
        descripcion_tarea = input("Ingrese la descripción de la tarea: ")
        fecha_limite = input("Ingrese la fecha límite de la tarea (en formato YYYY-MM-DD): ")
        agregar_tarea(usuario, proyecto_id, tarea, descripcion_tarea, fecha_limite)
        print("Tarea agregada al proyecto correctamente.")

    elif opcion == "3":  # Marcar Tarea como Completada
        usuario = input("Ingrese el nombre de usuario: ")
        tarea_id = input("Ingrese el ID de la tarea a marcar como completada: ")
        marcar_tarea_completada(usuario, tarea_id)
        print("Tarea marcada como completada.")

    elif opcion == "4":  # Mostrar Tareas Pendientes de un Proyecto
        usuario = input("Ingrese el nombre de usuario: ")
        proyecto_id = input("Ingrese el ID del proyecto del que desea ver las tareas pendientes: ")
        tareas_pendientes = mostrar_tareas_pendientes(usuario, proyecto_id)
        print("\nTareas Pendientes:")
        for tarea in tareas_pendientes:
            print(f"ID: {tarea[0]}, Tarea: {tarea[1]}, Descripción: {tarea[2]}, Fecha Límite: {tarea[3]}, Completada: {tarea[4]}")

    elif opcion == "5":  # Salir
        break

# Cerrar la conexión al final del programa
cursor.close()
conn.close()

