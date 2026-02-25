# Agendamiento de Horas Doctor Python

from datetime import datetime

horas_registradas = [] 

# Funciones CRUD

# Nueva Cita
def new_appointment():
    print("--- 1. NUEVA CITA MÉDICA ---")

    # 1. RUT (Identificador principal)
    while True:
        rut_input = input("RUT del Paciente: ").strip().upper()

        if validar_rut(rut_input):
            rut_formateado = formatear_rut(rut_input)
        
        # Verificar si ya existe
            paciente_encontrado = None
            for paciente_existente in horas_registradas:
                if paciente_existente["rut"] == rut_formateado:
                    paciente_encontrado = paciente_existente
                    break
            
            if paciente_encontrado:
                print(f"\n[AVISO] El paciente {paciente_existente['nombre']} ya tiene una cita.")
                if input("¿Desea MODIFICAR la cita existente? (s/n): ").lower() == 's':
                    modify_appointment_aux(paciente_encontrado)
                return
            
            break
        else:
            print("[!] RUT inválido. Intente nuevamente.")

    # 2. Nombre
    nombre = input("Nombre Completo: ").strip().title()

    # 3. Edad (Validación numérica)
    while True:
        edad = input("Edad: ").strip()
        if validar_edad(edad): break
        print("[!] Ingrese una edad válida (0-120).")

    # 4. Dirección y 5. Comuna
    direccion = input("Dirección: ").strip()
    comuna = input("Comuna: ").strip()

    # 6. Celular
    celular = input("Celular (Ej: +56912345678): ").strip()

    # 7. Correo (Validación de formato)
    while True:
        correo = input("Correo Electrónico: ").strip().lower()
        if validar_correo(correo): break
        print("[!] Formato de correo inválido (ejemplo@dominio.com).")

    # 8. Previsión
    prevision = input("Previsión (Fonasa/Isapre/Particular): ").strip()

    # 9. Fecha (Validación de calendario)
    while True:
        fecha = input("Fecha de Atención (DD/MM/AAAA): ").strip()
        if validar_fecha(fecha): break
        print("[!] Fecha no válida o formato incorrecto (DD/MM/AAAA).")

    # 10. Hora (Validación de reloj)
    while True:
        hora = input("Hora de Atención (HH:MM): ").strip()
        if validar_hora(hora): break
        print("[!] Hora no válida (00:00 - 23:59).")

    # Guardar todo en el diccionario
    nuevo_paciente = {
        "rut": rut_formateado, 
        "nombre": nombre, 
        "edad": edad,
        "direccion": direccion, 
        "comuna": comuna,
        "celular": celular, 
        "correo": correo,
        "prevision": prevision, 
        "fecha": fecha, 
        "hora": hora
    }

    horas_registradas.append(nuevo_paciente)
    ordenar_citas()
    print("\n" + "-"*35)
    print(f"¡EXITO! Cita agendada para {nombre}")
    print(f"Día: {fecha} a las {hora} hrs.")


# Validación de RUT
def validar_rut(rut):
    # 1. Limpiar el RUT (quitar puntos, guiones y espacios)
    rut = rut.replace(".", "").replace("-", "").strip().upper()
    
    # 2. Validar largo mínimo (al menos un número y un DV)
    if len(rut) < 2 or len(rut) > 9:
        return False
    
    cuerpo = rut[:-1]
    dv = rut[-1]
    
    # 3. Validar que el cuerpo sean solo números
    if not cuerpo.isdigit():
        return False
    
    # 4. Calcular el dígito verificador esperado
    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo = 2 if multiplo == 7 else multiplo + 1
    
    dv_esperado = 11 - (suma % 11)
    if dv_esperado == 11: dv_esperado = '0'
    elif dv_esperado == 10: dv_esperado = 'K'
    else: dv_esperado = str(dv_esperado)
    
    return dv == dv_esperado


# Dar formato al RUT para el guardado en el registro
def formatear_rut(rut_sucio):
    # 1. Limpiar: quitar puntos, guiones y espacios
    rut_limpio = rut_sucio.replace(".", "").replace("-", "").strip().upper()
    
    # 2. El cuerpo es todo menos el último dígito
    cuerpo = rut_limpio[:-1]
    dv = rut_limpio[-1]
    
    # 3. Retornar el formato estándar: "XXXXXXXX-X"
    return f"{cuerpo}-{dv}"


#Validar formato correo electrónico
def validar_correo(correo):
    # Verificamos que tenga una '@', que no sea el primer carácter y que tenga al menos un '.' después de la '@'
    if "@" in correo and correo.index("@") > 0:
        parte_dominio = correo.split("@")[1]
        if "." in parte_dominio and parte_dominio.index(".") > 0:
            return True
    return False


#Validación de edad como sólo números
def validar_edad(edad_str):
    # Verifica que sea un número y que esté en un rango razonable
    if edad_str.isdigit():
        edad = int(edad_str)
        return 0 <= edad <= 120
    return False


# Validación formato de fecha dd/mm/aaaa
def validar_fecha(fecha_str):
    try:
        # Intenta convertir el texto a una fecha real
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


#Validación formato de hora HH:MM
def validar_hora(hora_str):
    try:
        # Intenta convertir el texto a una hora real
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False


