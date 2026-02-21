import sys
import App.logic as logic
from tabulate import tabulate
from DataStructures.List import array_list as lt

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    filename = "computer_prices_large.csv"
    total_computers, min_comp, max_comp, load_time, first_five_comp, last_five_comp = logic.load_data(control, filename)
    print("Total computadores cargados: ", total_computers)
    print("Tiempo de carga (ms):", round(load_time, 3))

    print("\nComputador con MENOR precio:")
    min_list = [min_comp]
    print(tabulate(format_comp_for_table(min_list), headers = ["Modelo", "Marca", "Año", "CPU", "GPU", "Precio"], tablefmt="pretty"))

    print("\nComputador con MAYOR precio:")
    max_list = [max_comp]
    print(tabulate(format_comp_for_table(max_list), headers = ["Modelo", "Marca", "Año", "CPU", "GPU", "Precio"], tablefmt="pretty"))

    print("\nPrimeros 5 computadores cargados:")
    print(tabulate(format_comp_for_table(first_five_comp), headers = ["Modelo", "Marca", "Año", "CPU", "GPU", "Precio"], tablefmt="pretty"))
    print("\nÚltimos 5 computadores cargados:")
    print(tabulate(format_comp_for_table(last_five_comp), headers = ["Modelo", "Marca", "Año", "CPU", "GPU", "Precio"], tablefmt="pretty"))

def format_comp_for_table(computers):
    data_comp = []
    for comp in computers:
        fila = [comp["model"],comp["brand"],comp["release_year"],comp["cpu_brand"],comp["gpu_brand"],comp["price"]]
        data_comp.append(fila)
    return data_comp
        
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    size = lt.size(control["computers"])
    if id < 0 or id >= size:
        raise Exception("IndexError: id fuera del rango de lista de computadores")
    
    comp = lt.get_element(control["computers"], id)
    print("Modelo:", comp["model"])
    print("Marca:", comp["brand"])
    print("Año:", comp["release_year"])
    print("CPU:", comp["cpu_model"])
    print("GPU:", comp["gpu_model"])
    print("Precio:", comp["price"])

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    marca = input(" Ingrese el nombre de la marca\n(EJEMPLO: Samsung): ").strip()

    (tiempo, total_comp, prom_price, min_price, max_price,
     prom_ram, min_ram, max_ram, prom_vram, min_vram, max_vram,
     prom_num_nucleos, min_nucleos, max_nucleos,
     prom_anio_release, min_release, max_release,
     model_max_comp, model_min_comp, general_info) = logic.req_1(control, marca)

    print("\n" + "=" * 65)
    print(" Requerimiento 1: Promedio de características por marca")
    print("=" * 65)
    print(f" Tiempo de ejecución: {tiempo:.3f} ms")

    if total_comp == 0:
        print(f" No se encontraron computadores de la marca '{marca}'.")
        return

    print(f" Total de computadores de la marca {marca}: {total_comp}")
    print("\n Estadísticas de precio")
    print(f"  Promedio: ${prom_price:.2f}")
    print(f"  Mínimo:   ${min_price:.2f}")
    print(f"  Máximo:   ${max_price:.2f}")

    print("\n Estadísticas de RAM (GB)")
    print(f"  Promedio: {prom_ram:.2f}")
    print(f"  Mínimo:   {min_ram:.2f}")
    print(f"  Máximo:   {max_ram:.2f}")

    print("\n Estadísticas de VRAM (GB)")
    print(f"  Promedio: {prom_vram:.2f}")
    print(f"  Mínimo:   {min_vram:.2f}")
    print(f"  Máximo:   {max_vram:.2f}")

    print("\n Estadísticas de núcleos de CPU")
    print(f"  Promedio: {prom_num_nucleos:.2f}")
    print(f"  Mínimo:   {min_nucleos:.2f}")
    print(f"  Máximo:   {max_nucleos:.2f}")

    print("\n Estadísticas de año de lanzamiento")
    print(f"  Promedio: {prom_anio_release:.2f}")
    print(f"  Mínimo:   {min_release}")
    print(f"  Máximo:   {max_release}")

    print("\n Modelos destacados de la marca")
    print(f"  Mayor precio: {model_max_comp} (${max_price:.2f})")
    print(f"  Menor precio: {model_min_comp} (${min_price:.2f})")
    
    print("\n" + "=" * 65)
    print(f" Informe general de la marca {marca}: ")
    print("=" * 65)
    tabla_precio = [[f"${prom_price:.2f}", f"${min_price:.2f}", f"${max_price:.2f}"]]
    tabla_ram = [[f"{prom_ram:.2f}", f"{min_ram:.2f}", f"{max_ram:.2f}"]]
    tabla_vram = [[f"{prom_vram:.2f}", f"{min_vram:.2f}", f"{max_vram:.2f}"]]
    tabla_nucleos = [[f"{prom_num_nucleos:.2f}", f"{min_nucleos:.2f}", f"{max_nucleos:.2f}"]]
    tabla_anio = [[f"{prom_anio_release:.2f}", f"{min_release}", f"{max_release}"]]
    tabla_modelos = [
        ["Mayor precio", model_max_comp, f"${max_price:.2f}"],
        ["Menor precio", model_min_comp, f"${min_price:.2f}"]
    ]
    print("\n[Precio]")
    print(tabulate(tabla_precio, headers=["Promedio", "Minimo", "Maximo"], tablefmt="pretty"))
    print("\n[RAM (GB)]")
    print(tabulate(tabla_ram, headers=["Promedio", "Minimo", "Maximo"], tablefmt="pretty"))
    print("\n[VRAM (GB)]")
    print(tabulate(tabla_vram, headers=["Promedio", "Minimo", "Maximo"], tablefmt="pretty"))
    print("\n[Nucleos CPU]")
    print(tabulate(tabla_nucleos, headers=["Promedio", "Minimo", "Maximo"], tablefmt="pretty"))
    print("\n[Anio de lanzamiento]")
    print(tabulate(tabla_anio, headers=["Promedio", "Minimo", "Maximo"], tablefmt="pretty"))
    print("\n[Modelos destacados]")
    print(tabulate(tabla_modelos, headers=["Tipo", "Modelo", "Precio"], tablefmt="pretty"))
    
    print("")
    
