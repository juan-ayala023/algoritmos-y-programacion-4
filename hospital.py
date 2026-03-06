import heapq

cola = []

print("=== Sistema de atencion hospital ===\n")

while True:
    print("\n1. Agregar paciente")
    print("2. Atender siguiente paciente")
    print("3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        prioridad = int(input("Prioridad (1=urgente, 2=normal, 3=leve): "))
        heapq.heappush(cola, (prioridad, nombre))
        print(f"Paciente {nombre} agregado con prioridad {prioridad}")

    elif opcion == "2":
        if cola:
            prioridad, nombre = heapq.heappop(cola)
            print(f"\nSiguiente paciente: {nombre} | Prioridad: {prioridad}")
        else:
            print("No hay pacientes en espera.")

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opcion invalida.")
