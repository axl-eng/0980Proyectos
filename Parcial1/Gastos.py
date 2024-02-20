import psycopg2
import datetime
usuario_global = None  
presupuesto_usuario = None
meta_gasto = None
def conectar():
    conn = psycopg2.connect(
    dbname='Gastosal',
    user='postgres',
    password='PAIE8',
    host='localhost',
    port='5432')
    return conn

def menu_principal():
    conn = conectar()
    while True:
        print("1. Ingreso de usuario")
        print("2. Ejecución de programa")
        print("3. Historial de datos")
        print("4. Borrado de datos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingreso_usuario()
        elif opcion == "2":
            ejecucion_programa()
        elif opcion == "3":
            historial_datos(conn=conectar())
        elif opcion == "4":
            borrado_datos(conn=conectar())
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def ingreso_usuario():
    global usuario_global
    global presupuesto_usuario
    usuario_global = input("Ingrese su nombre de usuario: ")
    presupuesto_usuario = float(input("Ingrese su presupuesto: "))
    print(f"Bienvenido, {usuario_global}")

def ejecucion_programa():
    while True:
        print("1. Registrar gasto")
        print("2. Analizar hábitos alimenticios")
        print("3. Sugerencias para ajustar el presupuesto")
        print("4. Establecer metas nutricionales")
        print("5. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            regis_gasto(conn=conectar())
        elif opcion == "2":
            analizar_habitos(conn=conectar())
        elif opcion == "3":
            sugerencias_presupuesto()
        elif opcion == "4":
            establecer_metas()
        elif opcion == "5":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Registrar_gasto, analizar_habitos, sugerencias_presupuesto y establecer_metas
def regis_gasto(conn):
    if usuario_global is None:
        print("Por favor, ingrese primero al sistema.")
        return ingreso_usuario()

    cur = conn.cursor()
    alimento = input("Ingrese el alimento: ")
    costo = float(input("Ingrese el costo: "))
    fecha = datetime.datetime.now()  # Usamos la fecha actual

    cur.execute("INSERT INTO gastos (nombre, alimento, costo, fecha) VALUES (%s, %s, %s, %s)", (usuario_global, alimento, costo, fecha))
    conn.commit()
    print("Gasto registrado exitosamente.")


def analizar_habitos(conn):
    if usuario_global is None:
        print("Por favor, ingrese primero al sistema.")
        return ingreso_usuario()

    cur = conn.cursor()
    cur.execute("SELECT alimento, SUM(costo) as total_gasto FROM gastos WHERE nombre = %s GROUP BY alimento ORDER BY total_gasto DESC", (usuario_global,))
    gastos = cur.fetchall()

    # Identificar los alimentos en los que el usuario gasta más dinero
    print("Los alimentos en los que gastas más dinero son:")
    for gasto in gastos:
        print(f"{gasto[0]}: {gasto[1]}")


def sugerencias_presupuesto(conn):
   
        print("Parece que estás gastando más de lo que te gustaría en alimentos. Aquí tienes algunas sugerencias para reducir tus gastos:")
        print("- Planifica tus comidas con antelación y haz una lista de compras.")
        print("- Evita las comidas para llevar y cocina en casa.")
        print("- Compra alimentos en temporada o en oferta.")


  # Variable global para la meta de gasto del usuario

def establecer_metas():
    global meta_gasto
    meta_gasto = float(input("Ingrese su meta de gasto: "))
    print(f"Tu meta de gasto ha sido establecida en: {meta_gasto}")


def historial_datos(conn):
    if usuario_global is None:
        print("Por favor, ingrese primero al sistema.")
        return ingreso_usuario()

    cur = conn.cursor()
    cur.execute("SELECT alimento, costo, fecha FROM gastos WHERE nombre = %s ORDER BY fecha DESC", (usuario_global,))
    gastos = cur.fetchall()

    print("Aquí está tu historial de gastos:")
    for gasto in gastos:
        print(f"Alimento: {gasto[0]}, Costo: {gasto[1]}, Fecha: {gasto[2]}")


def borrado_datos(conn):
    if usuario_global is None:
        print("Por favor, ingrese primero al sistema.")
        return ingreso_usuario()

    cur = conn.cursor()
    alimento = input("Ingrese el alimento del gasto que desea eliminar: ")
    # Eliminar el gasto
    cur.execute("DELETE FROM gastos WHERE nombre = %s AND alimento = %s ", (usuario_global, alimento))
    conn.commit()

    print("Gasto eliminado exitosamente.")


# Llamar a la función del menú principal para iniciar el programa
menu_principal()
