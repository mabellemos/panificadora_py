caminho = '/workspace/panificadora_py/database/funcionarios.txt'
from Usuario import Usuario

class Funcionario (Usuario):
    def __init__ (self, user, senha, id, nome, funcao):
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
    def salvar(self, user, senha, id):

        super().salvar(user, senha)
        funcEncontrado = False

        with open (caminho , 'r') as arquivo:
            linhas = arquivo.readlines()

            if (len(linhas) == 0):
                with open (caminho , 'a') as arquivo:
                    arquivo.write(f"{id},{nome},{funcao}\n")
                    print("Funcionário foi salvo com sucesso!")
            else:
                for linha in linhas:
                    if id in linha:
                       funcEncontrado = True

                if funcEncontrado == True:
                    print("\nNão foi possível cadastrar o funcionário no sistema. Tente novamente!")
                else:
                    with open (caminho , 'a') as arquivo:
                        arquivo.write(f"{id},{nome},{funcao}\n")
                        print("Funcionário foi salvo com sucesso!")

    def exibir(self):
            with open(caminho, 'r') as arquivo:
                print('\nFuncionários do Sistema\n')
                super().exibir()
                for linha in arquivo:    
                    if linha.strip():        
                        id, nome, funcao = linha.strip().split(',')
                        print(f'\nID: {id}\nNome: {nome}\nFunção: {funcao}\nUserName: {super().getUser()}\n')

    def excluir(self, id): 
        with open (caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = [] 

            for linha in linhas: 
                if id not in linha: 
                    linhasSalvas.append(linha)

        with open(caminho, 'w') as arquivo: 
            arquivo.writelines(linhasSalvas)
            print("\nFuncionário ecluído do sistema!")

    def alterarFunc(self, id):
        opc = int(input("\nAlteração de Dados do Funcionário\n\nInforme a informação a ser alterada:\n\n1 - UserName\n2 - Senha3 - Nome\n4 - Função"))

        if(opc == 1):
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
                        arquivo.write(f"{super().getUser()},{super().getSenha()},{id}, {nome}, {funcao}\n")
                        print("Funcionário alterado com sucesso!")    
                else:
                    print("Funcionário não foi encontrado") 