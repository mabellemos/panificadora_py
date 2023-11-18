caminho = 'C:\\Users\\Thiago\\Desktop\\Projeto Mauricio\\panificadora_py\\database\\materia.txt'
class Materia:
    def __init__(self, nome, quantidade, fornecedor):
        self._nome = nome
        self._quantidade = quantidade
        self._fornecedor = fornecedor

    def getNome(self):
        return self._nome
    def getQuantidade(self):
        return self._quantidade
    def getFornecedor(self):
        return self._fornecedor
        
    def setNome(self, nome):
        self._nome = nome
    def setQuantidade(self, quantidade):
        self._quantidade = quantidade
    def setFornecedor(self, fornecedor):
        self._fornecedor = fornecedor
        
    def cadastrarMateria(self):
        with open (caminho, 'a') as arquivo:
            arquivo.write(f"{self._nome},{self._quantidade},{self._fornecedor}")
            print("Materia cadastrada com sucesso")

    @staticmethod
    def mostrarMateria():
        with open (caminho, 'r') as arquivo:
            print("Lista de Matéria Prima")
            for linha in arquivo:
                if linha.strip():
                    nome, quantidade, fornecedor = linha.strip().split(',')
                    print(f"Nome: {nome}, Quantidade: {quantidade} kg, Fornecedor: {fornecedor}")
    
    @staticmethod
    def excluirProduto(nome):
        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []

            for linha in linhas: 
                if nome not in linha:
                    linhasSalvas.append(linha)
        
        with open (caminho, 'w') as arquivo:
            arquivo.writelines(linhasSalvas)

    def alterarMateria(self, nomeE):

        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            linhasSalvas = []
            materiaEncontrado = False

            for linha in linhas:

                verificação = linha.split(',')

                if nomeE != verificação[0]:
                    linhasSalvas.append(linha)
                else:
                    materiaEncontrado = True

            if materiaEncontrado:
                with open (caminho, 'w') as arquivo:
                    arquivo.writelines(linhasSalvas)

                with open (caminho, 'a') as arquivo:
                    arquivo.write(f"\n{self._nome},{self._quantidade},{self._fornecedor}")
                    print("Máteria prima foi alterado com sucesso!")
            else:
                print("Matéria prima não foi achado")
