import json


def cargar_inventario(archivo):
    """Carga el inventario desde un archivo JSON y lo almacena en un diccionario."""
    try:
        with open(archivo, 'r') as file:
            inventario = json.load(file)
        print("Inventario cargado exitosamente.")
        return inventario
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado. Se creará uno nuevo.")
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return {}






def guardar_inventario(archivo, inventario):
    """Guarda el inventario en un archivo JSON."""
    try:
        with open(archivo, 'w') as file:
            json.dump(inventario, file, indent=4)
        print("Inventario guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar el inventario: {e}")


def agregar_producto(archivo):
    """Permite al usuario agregar un producto al inventario y lo guarda en el archivo JSON."""
    inventario = cargar_inventario(archivo)

    # Pedir al usuario los datos del producto
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    precio = float(input(f"Ingrese el precio de {nombre}: "))

    # Verificar si el producto ya existe
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe en el inventario. Actualizando cantidad y precio.")
        inventario[nombre]['cantidad'] += cantidad
        inventario[nombre]['precio'] = precio  # Actualiza el precio al último ingresado
    else:
        # Si no existe, agregar el nuevo producto
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}

    # Guardar el inventario actualizado
    guardar_inventario(archivo, inventario)


def actualizar_producto(archivo):
    """Permite al usuario actualizar la cantidad y/o precio de un producto existente."""
    inventario = cargar_inventario(archivo)

    # Mostrar los productos existentes
    if not inventario:
        print("El inventario está vacío.")
        return

    print("Productos en el inventario:")
    for producto in inventario:
        print(f"- {producto} (Cantidad: {inventario[producto]['cantidad']}, Precio: {inventario[producto]['precio']})")

    # Pedir al usuario que seleccione un producto para actualizar
    nombre = input("Ingrese el nombre del producto que desea actualizar: ")

    if nombre in inventario:
        # Preguntar al usuario qué desea actualizar
        actualizar_cantidad = input(f"¿Desea actualizar la cantidad de {nombre}? (s/n): ").lower()
        if actualizar_cantidad == 's':
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {nombre}: "))
            inventario[nombre]['cantidad'] = nueva_cantidad

        actualizar_precio = input(f"¿Desea actualizar el precio de {nombre}? (s/n): ").lower()
        if actualizar_precio == 's':
            nuevo_precio = float(input(f"Ingrese el nuevo precio de {nombre}: "))
            inventario[nombre]['precio'] = nuevo_precio

        # Guardar el inventario actualizado
        guardar_inventario(archivo, inventario)
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


def eliminar_producto(archivo):
    """Permite al usuario eliminar un producto del inventario."""
    inventario = cargar_inventario(archivo)

    # Mostrar los productos existentes
    if not inventario:
        print("El inventario está vacío.")
        return

    print("Productos en el inventario:")
    for producto in inventario:
        print(f"- {producto} (Cantidad: {inventario[producto]['cantidad']}, Precio: {inventario[producto]['precio']})")

    # Pedir al usuario que seleccione un producto para eliminar
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")

    if nombre in inventario:
        confirmar = input(f"¿Está seguro de que desea eliminar '{nombre}' del inventario? (s/n): ").lower()
        if confirmar == 's':
            del inventario[nombre]  # Eliminar el producto del inventario
            guardar_inventario(archivo, inventario)
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")


def mostrar_inventario(archivo):
    """Muestra en pantalla todos los productos disponibles en el inventario."""
    inventario = cargar_inventario(archivo)

    if not inventario:
        print("El inventario está vacío.")
        return

    print("Inventario disponible:")
    print("-" * 40)
    for producto, detalles in inventario.items():
        print(f"Producto: {producto}")
        print(f"  Cantidad: {detalles['cantidad']}")
        print(f"  Precio: {detalles['precio']}")
        print("-" * 40)


def menu():
    """Muestra el menú de opciones y ejecuta la opción seleccionada."""
    archivo_inventario = 'inventory.json'
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_producto(archivo_inventario)
        elif opcion == '2':
            actualizar_producto(archivo_inventario)
        elif opcion == '3':
            eliminar_producto(archivo_inventario)
        elif opcion == '4':
            mostrar_inventario(archivo_inventario)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
menu()