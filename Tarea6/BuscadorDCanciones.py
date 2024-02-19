import psycopg2

def desplegar_canciones(cursor):
    # Opción 1: Desplegar el listado de canciones
    cursor.execute("SELECT * FROM Lista;")
    canciones = cursor.fetchall()
    for cancion in canciones:
        print(f"{cancion[0]} by {cancion[1]}:\n{cancion[2]}\n")

def buscar_por_artista(cursor):
    # Opción 2: Buscar por artista
    artista = input("Ingrese el nombre del artista: ")
    cursor.execute("SELECT * FROM Lista WHERE artista = %s;", (artista,))
    canciones = cursor.fetchall()
    if canciones:
        for cancion in canciones:
            print(f"{cancion[0]} by {cancion[1]}:\n{cancion[2]}\n")
    else:
        print(f"No se encontraron canciones del artista {artista}.\n")

def buscar_por_cancion(cursor):
    # Opción 3: Buscar por canción
    cancion = input("Ingrese el nombre de la canción: ")
    cursor.execute("SELECT * FROM Lista WHERE cancion = %s;", (cancion,))
    canciones = cursor.fetchall()
    if canciones:
        for cancion in canciones:
            print(f"{cancion[0]} by {cancion[1]}:\n{cancion[2]}\n")
    else:
        print(f"No se encontró la canción {cancion}.\n")

def main():
    # Conectar a la base de datos
    conn = psycopg2.connect(
        host="localhost",
        database="Buscadordcanciones",
        user="postgres",
        password="PAIE8",
    )

    # Crear un cursor para ejecutar consultas SQL
    cursor = conn.cursor()

    while True:
        # Menú principal
        print("Menú:")
        print("1. Desplegar el listado de canciones")
        print("2. Buscar por artista")
        print("3. Buscar por canción")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desplegar_canciones(cursor)
        elif opcion == "2":
            buscar_por_artista(cursor)
        elif opcion == "3":
            buscar_por_cancion(cursor)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

