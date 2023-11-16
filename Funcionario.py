class Funcionario ( Usuario):
    def __init__ (self, id, nome, acesso, funcao, user, senha, telefone):
        super().__init__(id, nome, telefone)
        super().__init__(user, acesso, senha)
        self._funcao = funcao

def getFuncao(self):
    return self._funcao

def setFuncao(self, funcao):
    self._funcao = funcao

