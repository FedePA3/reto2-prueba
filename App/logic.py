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

    end_time = get_time()
    tiempo_transcurrido = delta_time(start_time, end_time)

    return total_computers, min_comp, max_comp, tiempo_transcurrido

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


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
