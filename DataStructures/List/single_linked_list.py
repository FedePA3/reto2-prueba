def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }

    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else: 
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def size(my_list):
    return my_list["size"]

def add_first(my_list, element):
    new_node = {
        "info": element,
        "next": my_list["first"],
    }
    my_list["first"] = new_node
    if my_list["last"] is None:
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = {
        "info": element,
        "next": None,
    }
    if my_list["last"] is None:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    
    return my_list["first"]["info"]

def is_empty(my_list):
    return size(my_list) == 0

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range') #Primero se valida que la posicion sea valida
    
    if pos == 0:
        my_list["first"] = my_list["first"]["next"] #Si la posicion es 0, se elimina el primer elemento

        if my_list["size"] == 1:
            my_list["last"] = None #Si la lista tiene ahora un solo elemento, se actualiza el ultimo elemento
    
    #En general eliminamos algun nodo en el medio o al final
    else:
        current = my_list["first"]
        for i in range(pos - 1):
            current = current["next"]

        current["next"] = current["next"]["next"]

        if pos == size(my_list) - 1:
            my_list["last"] = current
    my_list["size"] -= 1
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    rm_element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    return rm_element

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')

    if size(my_list) == 1:
        return remove_first(my_list)

    removed_element = my_list["last"]["info"] #Se guarda el elemento a eliminar para retornarlo al final
    
    current = my_list["first"]
    while current["next"]["next"] is not None: #asi evaluamos si el siguiente nodo no es el ultimo, si es None, es porque el siguiente nodo es el ultimo
        current = current["next"]
    current["next"] = None #se desvincula el ultimo nodo

    my_list["last"] = current #se actualiza el ultimo nodo
    my_list["size"] -= 1 #se actualiza el tamaño de la lista
    return removed_element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range')

    if pos == 0:
        return add_first(my_list, element)

    if pos == my_list["size"]:
        return add_last(my_list, element)
    
    current = my_list["first"]
    
    for i in range(pos -1): #llegamos al nodo anterior
        current = current["next"] 

    new_node = {
        "info": element,
        "next": current["next"] #asi apunta al que estaba en pos
    }

    current["next"] = new_node

    my_list["size"] += 1

    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    current = my_list["first"]

    for i in range(pos):
        current = current["next"]

    current["info"] = new_info

    return my_list


def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= size(my_list) or pos2 < 0 or pos2 >= size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos1 == pos2: #en caso de que sean iguales, no hay cambio
        return my_list
    
    #caso normal. Se navega hasta la posicion 1 y 2. Se accede a sus valores
    current1 = my_list["first"]
    for i in range(pos1):
        current1 = current1["next"]

    current2 = my_list["first"]
    for i in range(pos2):
        current2 = current2["next"]

    # guardamos tmeporalmente los datos
    info1 = current1["info"]
    info2 = current2["info"]

    #usamos los valores guardados para intercambia
    current1["info"] = info2
    current2["info"] = info1

    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"] or (pos + num_elements) > my_list["size"]:
        raise Exception("IndexError: list index out of range")

    new_sub_list = new_list() #inicializamos una lista vacia

    current = my_list["first"] #accedemos al primer nodo de la lista original

    for i in range(pos): #navegamos hasta pos
        current = current["next"]

    #copiamos num elementos a nuestra nueva lsita usando funcion ya creada add last
    for i in range(num_elements):
        add_last(new_sub_list, current["info"]) #anadimos a nuestrra nueva lista, e insertamos info del nodo de la lista original
        current = current["next"] #continuamos

    return new_sub_list
