def main():
    contacto1 = agenda()
    while True:
        print('**--MENÚ--**')
        print('1. añadir contacto')
        print('2. lista de contactos')
        print('3. buscar contacto')
        print('4. editar contacto')
        print('5. salir')
        print('')
        opcion = input('bienvenidos que desea hacer? ')
        print('')
        

        if (opcion == '1'):
            print('')
            contacto1.registro()
        elif (opcion == '2'):
            print('')
            contacto1.mostrar_registro()
        elif opcion == '3':
            print('')
            contacto1.editar_registro()
        elif opcion == '4':
            print("")
            break
            


if __name__ == "__main__":
    main()