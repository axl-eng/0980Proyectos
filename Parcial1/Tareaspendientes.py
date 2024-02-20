import psycopg2
from psycopg2 import sql

# Conexión a la base de datos 
conn = psycopg2.connect(
    dbname='Gestiontareas',
    user='postgres',
    password='PAIE8',
    host='localhost',
    port='5432'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Función para agregar una nueva tarea
def agregar_tarea(usuario, descripcion, fecha_vencimiento):
    query = sql.SQL("""
        INSERT INTO tareas (usuario, descripcion, fecha_vencimiento, completada)
        VALUES (%s, %s, %s, %s)
    """)
    cursor.execute(query, (usuario, descripcion, fecha_vencimiento, False))
    conn.commit()

# Función para marcar una tarea como completada
def marcar_tarea_completada(usuario, tarea_id):
    query = sql.SQL("""
        UPDATE tareas
        SET completada = TRUE
        WHERE usuario = %s AND id = %s
    """)
    cursor.execute(query, (usuario, tarea_id))
    conn.commit()

# Función para mostrar tareas pendientes
def mostrar_tareas_pendientes(usuario):
    query = sql.SQL("""
        SELECT * FROM tareas
        WHERE usuario = %s AND completada = FALSES
        ORDER BY fecha_vencimiento
    """)
    cursor.execute(query, (usuario,))
    tareas_pendientes = cursor.fetchall()
    return tareas_pendientes

# Menú principal
while True:
    print("\n--- Organizador de Tareas ---")
    print("1. Agregar Nueva Tarea")
    print("2. Marcar Tarea como Completada")
    print("3. Mostrar Tareas Pendientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Agregar Nueva Tarea
        usuario = input("Ingrese el nombre de usuario: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (en formato YYYY-MM-DD, deja en blanco si no hay fecha límite): ")

        if fecha_vencimiento:
            fecha_vencimiento = fecha_vencimiento
        else:
            fecha_vencimiento = None

        agregar_tarea(usuario, descripcion, fecha_vencimiento)
        print("Tarea agregada correctamente.")

    elif opcion == "2":  # Marcar Tarea como Completada
        usuario = input("Ingrese el nombre de usuario: ")
        tarea_id = input("Ingrese el ID de la tarea a marcar como completada: ")
        marcar_tarea_completada(usuario, tarea_id)
        print("Tarea marcada como completada.")

    elif opcion == "3":  # Mostrar Tareas Pendientes
        usuario = input("Ingrese el nombre de usuario: ")
        tareas_pendientes = mostrar_tareas_pendientes(usuario)
        print("\nTareas Pendientes:")
        for tarea in tareas_pendientes:
            print(tarea)

    elif opcion == "4":  # Salir
        break

# Cerrar la conexión al final del programa
cursor.close()
conn.close()