# Modificar cita de paciente desde el menú
def modify_appointment():
    print("\n--- 3. MODIFICAR HORA ---")

    if not horas_registradas:
        print("No se puede acceder a Modificar Hora. No existen registros en el sistema.")
        return
    
    rut_modificar = input("Ingrese RUT del paciente para modificar su hora: ")

    for rut_paciente in horas_registradas:
        if rut_paciente["rut"] == rut_modificar:
            modify_appointment_aux(rut_paciente)
            return
        
    print(f"El paciente RUT: {rut_modificar} no tiene horas agendadas en la clínica")

# Modificar cite del paciente desde el menú o función búsqueda
def modify_appointment_aux(paciente):
    print(f"\n--- ACTUALIZANDO DATOS DE: {paciente['nombre']} ---")
    print("Presione ENTER para mantener el dato actual.")

    nueva_fecha = input(f"Nueva fecha ({paciente['fecha']}): ")
    nueva_hora = input(f"Nueva hora ({paciente['hora']}): ")

    if nueva_fecha:
        paciente["fecha"] = nueva_fecha
    if nueva_hora:
        paciente["hora"] = nueva_hora
    
    ordenar_citas()
    print("¡Información actualizada correctamente!")

# Buscar Cita de Paciente
def search_appointment():
    print("\n--- 2. BUSCAR HORA ---")

    if not horas_registradas:
        print("No se puede acceder a Buscar Hora. No existen registros en el sistema.")
        return 
           
    rut_buscar = input("Ingrese el RUT del paciente a consultar: ")
    encontrado = False

    for i, rut_paciente in enumerate(horas_registradas):
        if rut_paciente["rut"] == rut_buscar:
            print(f"\nPaciente encontrado: {rut_paciente['nombre']}")
            print(f"Hora agendada par el día {rut_paciente['fecha']} a las {rut_paciente['hora']} horas.")
            encontrado = True

            #Pregunta si desea modificar
            print("\n¿Qué desea hacer con este registro?")
            print("1. Modificar Hora Agendada")
            print("2. Eliminar Hora Agendada")
            print("3. Regresar al Menú Principal")
            buscar = input("Seleccione una opción (1, 2 o 3): ")
            if buscar == "1":
                modify_appointment_aux(rut_paciente)
            elif buscar == "2":
                confirmar_y_eliminar(i)
            break

    if not encontrado:
        print(f"El paciente RUT: {rut_buscar} no tiene horas agendadas en la clínica")

# Eliminar Hora desde el menú
def delete_appointment():
    print("\n--- 4. ELIMINAR UNA HORA ---")

    if not horas_registradas:
        print("No se puede acceder a Eliminar Hora. No existen registros en el sistema.")
        return   
     
    rut_eliminar = input("Buscar por RUT para eliminar, RUT: ")

    for i in range(len(horas_registradas)):
        if horas_registradas[i]["rut"] == rut_eliminar:
            confirmar_y_eliminar(i)
            return 
        
    print("No se encontró hora agendada para un paciente con ese RUT.")   

# Confirmación eliminación Hora paciente
def confirmar_y_eliminar(indice):
    nombre = horas_registradas[indice]['nombre']
    confirmar = input(f"¿Está seguro que desea eliminar la hora de {nombre}? (s/n): ")

    if confirmar.lower() == 's':
        horas_registradas.pop(indice)
        print("Registro eliminado correctamente.")
    else:
        print("Operación cancelada.")

# Listadoi Horas Agendadas
def list_appointments():
    print("\n" + "="*40)
    print("\n--- 5. LISTA DE HORAS AGENDADAS ---")
    print("\n" + "="*40)

    if not horas_registradas:
        print("No existen registros en el sistema")
        return
    
    ordenar_citas()

    for i, rut_paciente in enumerate(horas_registradas, 1):
        print(f"\nREGISTRO #{i}")
        print(f"RUT: {rut_paciente['rut']} | Nombre: {rut_paciente['nombre']} | Edad: {rut_paciente['edad']}")
        print(f"Dirección: {rut_paciente['direccion']}, {rut_paciente['comuna']}")
        print(f"Contacto: Celular: {rut_paciente['celular']} | Correo: {rut_paciente['correo']}")
        print(f"Previsión: {rut_paciente['prevision']}")
        print(f"Fecha: {rut_paciente['fecha']} | Hora: {rut_paciente['hora']}")
        print("-" * 60)


# Ordenar citas
def ordenar_citas():
    global horas_registradas
    # Ordenamos la lista usando una clave (key) que combina fecha y hora
    horas_registradas.sort(key=lambda p: datetime.strptime(f"{p['fecha']} {p['hora']}", "%d/%m/%Y %H:%M"))


def show_menu():
    while True:
        print("\n" + "="*35)
        print("\n--- MENÚ DOCTOR PYTHON ---")
        print("\n" + "="*35)
        print("1. Nueva Hora")
        print("2. Buscar Hora")
        print("3. Modificar Hora")
        print("4. Eliminar Hora")
        print("5. Lista de Horas Agendadas")
        print("6. Salir del Sistema")
        opcion = input("Selecciona una opción (1-6): ")
        if opcion == "1":
            new_appointment()
        elif opcion == "2":
            search_appointment()
        elif opcion == "3":
            modify_appointment()
        elif opcion == "4":
            delete_appointment()
        elif opcion == "5":
            list_appointments()
        elif opcion == "6":
            salir = input("¿Está seguro que desea cerrar el sistema? (s/n): ").lower()
            if salir == "s":
                print("Cerrrando sistema... ¡HastaPronto!")
                break
        else:
            print("\nOpción inválida, intente de nuevo")

if __name__ == "__main__":
    show_menu()
