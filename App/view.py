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
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    min_price = float(input(" Ingrese el precio mínimo: "))
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

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    cpu_brand = input(" Ingrese la marca de CPU: ")
    cpu_tier = input(" Ingrese el CPU tier: ")

    (
        count,
        avg_price,
        avg_ram,
        avg_vram,
        avg_threads,
        most_common_gpu,
        most_common_gpu_appearances,
        most_common_release_year,
        most_common_release_year_appearances,
        elapsed_time,
    ) = logic.req_3(control, cpu_brand, cpu_tier)

    print(f" Tiempo de ejecución: {elapsed_time} ms")
    print(f" Número total de computadores que cumplieron el filtro: {count}")

    if count == 0:
        print(" No se encontraron computadores con esos criterios.")
    else:
        data_req_3 = [
            ["Cantidad de computadores que cumplen con las características", count],
            ["Promedio de precio", f"${round(avg_price, 2)}"],
            ["Promedio de RAM", f"{round(avg_ram, 2)} GB"],
            ["Promedio de VRAM", f"{round(avg_vram, 2)} GB"],
            ["Promedio de número de hilos", round(avg_threads, 2)],
            ["GPU más frecuente", f"{most_common_gpu} ({most_common_gpu_appearances} ocurrencias)"],
            ["Año de lanzamiento más frecuente", f"{most_common_release_year} ({most_common_release_year_appearances} ocurrencias)"],
        ]
        print(tabulate(data_req_3, headers=["Métrica", "Valor"], tablefmt="pretty"))


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