def format_req_1_for_table(computers):
    data_comp = []
    for comp in computers:
        fila = [comp["marca"], comp["total_comp"],
                f"{comp['prom_price']:.2f}", f"{comp['min_price']:.2f}", f"{comp['max_price']:.2f}",
                f"{comp['prom_ram']:.2f}", f"{comp['min_ram']:.2f}", f"{comp['max_ram']:.2f}",
                f"{comp['prom_vram']:.2f}", f"{comp['min_vram']:.2f}", f"{comp['max_vram']:.2f}",
                f"{comp['prom_nucleos']:.2f}", f"{comp['min_nucleos']:.2f}", f"{comp['max_nucleos']:.2f}",
                f"{comp['prom_anio_release']:.2f}", comp["min_release"], comp["max_release"],
                comp["model_max"], comp["model_min"]]
        data_comp.append(fila)
    return data_comp

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
""""   min_price = float(input(" Ingrese el precio mínimo: "))
    max_price = float(input(" Ingrese el precio máximo: "))

    lista, contador, p_ram, p_vram, p_price, moderno, barato, caro, tiempo = logic.req_2(control, min_price, max_price)

    print(f" Tiempo estimado:{tiempo} ms ")
    if contador == 0:
        print(" No se encontraron computadores en este rango de precio.")
        
    else:  
        print(f" Se encontraron {contador} computadores que coinciden.")
        print(f" RAM promedio:   {p_ram} GB")
        print(f" VRAM promedio:  {p_vram} GB")
        print(f" Precio promedio: ${p_price}")
        
        print("-"*50)
                
        print(" EQUIPOS DESTACADOS:")
        print(f" * El más moderno: {moderno['model']} ({moderno["brand"]}) ({moderno["release_year"]}) ({moderno["cpu_brand"]}) ({moderno["gpu_brand"]}) - {float(moderno['price'])}")
        print(f" * El más barato:  {barato['model']} ({barato["brand"]}) ({barato["release_year"]}) ({barato["cpu_brand"]}) ({barato["gpu_brand"]}) - ${float(barato['price'])}")
        print(f" * El más caro:    {caro['model']} ({caro["brand"]}) ({caro["release_year"]}) ({caro["cpu_brand"]}) ({caro["gpu_brand"]}) - ${float(caro['price'])}")
"""
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

