import psycopg2
from psycopg2 import sql

# Conexión a la base de datos 
conn = psycopg2.connect(
    dbname='Hlectura',
    user='postgres',
    password='PAIE8',
    host='localhost',
    port='5432'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Función para registrar un libro leído
def registrar_libro_leido(usuario, libro, autor, fecha_lectura, paginas_leidas, meta_paginas, recomendacion):
    query = sql.SQL("""
        INSERT INTO control_lectura (usuario, libro, autor, fecha_lectura, paginas_leidas, meta_paginas, recomendacion)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """)
    cursor.execute(query, (usuario, libro, autor, fecha_lectura, paginas_leidas, meta_paginas, recomendacion))
    conn.commit()

# Función para establecer la meta de lectura
def establecer_meta_lectura(usuario, meta_paginas):
    query = sql.SQL("""
        UPDATE control_lectura
        SET meta_paginas = %s
        WHERE usuario = %s AND meta_paginas IS NULL
    """)
    cursor.execute(query, (meta_paginas, usuario))
    conn.commit()

# Función para recibir recomendaciones
def recibir_recomendaciones(usuario):
    query = sql.SQL("""
        SELECT recomendacion
        FROM control_lectura
        WHERE usuario = %s AND recomendacion IS NOT NULL
    """)
    cursor.execute(query, (usuario,))
    recomendaciones = cursor.fetchall()
    return recomendaciones

# Menú principal
while True:
    print("\n--- Control de Hábitos de Lectura ---")
    print("1. Registrar Libro Leído")
    print("2. Establecer Meta de Lectura")
    print("3. Recibir Recomendaciones")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":  # Registrar Libro Leído
        usuario = input("Ingrese el nombre de usuario: ")
        libro = input("Ingrese el título del libro leído: ")
        autor = input("Ingrese el nombre del autor: ")
        fecha_lectura = input("Ingrese la fecha de lectura (en formato YYYY-MM-DD): ")
        paginas_leidas = int(input("Ingrese el número de páginas leídas: "))
        meta_paginas = None
        recomendacion = None

        # Verificar si hay una meta establecida
        query_meta = sql.SQL("""
            SELECT meta_paginas
            FROM control_lectura
            WHERE usuario = %s AND meta_paginas IS NOT NULL
        """)
        cursor.execute(query_meta, (usuario,))
        meta_result = cursor.fetchone()
        if meta_result:
            meta_paginas = meta_result[0]

        # Verificar si hay una recomendación pendiente
        query_recomendacion = sql.SQL("""
            SELECT recomendacion
            FROM control_lectura
            WHERE usuario = %s AND recomendacion IS NOT NULL
        """)
        cursor.execute(query_recomendacion, (usuario,))
        recomendacion_result = cursor.fetchone()
        if recomendacion_result:
            recomendacion = recomendacion_result[0]

        registrar_libro_leido(usuario, libro, autor, fecha_lectura, paginas_leidas, meta_paginas, recomendacion)
        print("Libro leído registrado correctamente.")

    elif opcion == "2":  # Establecer Meta de Lectura
        usuario = input("Ingrese el nombre de usuario: ")
        meta_paginas = int(input("Ingrese la meta de páginas a leer: "))
        establecer_meta_lectura(usuario, meta_paginas)
        print("Meta de lectura establecida correctamente.")

    elif opcion == "3":  # Recibir Recomendaciones
        usuario = input("Ingrese el nombre de usuario: ")
        recomendaciones = recibir_recomendaciones(usuario)
        print("\nRecomendaciones Pendientes:")
        for recomendacion in recomendaciones:
            print(recomendacion[0])

    elif opcion == "4":  # Salir
        break

# Cerrar la conexión al final del programa
cursor.close()
conn.close()

