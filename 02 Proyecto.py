'''
Proyecto 02 | Crear un programa que implemente una 
agenda de contactos haciendo uso de un diccionario.
'''
import os
import pathlib

AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
ELIMINAR = 4
SALIR = 0
programa = ""

# Función menú
def menu():
    os.system('cls')
    print('       *****   Agenda Contactos   *****')
    print("----------------------------------------------")
    print(f'''       *****   MENÚ DE OPCIONES   *****
    {AGREGAR}) Agregar
    {MOSTRAR}) Mostrar
    {BUSCAR}) Buscar
    {ELIMINAR}) Eliminar
    {SALIR}) Salir
    ''')

# Función saludo 
def saludo(nombreUsuario):
    if nombreUsuario:
        print('-----------------------')
        print(f"¡Bienvenido, {nombreUsuario}!")
        print('-----------------------')
        input("Presione ENTER para continuar.")
    else:
        print('--------------------------------------------------')
        print("Bienvenido, la próxima digite su nombre por favor.")
        print('--------------------------------------------------')
        input("Presione ENTER para continuar.")

# Función despedida
def despedida(nombreUsuario):
    os.system('cls')
    if nombreUsuario:
        print('----------------------------------')
        print(f"¡Fue un gusto servirte, {nombreUsuario}!")
        print('----------------------------------')
    else:
        print('-----------------------')
        print("¡Fue un gusto servirte!")
        print('-----------------------')

# Función cargar agenda
def cargarAgenda(agenda, nombreArchivo):
    if pathlib.Path(nombreArchivo).exists():
        with open(nombreArchivo, 'r') as archivo:
            for line in archivo:
                contacto, telefono, email = line.strip().split(',')
                agenda.setdefault(contacto, (telefono, email))
    else:
        with open(nombreArchivo, 'w') as archivo: 
            pass

# Función agregar 
def agregarContacto(agenda, nombreArchivo):
    os.system('cls')
    print("            *** Mis Contactos ***             ")
    print("----------------------------------------------")
    print("          *****     AGREGAR     *****         ")
    nombre = input("Digite un nombre: ")
    if agenda.get(nombre):
        print("Ese contacto ya existe.")
    else:
        telefono = input("Digite el número de teléfono: ")
        email = input("Digite el correo electrónico: ")
        with open(nombreArchivo, 'a') as archivo:
            archivo.write(f'{nombre}, {telefono}, {email}\n')
            print('----------------------------')
            print("Contacto agregado con éxito.")
        archivo.close()

# Función mostrar 
def mostarContacto(agenda,nombreArchivo):
    os.system('cls')
    print("            *** Mis Contactos ***             ")
    print("----------------------------------------------")
    print("          *****     MOSTAR     *****          ")
    if len(agenda) > 0:
        with open(nombreArchivo, 'r') as archivo:
            for contacto, datos in agenda.items():
                print(f"Nombre: {contacto}")
                print(f"Teléfono: {datos[0]}")
                print(f"Correo: {datos[1]}")
                print('-----------------------------')
    else:
        print('-----------------------------')
        print('No hay contactos registrados.')

# Función buscar
def buscarContacto(agenda, nombreArchivo):
    os.system("cls")
    print("            *** Mis Contactos ***             ")
    print("----------------------------------------------")
    print("          *****     BUSCAR     *****          ")
    if len(agenda) > 0:
        nombre = input("Digite un nombre: ")
        cuentaCont = 0
        with open(nombreArchivo, 'r') as archivo:
            for contacto, datos in agenda.items():
                if nombre in contacto:
                    print(f"Nombre: {contacto}")
                    print(f"Teléfono: {datos[0]}")
                    print(f"Correo: {datos[1]}")
                    print('-----------------------------')
                    cuentaCont += 1
                elif cuentaCont == 0:
                    print("No se encontró el contacto.")
                    break
            print(f"Se encontraron {cuentaCont} contactos.")
    else:
        print('-----------------------------')
        print("No hay contactos registrados.")
        
# Funcion eliminar contacto
def eliminarContacto(agenda, nombreArchivo):
    os.system('cls')
    print("            *** Mis Contactos ***             ")
    print("----------------------------------------------")
    print("         *****     ELIMINAR     *****         ")
    if len(agenda) > 0:
        nombre = input("Digite el nombre del contacto que desea eliminar: ")
        if agenda.get(nombre):
            with open(nombreArchivo, 'r') as archivo:
                lineas = archivo.readlines()
            archivo.close()
            with open(nombreArchivo, 'w') as archivo:
                for linea in lineas:
                    if nombre not in linea:
                        archivo.write(linea)
            archivo.close()
            print("¡Contacto eliminado con éxito!")
            print('------------------------------')
        else:
            print('----------------------------------')
            print("El contacto que ingresó no existe.")
    else:
        print('-----------------------------')
        print("No hay contactos registrados.")

def main():
    agenda = dict()
    nombreArchivo = "Agenda de Contactos.txt"
    os.system('cls')
    print("-------------------")
    print("Solicitud de nombre")
    print("-------------------")
    nombreUsuario = input("Digite su nombre: ")
    os.system('cls')
    saludo(nombreUsuario)
    continuar = True
    while continuar:
        cargarAgenda(agenda, nombreArchivo)
        menu()
        opc = int(input("Seleccione una opción: "))
        if opc == AGREGAR:
            agregarContacto(agenda, nombreArchivo)
        elif opc == MOSTRAR:
            mostarContacto(agenda, nombreArchivo)
        elif opc == BUSCAR:
            buscarContacto(agenda,nombreArchivo)
        elif opc == ELIMINAR:
            eliminarContacto(agenda, nombreArchivo)
        elif opc == SALIR:
            continuar = False
        else:
            print("Opción no válida.")
        input("Presione ENTER para continuar")
    os.system('cls')
    print('-----------------------------------')
    programa = str(input("¿Desea salir del programa? Si/No -> "))
    if programa == 'Si' or programa == 'sI' or programa == 'SI' or programa == 'si':
        despedida(nombreUsuario)
        continuar = False
    elif programa == 'No' or programa == 'nO' or programa == "NO" or programa == 'no':
        main()
    else:
        print('------------------------------')
        print("¡Lo sentimos, opción inválida!")    
        print('------------------------------')

if __name__ == '__main__':
    main()