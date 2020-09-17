from os import system
class agenda():
    system('cls')
    contacto = {}
    contacto2 = {}
    nombre = ''
    telefono = ''
    Email = ''
    codigo = ''
    
    def registro(self):
        while True:
            system('cls')
            self.codigo = (input("digite el codigo del contacto: "))
            self.nombre = input("digite el nombre: ")
            self.telefono = input("digite el telefono ")
            self.Email = input("digite el EMAIL: ")
            self.contacto[self.codigo] = (self.nombre,self.telefono,self.Email)
            opcion = input("desea continuar s/n: ")

            if (opcion == "n"):
                break
        return self.contacto

def main():
    contacto1 = agenda()

if __name__ == "__main__":
    main()