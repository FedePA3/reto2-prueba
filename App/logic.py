import time
import csv
import os

from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll


base_dir = os.path.dirname(os.path.realpath('__file__'))
data_dir = os.path.join(base_dir, 'Data')

csv.field_size_limit(2147483647)



def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "computers": lt.new_list()
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga datos y retorna total, computador de menor precio,
    computador de mayor precio y tiempo de carga.
    """
    start_time = get_time()

    total_computers = load_computers(catalog, filename)
    min_comp, max_comp = get_min_max_price_computers(catalog["computers"])
    first_five_comp = get_first_five(catalog)
    last_five_comp = get_last_five(catalog)
    
    end_time = get_time()
    tiempo_transcurrido = delta_time(start_time, end_time)

    return total_computers, min_comp, max_comp, tiempo_transcurrido, first_five_comp, last_five_comp

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog, min_price, max_price):
    """
    Retorna el resultado del requerimiento 2
    """

    start_time = get_time()

    lista = lt.new_list()
    tamanio = lt.size(catalog["computers"])

    contador = 0
    sum_ram = 0.0
    sum_vram = 0.0
    sum_price = 0.0
    
    most_modern = None
    min_comp = None
    max_comp = None

    for i in range(tamanio):
        computer = lt.get_element(catalog["computers"], i)
        price = float(computer["price"])
        
        if min_price <= price <= max_price:
            lt.add_last(lista, computer)
            contador += 1
            sum_ram += float(computer["ram_gb"])
            sum_vram += float(computer["vram_gb"])
            sum_price += price
            
            if most_modern is None:
                most_modern = computer
            else:
                if int(computer["release_year"]) > int(most_modern["release_year"]):
                    most_modern = computer
                elif int(computer["release_year"]) == int(most_modern["release_year"]):
                    if price > float(most_modern["price"]):
                        most_modern = computer
            
            if (min_comp is None) or (price < float(min_comp["price"])):
                min_comp = computer
            
            if (max_comp is None) or (price > float(max_comp["price"])):
                max_comp = computer


    if contador > 0:

        prom_ram = sum_ram / contador
        prom_vram = sum_vram / contador
        prom_price = sum_price / contador

    else:
        prom_ram = 0.0
        prom_vram = 0.0
        prom_price = 0.0



    end_time = get_time()
    tiempo_transcurrido = delta_time(start_time, end_time)

    return lista, contador, prom_ram, prom_vram, prom_price, most_modern, min_comp, max_comp, tiempo_transcurrido


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

# Funcion para total de computadores
def load_computers(catalog, filename):
    filepath = os.path.join(data_dir, 'computerData', filename)

    file = open(filepath, encoding="utf-8")
    reader = csv.DictReader(file)

    for computer in reader:
        lt.add_last(catalog["computers"], computer)
        
    file.close()
    return lt.size(catalog["computers"])


def get_min_max_price_computers(computers_list):
    """
    Retorna el computador de menor y mayor precio en una sola pasada.
    """
    size = lt.size(computers_list)
    if size == 0:
        return None, None

    min_comp = lt.get_element(computers_list, 0)
    max_comp = min_comp

    i = 1
    while i < size:
        comp = lt.get_element(computers_list, i)

        price = float(comp["price"])
        min_price = float(min_comp["price"])
        max_price = float(max_comp["price"])

        if price < min_price:
            min_comp = comp
        if price > max_price:
            max_comp = comp

        i += 1

    return min_comp, max_comp

def get_first_five(catalog):
    """
    Función para obtener los 5 primeros computadores del dataset
    """
    first_five = []
    tamanio = lt.size(catalog["computers"])
    for i in range(min(5,tamanio)):
        first_five.append(lt.get_element(catalog["computers"], i))

    return first_five

def get_last_five(catalog):
    """
    Función para obtener los 5 últimos computadores del dataset
    """
    last_five = []
    tamanio = lt.size(catalog["computers"])
    for i in range(max(0, tamanio - 5), tamanio):
        last_five.append(lt.get_element(catalog["computers"], i))

    return last_five