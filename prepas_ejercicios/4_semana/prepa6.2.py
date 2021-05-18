# A continuación se te presentan 5 códigos postales escritos en código Morse, 
# todos almacenados en un mismo string y separados por “*”. Tu labor consiste en descifrar 
# cuáles son los números que componen cada código utilizando un diccionario que contenga lo 
# mostrado en la tabla.

postal_codes = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____."

morse_code = {".____": 1, "..___": 2, "...__": 3, "...._": 4,
              ".....": 5, "_....": 6, "__...": 7, "___..": 8,
              "____.": 9, "_____": 0}

def check_for_postal_code(postal, morse):
    postals = postal.split("*")
    postal_codes_list = []
    for postal_code in postals:
        postal_number = postal_code.split(" ")
        code_number = ""
        for code in postal_number:
            for morse_code, number in morse.items():
                if code == morse_code:
                    code_number += str(number)
        postal_codes_list.append(int(code_number))
    print("Los codigos postales son:", *postal_codes_list, sep= "/")

check_for_postal_code(postal_codes, morse_code)
