import funciones as fn

def programa_principal():
    coleccion_peliculas = []

    opcion = 0
    
    while opcion != 6:
        fn.mostrar_menu()
        opcion = fn.solicitar_opcion()
        
        if opcion == 1:
            fn.agregar_pelicula(coleccion_peliculas)
            
        elif opcion == 2:
            pel_buscar = input("Ingrese el nombre de la película a buscar: ")
            posicion = fn.buscar_pelicula(coleccion_peliculas, pel_buscar)
            
            if posicion != -1:
                pelicula_encontrada = coleccion_peliculas[posicion]
                print(f"Película encontrada en la posición/índice: {posicion}")
                print(f"Título: {pelicula_encontrada['titulo']}")
                print(f"Duración: {pelicula_encontrada['duracion']} minutos")
                print(f"Calificación: {pelicula_encontrada['calificaion']}")
                estado_texto = "DISPONIBLE" if pelicula_encontrada['disponible'] else "NO RECOMENDADA"
                print(f"Estado actual: {estado_texto}")
            else:
                print("Pelicula no encontrada.")
                
        elif opcion == 3:
            pel_eliminar = input("Ingrese el nombre de la película a eliminar: ")
            posicion = fn.buscar_pelicula(coleccion_peliculas, pel_eliminar)
            
            if posicion != -1:
                coleccion_peliculas.pop(posicion)
                print("La pelicúla fue eliminada correctamente.")
            else:
                print(f"La película '{pel_eliminar}' no se encuentra registrada.")
                
        elif opcion == 4:
            fn.actualizar_disponibilidad(coleccion_peliculas)
            print("Estados actualizados de manera global en base a las prioridades.")
            
        elif opcion == 5:
            fn.mostrar_peliculas(coleccion_peliculas)
            
    print("“Gracias por usar el sistema. Vuelva Pronto”")

programa_principal()