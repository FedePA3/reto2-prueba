def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

#DONE Implementación función add_first()
def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

#DONE Implementación función add_last()
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

#DONE Implementación función size()
def size(my_list):
    return my_list["size"]

#DONE Implementación función is_empty()
def is_empty(my_list):
    return size(my_list) == 0

#DONE Implementación función first_element()
def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][0]

#DONE Implementación función last_element()
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["elements"][-1]
    
#DONE Implementación función delete_element()
def delete_element(my_list,pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list

#DONE Implementación función remove_first()
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
   
    rm_element = my_list["elements"].pop(0)
    my_list["size"] -=1
    return rm_element

#DONE Implementación función remove_last()
def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
 
    rm_element = my_list["elements"].pop()
    my_list["size"] -=1
    return rm_element

#DONE Implementación función insert_element()
def insert_element(my_list,element,pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')

    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list
    
#DONE Implementación función change_info()
def change_info(my_list,pos,new_info):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')

    my_list["elements"][pos] = new_info
    return my_list

#DONE Implementación función exchange()
def exchange(my_list,pos_1,pos_2):
    if (pos_1 < 0 or pos_1 > size(my_list)) or (pos_2 < 0 or pos_2 > size(my_list)):
        raise Exception('IndexError: list index out of range')
    
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = my_list["elements"][pos_1]
    return my_list

#DONE Implementación función sub_list()
def sub_list(my_list,pos_i,num_elements):
    if (pos_i < 0 or pos_i >= size(my_list)) or (num_elements<0 or pos_i+num_elements > size(my_list)):
        raise Exception('IndexError: list index out of range')
    
    new_sublist = {}
    new_sublist["elements"] = my_list["elements"][pos_i:pos_i+num_elements]
    new_sublist["size"] = num_elements
    return new_sublist

    


