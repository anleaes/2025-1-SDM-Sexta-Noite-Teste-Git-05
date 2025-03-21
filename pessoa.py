class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def _str_(self):
        return f"{self.nome}{self.sobrenome}"
