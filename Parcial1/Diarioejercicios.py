import psycopg2
from psycopg2 import sql

# Conexión a la base de datos 
conn = psycopg2.connect(
    dbname='Diarioejercicios',
    user='postgres',
    password='PAIE8',
    host='localhost',
    port='5432'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Función para insertar un nuevo ejercicio en el diario
def insertar_ejercicio(usuario, categoria, descripcion, duracion_minutos, fecha,
                        repeticiones, peso_kg, metas_alcanzadas):
    query = sql.SQL("""
        INSERT INTO diarioejercicios (usuario, categoria, descripcion, duracion_minutos,
                                      fecha, repeticiones, peso_kg, metas_alcanzadas)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """)
    cursor.execute(query, (usuario, categoria, descripcion, duracion_minutos,
                           fecha, repeticiones, peso_kg, metas_alcanzadas))
    conn.commit()

# Función para obtener el historial de ejercicios
def obtener_historial(usuario):
    query = sql.SQL("""
        SELECT * FROM diarioejercicios
        WHERE usuario = %s
        ORDER BY fecha DESC
    """)
    cursor.execute(query, (usuario,))
    historial = cursor.fetchall()
    return historial

# Función para mostrar estadísticas
def mostrar_estadisticas(usuario):
    query = sql.SQL("""
        SELECT AVG(duracion_minutos) as duracion_promedio, 
               AVG(repeticiones) as repeticiones_promedio, 
               AVG(peso_kg) as peso_promedio
        FROM diarioejercicios
        WHERE usuario = %s
    """)
    cursor.execute(query, (usuario,))
    estadisticas = cursor.fetchone()
    return estadisticas

# Función para eliminar datos
def eliminar_datos(usuario):
    fecha = input("Ingrese la fecha del ejercicio a borrar (en formato YYYY-MM-DD): ")
    query = sql.SQL("""
        DELETE FROM diarioejercicios
        WHERE usuario = %s AND fecha = %s
    """)
    cursor.execute(query, (usuario, fecha))
    conn.commit()
    print("Datos eliminados correctamente.")

# Menú principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Ingresar Datos")
    print("2. Visualizar Estadísticas")
    print("3. Historial de Datos")
    print("4. Borrar Datos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Ingresar Datos
        usuario = input("Ingrese el nombre de usuario: ")
        categoria = input("Ingrese la categoría del ejercicio: ")
        descripcion = input("Ingrese la descripción del ejercicio: ")
        duracion_minutos = int(input("Ingrese la duración en minutos: "))
        fecha = input("Ingrese la fecha (en formato YYYY-MM-DD): ")
        repeticiones = int(input("Ingrese el número de repeticiones: "))
        peso_kg = float(input("Ingrese el peso en kg: "))
        metas_alcanzadas = input("¿Se alcanzaron las metas? (Sí/No): ").lower() == "si"

        insertar_ejercicio(usuario, categoria, descripcion, duracion_minutos,
                           fecha, repeticiones, peso_kg, metas_alcanzadas)
        print("Datos ingresados correctamente.")

    elif opcion == "2":  # Visualizar Estadísticas
        usuario = input("Ingrese el nombre de usuario: ")
        estadisticas = mostrar_estadisticas(usuario)
        print("\nEstadísticas:")
        print("Duración promedio:", estadisticas[0], "minutos")
        print("Repeticiones promedio:", estadisticas[1])
        print("Peso promedio:", estadisticas[2], "kg")

    elif opcion == "3":  # Historial de Datos
        usuario = input("Ingrese el nombre de usuario: ")
        historial = obtener_historial(usuario)
        print("\nHistorial de ejercicios:")
        for ejercicio in historial:
            print(ejercicio)

    elif opcion == "4":  # Borrar Datos
        usuario = input("Ingrese el nombre de usuario: ")
        eliminar_datos(usuario)

    elif opcion == "5":  # Salir
        break

# Cerrar la conexión al final del programa
cursor.close()
conn.close()

