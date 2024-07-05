import random, os, csv, json
limpiar = lambda: os.system("cls")
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
diccionario_trabajadores = {}
#Definiciones aritmeticas
def salud(sueldo):
    return sueldo * 0.07
def afp(sueldo):
    return sueldo * 0.12
def liquido(sueldobase):
    dsalud = salud(sueldobase)
    dafp = afp(sueldobase)
    return sueldobase - dsalud - dafp
#Definiciones principales
def menu():
    print("1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Reporte de sueldos\n4. Exportar a JSON\n5. Salir|")
def sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
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
    rangos = clasificar_sueldos(diccionario_trabajadores)
    for rango, lista in rangos.items():
        print(f"Sueldos {rango} TOTAL: {len(lista)}")
        print(f"{"Nombre Empleado":<20}  {"Sueldo":<10}")
        for persona, sueldo in lista:
            print(f"{persona:<20}  ${sueldo:,}".replace(",","."))
        print()
    print(f"TOTAL SUELDOS: ${total:,}".replace(',', '.'))
def reporte(diccionario_trabajadores):
    print(f"{"Nombre Empleado":<20}  {"Sueldo Base":<15}  {"Descuento Salud":<18}  {"Descuento AFP":<18}  {"Sueldo Liquido":<15}")
    for persona, datos in diccionario_trabajadores.items():
        sueldobase = datos["sueldo_base"]
        dsalud = int(salud(sueldobase))
        dafp = int(afp(sueldobase))
        s_liquido = int(liquido(sueldobase))
        print(f"{persona:<20} ${sueldobase:<15,} ${dsalud:<18,} ${dafp:<18,} ${s_liquido:<15,}".replace(",","."))
def excel():
    with open("archivo.csv","w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for persona, datos in diccionario_trabajadores.items():
            sueldobase = datos["sueldo_base"]
            dsalud = int(salud(sueldobase))
            dafp = int(afp(sueldobase))
            s_liquido = int(liquido(sueldobase))
            escritor_csv.writerow([persona,sueldobase,dsalud,dafp,s_liquido])
def jabon():
    with open("archivo.json","w") as archivo_json:
        json.dump(diccionario_trabajadores,archivo_json,indent=4)
    print("Datos exportados a JSON exitosamente")
def esperar():
    global tecla
    tecla = input("Ingrese tecla cualquiera para continuar.")
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
