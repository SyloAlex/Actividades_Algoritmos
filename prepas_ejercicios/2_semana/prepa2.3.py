#Ejercicio 2.3: A continuación se te presentan 5 códigos postales escritos en código Morse, 
#todos almacenados en un mismo string y separados por “*”. 
#Tu labor consiste en descifrar cuáles son los números que componen cada código.

codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____."

def morse_to_numb(morse):
    morse_list = morse.split("*")
    code_list = []
    for morse_code in morse_list:
        morse_code = morse_code.split(" ")
        code_number = ""
        for code in morse_code:
            if code == ".____":
                code_number += "1"
            if code == "..___":
                code_number += "2"
            if code == "...__":
                code_number += "3"
            if code == "...._":
                code_number += "4"
            if code == ".....":
                code_number += "5"
            if code == "_....":
                code_number += "6"
            if code == "__...":
                code_number += "7"
            if code == "___..":
                code_number += "8"
            if code == "____.":
                code_number += "9"
            if code == "_____":
                code_number += "0"
        code_list.append(code_number)
    return code_list

prueba = morse_to_numb(codigos_postales)
print(prueba)