import sys
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as mp
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from tabulate import tabulate
import App.logic as logic

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    pass

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
   
    datos = logic.load_data(control)
    tiempo,total,Os,Año_minimo,Año_maximo,precio_minimo,precio_maximo,primeros,ultimos, Oss = datos
    print(f"Tiempo de carga: {tiempo} segundos")
    print(f"Total de computadores cargados: {total}")   
    print(f"Año mínimo de lanzamiento:   {Año_minimo}")
    print(f"Año máximo de lanzamiento:   {Año_maximo}")
    print(f"Precio mínimo:               ${precio_minimo:,.2f}")
    print(f"Precio máximo:               ${precio_maximo:,.2f}")
    
    print("\nTotal de equipos por Sistema Operativo:")
    os_data = []
    for i in range(0,al.size(Oss)):
        sistema = al.get_element(Oss,i)
        total = mp.get(Os,sistema)
        os_data.append([sistema,total])
    print(tabulate(os_data,
                   headers=["Sistema Operativo", "Total Equipos"],
                   tablefmt="grid",
                   colalign=("left", "right")))
    
    headers = ["Marca", "Modelo", "Tipo", "CPU", "RAM (GB)", "Storage (GB)", "Año", "Precio ($)"]
    print("\n====== Primeros 5 equipos ======")
    primeros_data = []
    for i in range(0,5):
        computador = al.get_element(primeros,i)
        primeros_data.append([
            mp.get(computador,"brand"), mp.get(computador,"model"), mp.get(computador,"device_type"),
            mp.get(computador,"cpu_model"), mp.get(computador,"ram_gb"), mp.get(computador,"storage_gb"),
            mp.get(computador,"release_year"), f"{mp.get(computador,"price"):,.2f}"
        ])
    print(tabulate(primeros_data,
                   headers=headers,
                   tablefmt="grid"))
    
    print("\n====== Ultimos 5 equipos ======")
    ultimos_data = []
    for i in range(0,5):
        computador = al.get_element(ultimos,i)
        ultimos_data.append([
            mp.get(computador,"brand"), mp.get(computador,"model"), mp.get(computador,"device_type"),
            mp.get(computador,"cpu_model"), mp.get(computador,"ram_gb"), mp.get(computador,"storage_gb"),
            mp.get(computador,"release_year"), f"{mp.get(computador,"price"):,.2f}"
        ])
    print(tabulate(ultimos_data,
                   headers=headers,
                   tablefmt="grid"))
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

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

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
