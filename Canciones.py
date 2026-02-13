# ============================================
# REPRODUCTOR DE CANCIONES - Algoritmos 4
# Estructura principal: LISTAS
# ============================================

# --- LISTAS PRINCIPALES ---
# Cada cancion se guarda como una lista: [nombre, artista, minutos, segundos]
# Todas las canciones se guardan en una lista de listas
canciones = []

# Esta variable guarda la posicion (indice) de la cancion actual
cancion_actual = -1  # -1 significa que no hay ninguna cancion cargada


# --- FUNCIONES ---

def agregar_cancion():
    """Agrega una nueva cancion a la lista"""
    nombre = input("  Nombre de la cancion: ")
    artista = input("  Artista: ")
    minutos = int(input("  Duracion - Minutos: "))
    segundos = int(input("  Duracion - Segundos: "))

    # Creamos una lista con los datos de la cancion
    cancion = [nombre, artista, minutos, segundos]

    # La agregamos al final de la lista de canciones
    canciones.append(cancion)

    print(f"\n  Cancion '{nombre}' agregada exitosamente!")
    print(f"  Total de canciones en la lista: {len(canciones)}")


def mostrar_cancion_actual():
    """Muestra la cancion que esta sonando ahora"""
    global cancion_actual

    # Si la lista esta vacia, no hay nada que mostrar
    if len(canciones) == 0:
        print("\n  No hay canciones en la lista. Agrega una primero!")
        return

    # Si no se ha seleccionado ninguna cancion, empezamos con la primera
    if cancion_actual == -1:
        cancion_actual = 0

    # Sacamos los datos de la lista usando el indice
    cancion = canciones[cancion_actual]
    nombre = cancion[0]
    artista = cancion[1]
    minutos = cancion[2]
    segundos = cancion[3]

    print("\n  ♪ REPRODUCIENDO AHORA ♪")
    print(f"  Cancion : {nombre}")
    print(f"  Artista : {artista}")
    print(f"  Duracion: {minutos} min {segundos} seg")
    print(f"  Posicion: {cancion_actual + 1} de {len(canciones)}")


def siguiente_cancion():
    """Pasa a la siguiente cancion en la lista"""
    global cancion_actual

    if len(canciones) == 0:
        print("\n  No hay canciones en la lista.")
        return

    # Si estamos en la ultima cancion, volvemos a la primera
    if cancion_actual >= len(canciones) - 1:
        cancion_actual = 0
        print("\n  Volviendo al inicio de la lista...")
    else:
        cancion_actual = cancion_actual + 1

    mostrar_cancion_actual()


def cancion_anterior():
    """Vuelve a la cancion anterior en la lista"""
    global cancion_actual

    if len(canciones) == 0:
        print("\n  No hay canciones en la lista.")
        return

    # Si estamos en la primera cancion, vamos a la ultima
    if cancion_actual <= 0:
        cancion_actual = len(canciones) - 1
        print("\n  Saltando al final de la lista...")
    else:
        cancion_actual = cancion_actual - 1

    mostrar_cancion_actual()


def buscar_cancion():
    """Busca una cancion por nombre recorriendo la lista"""
    if len(canciones) == 0:
        print("\n  No hay canciones en la lista.")
        return

    global cancion_actual
    texto = input("  Escribe el nombre a buscar: ").lower()

    # Recorremos la lista con un for para buscar
    encontradas = []  # Lista donde guardamos las que coincidan
    for i in range(len(canciones)):
        nombre = canciones[i][0].lower()
        if texto in nombre:
            encontradas.append(i)  # Guardamos el indice

    if len(encontradas) == 0:
        print("\n  No se encontro ninguna cancion con ese nombre.")
    else:
        print(f"\n  Se encontraron {len(encontradas)} resultado(s):\n")
        for i in range(len(encontradas)):
            indice = encontradas[i]
            c = canciones[indice]
            print(f"  {i + 1}. {c[0]} - {c[1]} ({c[2]} min {c[3]} seg)")

        # Reproducir la primera cancion encontrada
        cancion_actual = encontradas[0]
        print(f"\n  Reproduciendo la primera coincidencia...")
        mostrar_cancion_actual()


def mostrar_lista():
    """Muestra todas las canciones en la lista"""
    if len(canciones) == 0:
        print("\n  La lista esta vacia.")
        return

    print(f"\n  === LISTA DE CANCIONES ({len(canciones)} total) ===\n")
    for i in range(len(canciones)):
        c = canciones[i]
        # Marcamos con >> la cancion que esta sonando
        if i == cancion_actual:
            print(f"  >> {i + 1}. {c[0]} - {c[1]} ({c[2]} min {c[3]} seg) [SONANDO]")
        else:
            print(f"     {i + 1}. {c[0]} - {c[1]} ({c[2]} min {c[3]} seg)")


# --- MENU PRINCIPAL ---

def menu():
    """Muestra el menu y repite hasta que el usuario salga"""
    while True:
        print("\n  =============================")
        print("   REPRODUCTOR DE CANCIONES")
        print("  =============================")
        print("  1. Agregar cancion")
        print("  2. Reproducir (ver cancion actual)")
        print("  3. Siguiente cancion >>")
        print("  4. Cancion anterior <<")
        print("  5. Buscar cancion")
        print("  6. Ver toda la lista")
        print("  7. Salir")
        print("  =============================")

        opcion = input("  Elige una opcion (1-7): ")

        if opcion == "1":
            agregar_cancion()
        elif opcion == "2":
            mostrar_cancion_actual()
        elif opcion == "3":
            siguiente_cancion()
        elif opcion == "4":
            cancion_anterior()
        elif opcion == "5":
            buscar_cancion()
        elif opcion == "6":
            mostrar_lista()
        elif opcion == "7":
            print("\n  Saliendo del reproductor... Hasta luego!")
            break
        else:
            print("\n  Opcion no valida. Intenta de nuevo.")


# --- INICIO DEL PROGRAMA ---
# Esto es lo que se ejecuta cuando corres el archivo
menu()
