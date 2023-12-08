caminho = "database//funcionarios.txt"

from functions.Usuario import Usuario

class Funcionario ():
    def __init__ (self, id, nome, funcao):
        # super().__init__(user, senha)
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

    def salvar(self):
        # super().salvar(user, senha)
        funcEncontrado = False

        with open (caminho , 'r') as arquivo:
            linhas = arquivo.readlines()

            if (len(linhas) == 0):
                with open (caminho , 'a') as arquivo:
                    arquivo.write(f"\n{self._id},{self._nome},{self._funcao}\n")
                    print("Funcionário foi salvo com sucesso!")
            else:
                for linha in linhas:
                    if self._id in linha:
                       funcEncontrado = True

                if funcEncontrado == True:
                    print("\nNão foi possível cadastrar o funcionário no sistema. Tente novamente!")
                else:
                    with open (caminho , 'a') as arquivo:
                        arquivo.write(f"\n{self._id},{self._nome},{self._funcao}\n")
                        print("Funcionário foi salvo com sucesso!")

    def exibir():
            with open(caminho, 'r') as arquivo:
                print('\nFuncionários do Sistema\n')
                # super().exibir()
                for linha in arquivo:    
                    if linha.strip():        
                        id, nome, funcao = linha.strip().split(',')
                        print(f"\nID: {id}\nNome: {nome}\nFunção: {funcao}\n")

    def excluir(self, id): 
        with open (caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = [] 

            for linha in linhas: 
                if id not in linha: 
                    linhasSalvas.append(linha)

        with open(caminho, 'w') as arquivo: 
            arquivo.writelines(linhasSalvas)
            print("\nFuncionário excluído do sistema!")

    def alterarFunc(id):
        opc = int(input("\nAlteração de Dados do Funcionário\n\nInforme a informação a ser alterada:\n\n1 - Nome\n2 - Função\n"))

        if(opc == 1):
            novoNome = str(input("\nInforme o novo nome do funcionário: "))

            with open(caminho, 'r') as arquivo:
                linhas = arquivo.readlines()

                linhasSalvas = []
                funcEncontrado = False
            
                for linha in linhas:

                    verifcação = linha.split(",")

                    if id.strip() != verifcação[0].strip():
                        linhasSalvas.append(linha)
                    else:
                        funcEncontrado = True
                        verifcação[1] = novoNome
                        novaLinha = ','.join(verifcação)
                        
                if funcEncontrado:
                    with open (caminho, 'w') as arquivo:
                        arquivo.writelines(linhasSalvas)                                    
                        print("\nNome alterado com sucesso!")

                    with open (caminho, 'a') as arquivo:
                        arquivo.write(f"\n{novaLinha}")
                        print("\nFunção alterada com sucesso!")  
                else:
                    print("\nFuncionário não foi encontrado")

        elif(opc == 2):
            novaFuncao = str(input("\nInforme a nova função do funcionário: "))

            with open(caminho, 'r') as arquivo:
                linhas = arquivo.readlines()

                linhasSalvas = []
                funcEncontrado = False
            
                for linha in linhas:

                    verifcação = linha.split(",")

                    if id.strip() != verifcação[0].strip():
                        linhasSalvas.append(linha)
                    else:
                        funcEncontrado = True
                        verifcação[2] = novaFuncao
                        novaLinha = ','.join(verifcação)

                if funcEncontrado:
                    with open (caminho, 'w') as arquivo:
                        arquivo.writelines(linhasSalvas)
            
                    with open (caminho, 'a') as arquivo:
                        arquivo.write(f"\n{novaLinha}")
                        print("\nFunção alterada com sucesso!")  
                else:
                    print("\nFuncionário não foi encontrado")
        else:
            print("\nOpção inválida!")