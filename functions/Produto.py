caminho = 'database/produto.txt'

class Produto:
    def __init__(self, nome, valor, unidade, validade):
        self._nome = nome
        self._valor = valor
        self._unidade = unidade
        self._validade = validade
     
    def getNome(self): 
        return self._nome
    def getValor(self):
        return self._valor
    def getUnidade(self):
        return self._unidade
    def getValidade(self):
        return self._validade
    
    def setNome(self, nome):
        self._nome = nome
    def setValor(self, valor):
        self._valor = valor
    def setUnidade(self, unidade):
        self._unidade = unidade
    def setValidade(self, validade):
        self._unidade = validade

    def cadastrarProduto (self): 
        with open (caminho , 'a') as arquivo: 
            arquivo.write(f"\n{self._nome},{self._valor},{self._unidade},{self._validade}")
            print("\nProduto foi cadastrado com sucesso!")
    @staticmethod
    def mostrarProdutos(): 
            with open(caminho, 'r') as arquivo:
                print("Lista de Produtos:")
                for linha in arquivo:        
                    if linha.strip():        
                        nome, valor, unidade, validade = linha.strip().split(',')
                        print(f"Nome: {nome}, Valor: {valor}, Unidade: {unidade}, Validade: {validade}")
    
    @staticmethod # Botei esse método como estático, pois ele não precisa da classe para funcionar
    def excluirProduto(id): #cria o método e passa o nome como parâmetro
        with open (caminho, 'r') as arquivo: # abre o arquivo, específica o caminho, o tipo de leitura que será feita e atríbui o .txt a uma variável
            linhas = arquivo.readlines() # atríbui a variável "linhas" os as linhas que estão dentro de arquivo

            linhasSalvas = [] # cria uma lista para salvar as linahs que não serão excluídas

            for linha in linhas: # intera a varável "linha" com "linhas"
                if id not in linha: # verifica se a variável nome que foi passada como parâmetro está presente na linha iterada
                    linhasSalvas.append(linha) # se nome não estiver presente adiciona a linha a lista criada anteriormente

        with open(caminho, 'w') as arquivo: # abre o arquivo em mode de escrita
            arquivo.writelines(linhasSalvas) # escreve no arquivo as linhas salvas na lista 

    def alterarProduto(self, nomeE): # Primeiro foi feito como no método de exclusão, depois foi feito como no método de cadastro :)

        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []
            produtoEncontrado = False

            for linha in linhas:

                verificacao = linha.split(",")
 
                if nomeE.strip() != verificacao[0].strip():
                    linhasSalvas.append(linha)
                else:
                    produtoEncontrado = True

            if produtoEncontrado:

                with open (caminho, 'w') as arquivo:
                    arquivo.writelines(linhasSalvas)

                with open (caminho, 'a') as arquivo:
                    arquivo.write(f"\n{self._nome},{self._valor},{self._unidade},{self._validade}")
                    print("Produto foi alterado com sucesso!")    
            else:
                print("Produto não foi encontrado")                    

