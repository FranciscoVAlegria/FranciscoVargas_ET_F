def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True

def validar_duracion(duracion):
    if duracion > 0:
        return True
    return False

def validar_calificacion(calificacion):
    if 0.0 <= calificacion <= 10:
        return True
    return False


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar películas")
    print("6. Salir")
    print("=====================================")

def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Elija una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Por favor, ingrese un número válido del 1 al 6.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

def agregar_pelicula(lista_peliculas):
    
    titulo = input("Ingrese el nombre de la película: ")
    
    if not validar_titulo(titulo):
        print("Error: La descripción no puede estar vacía ni contener solo espacios.")
        return

    try:
        duracion = int(input("Ingrese la duración de la película (número entero mayor a cero): "))
        if not validar_duracion(duracion):
            print("Error: La duración debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: La duración debe ser un número entero.")
        return

    try:
        calificacion = float(input("Ingrese la calificación de la película (número decimal entre 0.0 y 10): "))
        if not validar_calificacion(calificacion):
            print("Error: La calificación de la película debe ser un número decimal mayor que cero.")
            return
    except ValueError:
        print("Error: La calificación de la película debe ser un número válido.")
        return

    nueva_pelicula = {
        "titulo": titulo,
        "duracion": duracion,
        "calificaion": calificacion,
        "disponible": False
    }
    lista_peliculas.append(nueva_pelicula)
    print("¡Película registrada con éxito!")

def buscar_pelicula(lista_peliculas, titulo_buscar):
    for i in range(len(lista_peliculas)):
        if lista_peliculas[i]["titulo"].strip().lower() == titulo_buscar.strip().lower():
            return i
    return -1

def actualizar_disponibilidad(lista_peliculas):
    for pelicula in lista_peliculas:
        if pelicula["calificaion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False

def mostrar_peliculas(lista_peliculas):
    actualizar_disponibilidad(lista_peliculas)
    
    if len(lista_peliculas) == 0:
        print("No hay películas registradas en el sistema.")
        return

    print("\n=== LISTA DE PELICULAS ===")
    for pelicula in lista_peliculas:
        print(f"Título: {pelicula['titulo']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Calificación: {pelicula['calificaion']}")
        
        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")
        print("********************************************")