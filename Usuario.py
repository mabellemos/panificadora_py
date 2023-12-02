caminho = '/workspace/panificadora_py/database/usuarios.txt'

class Usuario:
    def __init__(self, user, senha):
        self._user = user
        self._senha = senha
    # def __init__ (self):
    #     self.inicializar()

    #Métodos gets e sets
    def getUser(self):
        return self._user

    def setUser(self, user):
        self._user = user

    def getSenha(self):
        return self._senha

    def setSenha(self, senha):
        self._senha = senha

    #Métodos da classe
    def inicializar():
        self._user = str(input("\nInforme o UserName do Usuário: "))
        self._senha = str(input("\nInforme a senha: "))

    def salvar(self, user, senha):
        userEncontrado = False

        with open (caminho , 'r') as arquivo:
            linhas = arquivo.readlines()

            if (len(linhas) == 0):
                with open (caminho , 'a') as arquivo:
                    arquivo.write(f"{user},{senha}\n")
                    print("Usuário foi salvo com sucesso!")
            else:
                for linha in linhas:
                    if user in linha:
                       userEncontrado = True

                if userEncontrado == True:
                    print("\nNão foi possível cadastrar o usuário no sistema. Tente novamente!")
                else:
                    with open (caminho , 'a') as arquivo:
                        arquivo.write(f"{user},{senha}\n")
                        print("Usuário foi salvo com sucesso!")
                    

    def logar(self, user, senha):
        userEncontrado = False

        with open (caminho, 'r') as arquivo:
            listaUsers = arquivo.readlines()
        
            for linha in listaUsers:
                if ((user in linha) and (senha in linha)):
                    userEncontrado = True

            if userEncontrado == True:
                return True
            else:
                return False

    def exibir(self):
            with open(caminho, 'r') as arquivo:
                print('\nUsuários do Sistema\n')
                for linha in arquivo:    
                    if linha.strip():        
                        user, senha = linha.strip().split(',')
                        print(f'UserName: {user}\nSenha: {senha}\n')

    def excluir(self, user): 
        with open (caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []

            for linha in linhas: 
                if user not in linha: 
                    linhasSalvas.append(linha)

        with open(caminho, 'w') as arquivo: 
            arquivo.writelines(linhasSalvas)
            print("\nUsuário excluído do sistema")

    def alterarUser(self, user):
        while True:
            opc = int(input("\nAlteração de Usuário\n\nInforme o que deseja alterar:\n\n1 - UserName\n2 - Senha\n"))

            if(opc == 1):
                userAlt = str(input("\nInforme o novo UserName do usuário: "))
                self.setUser(userAlt)

                with open(caminho, 'r') as arquivo:
                    linhas = arquivo.readlines()

                    linhasSalvas = []
                    usuarioEncontrado = False
                
                    for linha in linhas:
                        if user not in linha:
                            linhasSalvas.append(linha)
                        else:
                            usuarioEncontrado = True

                    if usuarioEncontrado == True:
                        with open (caminho, 'w') as arquivo:
                            arquivo.writelines(linhasSalvas)
                
                        with open (caminho, 'a') as arquivo:
                            arquivo.write(f"{self._user},{self._senha}")
                            print("UserName alterado com sucesso!")    
                    else:
                        print("\nUsuário não foi encontrado")
                        break

            elif(opc == 2):
                senhaAlt = str(input("\nInforme a nova senha do usuário: "))
                self.setSenha(senhaAlt)

                with open(caminho, 'r') as arquivo:
                    linhas = arquivo.readlines()

                    linhasSalvas = []
                    usuarioEncontrado = False
                
                    for linha in linhas:
                        if user not in linha:
                            linhasSalvas.append(linha)
                        else:
                            usuarioEncontrado = True

                    if usuarioEncontrado:
                        with open (caminho, 'w') as arquivo:
                            arquivo.writelines(linhasSalvas)
                
                        with open (caminho, 'a') as arquivo:
                            arquivo.write(f"{user},{senha}")
                            print("\nSenha alterada com sucesso!")    
                    else:
                        print("\nUsuário não foi encontrado")
                        break
            else:
                print("\nOpção inválida!")

            resp = str(input("\nDeseja realizar outra alteração? (sim/não)"))
            if(resp.lower() != "sim"):
                print("\nDados alterados\n\n")
                self.exibir()
                break