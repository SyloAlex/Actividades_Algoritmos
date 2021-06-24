# Busqueda lineal:
def linear_search(vector, key, key_name = ""):
    temp = None
    for element in vector:
        if element.get(key_name) is not None:
            if element[key_name] == key:
                temp = element
                break
    
    return temp

#Busqueda binaria:
def binary_search(vector, key, key_name = ""):
    if len(vector) == 0:
        return None
    mid = len(vector) // 2
    if vector[mid].get(key_name) is not None:
        if vector[mid][key_name] == key:
            return vector[mid]
        elif key < vector[mid][key_name]:
            return binary_search(vector[0: mid], key, key_name)
        else:
            return binary_search(vector[mid + 1:], key, key_name)