from cliente import Cliente

def main():
    C1 = Cliente("João", "Nunes", "Rua 1", "123456789", "email@gmail.com", "Masculino")
    C2 = Cliente("Maria", "Santos", "Rua 2", "987654321", "email3@gmail.com", "Feminino")

    print(C1)
    print(C2)

if __name__ == "__main__": 
    main()
