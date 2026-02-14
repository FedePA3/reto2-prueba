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
    # TODO: Imprimir el resultado del requerimiento 2
    pass


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
