import re
opcion = 0
while opcion != 11:
    print("Expresiones Regulares\n"
    "1-Todas las palabras que contengan una longitud de 7 o mas letras\n"
    +"2-Expresiones  que no finalicen con una vocal\n"
    +"3-Las palabras que inicien con M donde la segunda letra no sea una Vocal\n"
    +"4-Expresiones encerradas entre comillas\n"
    +"5-Ip´s\n"
    +"6-Horas\n"
    +"7-Telefonos\n"
    +"8-Correo electronico\n"
    +"9-URL´S\n"
    +"10-Codigo Postal\n"
    +"11-Salir\n")
    opcion = int(input("Seleccione un ejercicio:"))
    if opcion ==1:
        print("Todas las palabras que contengan una longuitud de 7 a mas letras")
        f  = open(
            "prueba.txt"
        ).read()
        ExpReg = "[A-Za-z]{7,}"
        Exp = re.findall(ExpReg,f,flags=re.MULTILINE)
        print(Exp)
    elif opcion ==2:
        print("Expresiones que no finalicen con una vocal")
        f = open("prueba.txt"
        ).read()
        ExpReg = "[a-zA-Z]+[^aeiou]\s"
        Exp = re.findall(ExpReg,f,flags=re.MULTILINE)
        print(Exp)
    elif opcion ==3:
        print("Las palabras que inicien con M donde la segunda letra no sea una Vocal")
        f = open("prueba.txt"
        ).read()
        ExpReg ="M[^aeiou][a.zA-Z]{1,}"
        Exp = re.findall(ExpReg,f,flags=re.MULTILINE)
        print(Exp)
    elif opcion ==4:
        print ("Expresiones encerradas entre comillas")
        f = open("prueba.txt"
        ).read()
        Expresiones = "(\".*?\"|'.*?')"
        Exp = re.findall(Expresiones, f, flags=re.MULTILINE)
        print(Exp)
    elif opcion ==5:
        print("Ip´s")
        f = open("prueba.txt"
        ).read()
        ExpReg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion ==6:
        print("Horas")
        f = open("prueba.txt"
        ).read()
        ExpReg = "(?:[01]\d|2[0-3]):[0-5]\d"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion ==7:
        print("Telefonos")
        f = open("prueba.txt"
        ).read()
        ExpReg = "\d[0-9]{7,10}"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion ==8:
        print("Correos electronicos")
        f = open("prueba.txt"
        ).read()
        ExpReg = r'[a-zA-Z0-9_\-\.]{2,}@[a-zA-Z0-9_\-\.]{2,}\.[a-zA-Z]{2,4}'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion ==9:
        print("Url´s")
        f = open("prueba.txt"
        ).read()
        ExpReg = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion ==10:
        print("Codigo Postal")
        f = open("prueba.txt"
        ).read()
        ExpReg = "^(\d{5}$)"
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)
    elif opcion ==11:
        print("Opcion 11")
    else:
        print("\n¡¡¡La Opcion seleccionada es Incorrecta!!!")

print("Prueba Terminada")