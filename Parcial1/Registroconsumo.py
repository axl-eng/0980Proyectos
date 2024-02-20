import psycopg2
from psycopg2 import sql

# Conexión a la base de datos 
conn = psycopg2.connect(
    dbname='Consumoagua',
    user='postgres',
    password='PAIE8',
    host='localhost',
    port='5432'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Función para registrar el consumo diario de agua
def registrar_consumo_agua(usuario, cantidad_litros):
    query = sql.SQL("""
        INSERT INTO consumo_agua (usuario, cantidad_litros, fecha)
        VALUES (%s, %s, CURRENT_DATE)
    """)
    cursor.execute(query, (usuario, cantidad_litros))
    conn.commit()

# Función para obtener estadísticas de consumo de agua
def obtener_estadisticas_consumo_agua(usuario):
    query = sql.SQL("""
        SELECT AVG(cantidad_litros) as consumo_promedio
        FROM consumo_agua
        WHERE usuario = %s
    """)
    cursor.execute(query, (usuario,))
    estadisticas = cursor.fetchone()
    return estadisticas

# Función para mostrar recordatorio de hidratación
def recordatorio_hidratacion(usuario):
    query = sql.SQL("""
        SELECT cantidad_litros
        FROM consumo_agua
        WHERE usuario = %s AND fecha = CURRENT_DATE
    """)
    cursor.execute(query, (usuario,))
    consumo_hoy = cursor.fetchone()

    if consumo_hoy and consumo_hoy[0] >= 2.0:  # Ajusta el límite según tus necesidades
        print("¡Felicidades! Ya has alcanzado tu objetivo diario de hidratación.")
    else:
        print("Recuerda mantener una buena hidratación. ¡Bebe más agua!")

# Menú principal
while True:
    print("\n--- Registro Diario de Consumo de Agua ---")
    print("1. Registrar Consumo de Agua")
    print("2. Mostrar Estadísticas de Consumo")
    print("3. Recordatorio de Hidratación")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Registrar Consumo de Agua
        usuario = input("Ingrese el nombre de usuario: ")
        cantidad_litros = float(input("Ingrese la cantidad de litros de agua consumidos hoy: "))
        registrar_consumo_agua(usuario, cantidad_litros)
        print("Registro de consumo de agua agregado correctamente.")

    elif opcion == "2":  # Mostrar Estadísticas de Consumo
        usuario = input("Ingrese el nombre de usuario: ")
        estadisticas = obtener_estadisticas_consumo_agua(usuario)
        print("\nEstadísticas de Consumo:")
        print("Consumo promedio:", estadisticas[0], "litros")

    elif opcion == "3":  # Recordatorio de Hidratación
        usuario = input("Ingrese el nombre de usuario: ")
        recordatorio_hidratacion(usuario)

    elif opcion == "4":  # Salir
        break

# Cerrar la conexión al final del programa
cursor.close()
conn.close()

