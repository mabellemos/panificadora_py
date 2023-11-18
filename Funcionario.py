caminho = '/workspace/panificadora_py/database/funcionarios.txt'
from Usuario import Usuario

class Funcionario (Usuario):
    def __init__ (self, id, nome,funcao, user, senha, telefone):
        super().__init__(user, senha)
        self._id = id
        self._nome = nome
        self._funcao = funcao

#Métodos gets e sets
def getId(self):
    return self._id

def setId(self, id):
    self._id = id

def getNome(self):
    return self._nome

def setNome(self, nome):
    self._nome = nome

def getFuncao(self):
    return self._funcao

def setFuncao(self, funcao):
    self._funcao = funcao

#Métodos da classe
    def salvar(self):
        with open (caminho , 'a') as arquivo:
            arquivo.write(f'{self._id},{self._nome}, {self._funcao}')
            print("Funcionário foi salvo com sucesso!")

    def exibir(self):
            with open(caminho, 'r') as arquivo:
                print('\nFuncionários do Sistema\n')
                super().exibir()
                for linha in arquivo:    
                    if linha.strip():        
                        id, nome, funcao = linha.strip().split(',')
                        print(f'\nID: {id}, Nome: {nome}, Função: {funcao}')

    def excluir(self, id): 
        with open (caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = [] 

            for linha in linhas: 
                if id not in linha: 
                    linhasSalvas.append(linha)

        with open(caminho, 'w') as arquivo: 
            arquivo.writelines(linhasSalvas)

    def alterarUser(self, id):
        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []
            funcEncontrado = False
        
            for linha in linhas:
                if id not in linha:
                    linhasSalvas.append(linha)
                else:
                    funcEncontrado = True

            if funcEncontrado:
                with open (caminho, 'w') as arquivo:
                    arquivo.writelines(linhasSalvas)
        
                with open (caminho, 'a') as arquivo:
                    arquivo.write(f"{self._user},{self._senha}")
                    print("Funcionário alterado com sucesso!")    
            else:
                print("Funcionário não foi encontrado") 

