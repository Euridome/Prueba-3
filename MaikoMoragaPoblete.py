import random, os, csv, json, math
limpiar = lambda: os.system("cls")
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
diccionario_trabajadores = {}
total = None
#Definiciones aritmeticas
def salud(sueldo):
    return sueldo * 0.07
def afp(sueldo):
    return sueldo * 0.12
def liquido(sueldobase):
    dsalud = salud(sueldobase)
    dafp = afp(sueldobase)
    return sueldobase - dsalud - dafp
#Definiciones principales caca
def menu():
    print("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Reporte de sueldos\n4. Exportar a JSON\n5. Exportar a TXT\n6. Estadisticas\n7. Salir")
def sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        #Esta parte añade a cada trabajador en la lista trabajadores, un sueldo aleatorio entre 300.000 y 2.500.000
        #ademas de agregar un apartado de descuento de salud, afp y el sueldo liquido, todo esto en el diccionario_trabajadores
        diccionario_trabajadores[trabajador] = {
            "sueldo_base": sueldo,
            "descuento_salud": int(salud(sueldo)),
            "descuento_afp": int(afp(sueldo)),
            "sueldo_liquido": int(liquido(sueldo))
        }
def clasificar_sueldos(diccionario_trabajadores):
    global contador1, contador2, contador3,total
    contador1 = 0
    contador2 = 0
    contador3 = 0
    rango_sueldo = {
        "Menor a 800.000": [],
        "Entre 800.000 y 2.000.000": [],
        "Mayor que 2.000.000": []
    }
    total = 0
    for trabajador, datos in diccionario_trabajadores.items():
        #Esta parte del codigo usa la variable datos y la transforma en la variable sueldo para clasificarla segun indica rango_sueldo
        #ademas contiene contadores para cada rango de sueldo
        sueldo = datos["sueldo_base"]
        total += sueldo
        if sueldo < 800000:
            contador1 += 1
            rango_sueldo["Menor a 800.000"].append((trabajador, sueldo))
        elif 800000 <= sueldo < 2000000:
            contador2 += 1
            rango_sueldo["Entre 800.000 y 2.000.000"].append((trabajador, sueldo))
        elif sueldo >= 2000000:
            contador3 += 1
            rango_sueldo["Mayor que 2.000.000"].append((trabajador,sueldo))
    return rango_sueldo
def impresion():
    #la variable rangos usa la funcion clasificar_sueldos para generar de manera ordenada la variable rango_sueldo y usarla para imprimir
    #en pantalla el rango, el total de personas en ese rango, el nombre del empleado, su sueldo y el total de todos los sueldos de los empleados
    rangos = clasificar_sueldos(diccionario_trabajadores)
    for rango, lista in rangos.items():
        print(f"Sueldos {rango} TOTAL: {len(lista)}")
        print(f"{"Nombre Empleado":<20}  {"Sueldo":<10}")
        for persona, sueldo in lista:
            print(f"{persona:<20}  ${sueldo:,}".replace(",","."))
        print()
    print(f"TOTAL SUELDOS: ${total:,}".replace(',', '.'))
def reporte(diccionario_trabajadores):
    #esta funcion trabaja de manera igual a la funcion impresion, pero esta imprime los datos de todas las variables dentro de diccionario_trabajadores
    print(f"{"Nombre Empleado":<20} {"Sueldo Base":<15}  {"Descuento Salud":<18}  {"Descuento AFP":<18}  {"Sueldo Liquido":<15}")
    for persona, datos in diccionario_trabajadores.items():
        sueldobase = datos["sueldo_base"]
        dsalud = datos["descuento_salud"]
        dafp = datos["descuento_afp"]
        s_liquido = datos["sueldo_liquido"]
        print(f"{persona:<20} ${sueldobase:<15,} ${dsalud:<18,} ${dafp:<18,} ${s_liquido:<15,}".replace(",","."))
