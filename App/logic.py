import time
import csv
import os
import random
from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_linear_probing as mp
csv.field_size_limit(2147483647)
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'



def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        'computers': None,
                        }
    catalog['computers'] = al.new_list()
    return catalog



def comparacion(objeto1,objeto2):
    precio1 = mp.get(objeto1,"price")
    precio2 = mp.get(objeto2,"price")
    if precio1 < precio2:
        return True
    if precio2 < precio1:
        return False
    if precio1 == precio2:
        modelo1 = mp.get(objeto1,"model")
        modelo2 = mp.get(objeto2,"model")
        if modelo1 < modelo2:
            return True
        else:
            return False



def load_data(catalog):
    start = get_time()
    booksfile = data_dir + 'computer_prices_100.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    computers = catalog['computers']
    total = 0
    Os = mp.new_map(4,0.5)
    Oss = al.new_list()
    Año_minimo = float("inf")
    Año_maximo = 0
    precio_minimo = float("inf")
    precio_maximo = 0
    primeros = al.new_list()
    ultimos = al.new_list()
    for x in input_file:
        mapa = mp.new_map(34,0.5)
        for y in x:
            if y == "release_year" or y == "cpu_cores" or y == "cpu_tier" or y == "gpu_tier" or y == "vram_gb" or y == "ram_gb" or y == "storage_gb" or y == "storage_drive_count" or y == "refresh_hz" or y == "battery_wh" or y == "charger_watts" or y == "psu_watts" or y == "warranty_months":
                mp.put(mapa,y,int(x[y]))
            elif y == "price" or y == "cpu_threads" or y == "cpu_base_ghz" or y == "cpu_boost_ghz" or y == "display_size_in" or y == "bluetooth" or y == "weight_kg":
                mp.put(mapa,y,float(x[y]))
            else:
                mp.put(mapa,y,x[y])
        al.add_last(computers,mapa)
        total += 1
        sistema = mp.get(mapa,"os")
        suma = mp.get(Os,sistema)
        if suma != None:
            mp.put(Os,sistema,suma + 1)
        else:
            mp.put(Os,sistema,1)
            al.add_last(Oss,sistema)
        if total <= 5:
            al.add_last(primeros,mapa)
        if total > 99995:
            al.add_last(ultimos,mapa)
        año = mp.get(mapa,"release_year")
        if año > Año_maximo:
            Año_maximo = año
        if año < Año_minimo:
            Año_minimo = año
        precio = mp.get(mapa,"price")
        if precio > precio_maximo:
            precio_maximo = precio
        if precio < precio_minimo:
            precio_minimo = precio
            
    al.quick_sort(primeros,comparacion)
    al.quick_sort(ultimos,comparacion)
    al.exchange(primeros,0,4)
    al.exchange(primeros,1,3)
    al.exchange(ultimos,0,4)
    al.exchange(ultimos,1,3)

    end = get_time()
    tiempo = delta_time(start,end)
    
    return tiempo,total,Os,Año_minimo,Año_maximo,precio_minimo,precio_maximo,primeros,ultimos,Oss



    



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


def req_3(catalog,N,GPU,Brand):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    
    start = get_time()
    computadores = catalog["computers"]
    total = 0
    ram = 0
    lista_filtrada = al.new_list()
    for i in range(al.size(computadores)):
        computador = al.get_element(computadores,i)
        if mp.get(computador,"brand") == Brand and mp.get(computador,"gpu_model") == GPU:
            al.add_last(lista_filtrada,computador)
            total += 1
            ram += mp.get(computador,"ram_gb")
    al.merge_sort(lista_filtrada,criterio_req3)
    lista_computadores = al.new_list()
    tamaño = al.size(lista_filtrada)-1
    if N <= al.size(lista_filtrada):
        limite = N
    else:
        limite = al.size(lista_filtrada)
    
    for i in range(limite):
        elemento = al.get_element(lista_filtrada,tamaño-i)
        al.add_last(lista_computadores,elemento)
    if total > 0:
        ram = ram/total
    end = get_time()
    tiempo = delta_time(start,end)
    
    return tiempo,total,ram,lista_computadores


def criterio_req3(comp1,comp2):
    precio1 = mp.get(comp1, "price")
    precio2 = mp.get(comp2, "price")
    if precio1 != precio2:
        return precio1 < precio2

    # empate → peso
    peso1 = mp.get(comp1, "weight_kg")
    peso2 = mp.get(comp2, "weight_kg")

    return peso1 < peso2


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

def req_6(catalog,N,form_factor,display_type):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start = get_time()
    computadores = catalog["computers"]
    total = 0
    Windows = 0
    linux = 0
    lista_puntaje = al.new_list()
    mapa_puntaje = mp.new_map(100000,0.5)
    for i in range(al.size(computadores)):
        computador = al.get_element(computadores,i)
        if mp.get(computador,"form_factor") == form_factor and mp.get(computador,"display_type") == display_type:
            total += 1
            puntaje = (mp.get(computador,"battery_wh") * mp.get(computador,"cpu boost ghz"))/mp.get(computador,"charger_watts")
            al.add_last(lista_puntaje,puntaje)
            mp.put(mapa_puntaje,puntaje,computador)
            if mp.get(computador,"os") == "Windows":
                Windows += 1
            if mp.get(computador,"os") == "linux":
                linux += 1
    al.quick_sort(lista_puntaje,al.default_sort_criteria)
    lista = al.new_list()
    tamaño = al.size(lista_puntaje) - 1
    for i in range(N):
        p = al.get_element(lista_puntaje,tamaño-i)
        computador = mp.get(mapa_puntaje,p)
        if tamaño-i > 0:
            anterior = (tamaño-i) -1
            r = al.get_element(lista_puntaje,anterior)
            if r == p:
                comant = mp.get(mapa_puntaje,r)
                preciop = mp.get(computador,"price")
                precior = mp.get(comant,"price")
                if preciop < precior:
                    al.exchange(lista_puntaje,tamaño-i,anterior)
                    al.add_last(lista,comant)
                else:
                    al.add_last(lista,computador)
            else:
                al.add_last(lista,computador)
        else:
            al.add_last(lista,computador)
    end = get_time()
    tiempo = delta_time(start,end)
    return tiempo,total,Windows,linux,lista


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
