caminho = 'C:\\Users\\Thiago\\Desktop\\Projeto Mauricio\\panificadora_py\\database\\produto.txt'
class Produto:
    #nome = paof; valor = 0.25; validade = perecível\\não;  
    def __init__(self, id, nome, valor, unidade, validade):
        self._id = id
        self._nome = nome
        self._valor = valor
        self._unidade = unidade
        self._validade = validade
     
    def getId(self): 
        return self._id
    def getNome(self): 
        return self._nome
    def getValor(self):
        return self._valor
    def getUnidade(self):
        return self._unidade
    def getValidade(self):
        return self._validade
    
    def setId(self, id):
        self._id = id
    def setNome(self, nome):
        self._nome = nome
    def setValor(self, valor):
        self._valor = valor
    def setUnidade(self, unidade):
        self._unidade = unidade
    def setValidade(self, validade):
        self._unidade = validade

    def cadastrarProduto (self): # Cria função de cadastrar produto
        # o "open" abre o arquivo, o "with" serve para após fazermos o que precisamos no arquvio ele ser fechado corretamente. 
        # "caminho" é uma varíavel que guarda o Path do .txt, 'a' é o modo que o arquivo será aberto o "a" significa que será para adição
        # "as arquivo" serve parar falar que estou atribuindo o arquivo aberto na variável arquivo para manipular ele
        with open (caminho , 'a') as arquivo:
            # o "arquivo.write" serve para falar que vou escrever (por isso o write) dentro do .txt (representado pela varíavel arquivo)
            # a varável "self._nome", recebe o valor da váriavel nome que foi guardada num obejto da classe produto criado no cadastro 
            arquivo.write(f"{self._id},{self._nome},{self._valor},{self._unidade},{self._validade}")
            print("Produto foi cadastrado com sucesso!")
    @staticmethod
    def mostrarProdutos(): #Cria uma função para mostrar os prdutos no estoque
            # o open serve para abrir o arquivo, o "with" serve para depois que finalizarmos o arquivo seja fechado corretamente
            # "caminho" é a variável que contem o Path do arquvio .txt, e 'r' é o mode que ele será aebrto, "r" é modo de leitura
            # "as arquivo" serve para guardar o .txt na varável arquivo para podermos manipular ele  
            with open(caminho, 'r') as arquivo:
                print("Lista de Produtos:")
                # esse for vai percorrer cada linha do arquivo
                for linha in arquivo:
                    # pimeiro: o if serve para verificar se a linha após remover espaços não está vazia, caso não tenha isso o o código após pegar todas as linhas do arquivo com algo, tentaria ler a linha vazia a seguir, o que gera um erro
                    # segundo: linha.strip().split(','). O "strip()" vai retirar possíveis espaços em brancos no começo e no final 
                    # da string, o split vai separar a string em uma lista, usando a ',' como delimitador exemplo ["paoc","0.50", "20"]
                    # e após isso é atribuido as varáveis os elementos da lista na ordem.            
                    if linha.strip():        
                        nome, valor, unidade, validade = linha.strip().split(',')
                        print(f"ID: {id}, Nome: {nome}, Valor: {valor}, Unidade: {unidade}, Validade: {validade}")
    
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

    def alterarProduto(self, idE): # Primeiro foi feito como no método de exclusão, depois foi feito como no método de cadastro :)

        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []
            produtoEncontrado = False
        
            for linha in linhas:

                verificacao = linha.split(",")
                
                if idE != verificacao[0]:
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