def excel():
    #esta funcion solo hace que se cree un archivo csv con los datos de diccionario_trabajadores dentro
    with open("archivo.csv","w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for persona, datos in diccionario_trabajadores.items():
            sueldobase = datos["sueldo_base"]
            dsalud = datos["descuento_salud"]
            dafp = datos["descuento_afp"]
            s_liquido = datos["sueldo_liquido"]
            escritor_csv.writerow([persona,sueldobase,dsalud,dafp,s_liquido])
def jabon():
    #esta funcion solo hace que se cree un archivo json con los datos de diccionario_trabajadores dentro
    with open("archivo.json","w") as archivo_json:
        json.dump(diccionario_trabajadores,archivo_json,indent=4)
    print("Datos exportados a JSON exitosamente")
def texto():
    #esta funcion solo hace que se cree un archivo txt con los datos de diccionario_trabajadores dentro
    with open("archivo.txt","w") as archivo_txt:
        for persona, datos in diccionario_trabajadores.items():
            archivo_txt.write(f"Nombre empleado: {persona}\n")
            archivo_txt.write(f"Sueldo base: ${datos["sueldo_base"]:,}".replace(",",".") + "\n")
            archivo_txt.write(f"Descuento Salud: ${datos["descuento_salud"]:,}".replace(",",".") + "\n")
            archivo_txt.write(f"Descuento AFP: ${datos["descuento_afp"]:,}".replace(",",".") + "\n")
            archivo_txt.write(f"Sueldo Liquido: ${datos["sueldo_liquido"]:,}".replace(",",".") + "\n")
            archivo_txt.write("\n")
    print("Datos exportados a TXT de manera exitosa.")
def esperar():
    #esta funcion hace un espacio para que de tiempo a leer lo que pasa dentro del codigo y no se salte automaticamente los datos
    global tecla
    tecla = input("Ingrese tecla cualquiera para continuar.")
def promedio():
    if total == None:
        print("para obtener el promedio de trabajadores primero ejecute la opcion 2.")
    else:
        prom = int(total / 10)
        print(f"El promedio de sueldo de los trabajadores es: ${prom:,}".replace(",","."))
def estadisticas():
    if not diccionario_trabajadores:
        print("No hay datos de trabajadores, por favor primero ingrese la opcion 1.")
        return None, None
    mayor_sueldo = max(diccionario_trabajadores, key=lambda k: diccionario_trabajadores[k]["sueldo_base"])
    menor_sueldo = min(diccionario_trabajadores, key=lambda k: diccionario_trabajadores[k]["sueldo_base"])
    print(f"El empleado con mayor sueldo es: {mayor_sueldo} y su sueldo es: ${diccionario_trabajadores[mayor_sueldo]["sueldo_base"]:,}".replace(",","."))
    print(f"El empleado con menor sueldo es: {menor_sueldo} y su sueldo es: ${diccionario_trabajadores[menor_sueldo]["sueldo_base"]:,}".replace(",","."))
    return mayor_sueldo, menor_sueldo
def media_geometrica():
    if not diccionario_trabajadores:
        print("No hay datos de trabajadores, por favor ingrese primero la opcion 1.")
        return None
    sueldos = [datos["sueldo_base"] for datos in diccionario_trabajadores.values()]
    producto = math.prod(sueldos)
    media_geo = int(producto ** (1 / len(sueldos)))
    print(f"La media geometrica de los sueldos es: ${media_geo:,}".replace(",","."))
    return media_geo
def app():
    try:
        global contadorantibombasnucleares
        contadorantibombasnucleares = 0
        while True:
            limpiar()
            menu()
            op = input("Elija una opción: ")
            if op.isdigit():
                op = int(op)
                if op == 1:
                    limpiar()
                    sueldos_aleatorios()
                    print("Sueldos generados exitosamente.")
                    esperar()
                elif op == 2:
                    limpiar()
                    clasificar_sueldos(diccionario_trabajadores)
                    impresion()
                    esperar()
                elif op == 3:
                    limpiar()
                    reporte(diccionario_trabajadores)
                    excel()
                    print("Reporte generado exitosamente en 'archivo.csv'.")
                    esperar()
                elif op == 4:
                    limpiar()
                    jabon()
                    esperar()
                elif op == 5:
                    limpiar()
                    texto()
                    esperar()
                elif op == 6:
                    limpiar()
                    promedio()
                    estadisticas()
                    media_geometrica()
                    esperar()
                elif op == 7:
                    limpiar()
                    print("Finalizando Programa....\nDesarrollado por Maiko Moraga\nRUT 20.871.562-3")
                    break
                else:
                    print("Opcion erronea, intente nuevamente")
                    esperar()
            else:
                contadorantibombasnucleares += 1
                if contadorantibombasnucleares >= 999999999:
                    print("Saliendo del programa...")
                    break
                else:
                    print("Algo malo ocurrió.")
    except ValueError:
        print("Opción seleccionada erronea")
app()
