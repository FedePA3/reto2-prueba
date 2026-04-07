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
    return logic.new_logic()

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
    print(f"Tiempo de carga: {tiempo} ms")
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
    N = int(input("Ingrese el numero N de registros que quieres listar: "))
    GPU = str(input("Ingrese el modelo del GPU con el cual quiere filtrar: "))
    Brand = str(input("Ingrese la marca de computador con el cual se quiere filtrar: "))
    logica = logic.req_3(control,N,GPU,Brand)
    tiempo,total,ram,lista_computadores = logica
    print(f"Tiempo de ejecución: {tiempo} ms")
    print(f"Total de computadores que cumplieron el filtro: {total}")   
    print(f"Promedio de memoria RAM de los computadores que cumplen el filtro:   {ram:.2f}")

    print(f"Top {N}  de computadores que cumplen con el filtro")

    os_data = []
    for i in range(0,al.size(lista_computadores)):
        computador = al.get_element(lista_computadores,i)
        tipo = mp.get(computador,"device_type")
        modelo = mp.get(computador,"model")
        memoria = mp.get(computador,"ram_gb")
        almacenamiento = mp.get(computador,"storage_gb")
        marca_gpu = mp.get(computador,"gpu_brand")
        modelo_gpu = mp.get(computador,"gpu_model")
        precio = mp.get(computador,"price")
        peso = mp.get(computador,"weight_kg")
        os_data.append([tipo,modelo,memoria,almacenamiento,marca_gpu,modelo_gpu,precio,peso])
    print(tabulate(os_data,
                   headers=["Tipo de dispositivo", "Modelo","Memoria RAM","Capacidad de almacenamiento","Marca de GPU","Modelo de GPU","Precio","Peso"],
                   tablefmt="grid",
                   colalign=("left", "right")))


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
    N = int(input("Ingrese el numero N de registros que quieres listar: "))
    form_factor = str(input("Ingrese el factor de forma con el cual quiere filtrar: "))
    display_type = str(input("Ingrese el tipo de pantalla con el cual se quiere filtrar: "))
    logica = logic.req_6(control,N,form_factor,display_type)
    tiempo,total,Windows,linux,lista = logica
    print(f"Tiempo de ejecución: {tiempo} ms")
    print(f"Total de computadores que cumplieron el filtro: {total}")   
    print(f"Total de computadores con sistema operativo Windows que cumplieron el filtro:   {Windows}")
    print(f"Total de computadores con sistema operativo Linux que cumplieron el filtro:   {linux}")
    print(f"Top {N}  de computadores que cumplen con el filtro")

    os_data = []
    for i in range(0,al.size(lista)):
        computador = al.get_element(lista,i)
        modelo = mp.get(computador,"model")
        memoria = mp.get(computador,"ram_gb")
        modelo_cpu = mp.get(computador,"cpu_model")
        cpu_boost_ghz = mp.get(computador,"cpu_boost_ghz")
        puntaje = (mp.get(computador,"battery_wh") * mp.get(computador,"cpu_boost_ghz"))/mp.get(computador,"charger_watts")
        puntaje = round(puntaje,2)
        os_data.append([modelo,memoria,modelo_cpu,cpu_boost_ghz,puntaje])
    print(tabulate(os_data,
                   headers=["Modelo","Memoria RAM","Modelo de CPU","Frecuencia máxima boost del CPU","Puntaje de eficiencia"],
                   tablefmt="grid",
                   colalign=("left", "right")))

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
