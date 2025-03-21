from pessoa import pessoa

class Cliente:
    def __init__(self, endereco, telefone, email, genero):
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        self._genero = genero