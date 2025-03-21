from pessoa import Pessoa 

class Cliente(Pessoa): 
    def __init__(self, nome, sobrenome, endereco, telefone, email, genero):
        super().__init__(nome, sobrenome) 
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.genero = genero

    def __str__(self):  
        return f"{super().__str__()}, {self.endereco}, {self.telefone}, {self.email}, {self.genero}"
