caminho = '/workspace/panificadora_py/database/usuarios.txt'

class Usuario:
    def __init__(self, user, senha):
        self._user = user
        self._senha = senha

    #Métodos gets e sets
    def getUser(self):
        return self._user

    def setUser(self, user):
        self._user = user

    def getSenha(self):
        return self._senha

    def setSenha(self, senha):
        self._acesso = acesso

    #Métodos da classe
    def salvar(self):
        with open (caminho , 'a') as arquivo:
            arquivo.write(f'{self._user},{self._senha}')
            print("Usuário foi salvo com sucesso!")

    # def logar(self, user, senha):
    #     with open (caminho, 'r') as arquivo:
    #         lista = str(arquivo.readlines())
    #         print(len(lista))
    #         for i in range(len(lista)):
    #             name = user[i].replace("['", "")
    #             passw = user[i].replace("['", "")
    #             print(name)
    #             print(passw)

    #             if (user == name and senha == passw):
    #                 return True
    #             else:
    #                 return False

    def exibir(self):
            with open(caminho, 'r') as arquivo:
                print('\nUsuários do Sistema\n')
                for linha in arquivo:    
                    if linha.strip():        
                        user, senha = linha.strip().split(',')
                        print(f'UserName: {self._user}, Senha: {senha}')

    def excluir(self, nome): 
        with open (caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = [] 

            for linha in linhas: 
                if nome not in linha: 
                    linhasSalvas.append(linha)

        with open(caminho, 'w') as arquivo: 
            arquivo.writelines(linhasSalvas)

    def alterarUser(self, nome):
        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []
            usuarioEncontrado = False
        
            for linha in linhas:
                if nome not in linha:
                    linhasSalvas.append(linha)
                else:
                    usuarioEncontrado = True

            if usuarioEncontrado:
                with open (caminho, 'w') as arquivo:
                    arquivo.writelines(linhasSalvas)
        
                with open (caminho, 'a') as arquivo:
                    arquivo.write(f"{self._user},{self._senha}")
                    print("Usuário alterado com sucesso!")    
            else:
                print("Usuário não foi encontrado") 

'''
Construtores (com parâmetros e sem)
Agregação
Encapsulamento 
Métodos gets/sets
Métodos da classe
Arquivos
'''