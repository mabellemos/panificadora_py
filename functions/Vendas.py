caminho = "database/produto.txt"

from functions.Produto import Produto
from functions.Funcionario import Funcionario

class Vendas:
    def __init__(self, produto, funcionario):
        self._produto = Produto()
        self._funcionario = Funcionario()

    #Métodos sets e gets
    def getProduto(self):
        return self._produto

    def setProduto(self, produto):
        self._produto = produto

    def getFuncionario(self):
        return self._produto

    def setFuncionario(self, funcionario):
        self._funcionario = funcionario

    def getValorFinal(self):
        return self._valorFinal

    def setValorFinal(self, valorFinal):
        self._valorFinal = valorFinal

    #Métodos da classe Vendas
    # def atualizarEstoque(produtoId, quantidade):
    #     with open(caminho, 'r') as arquivo:
    #         linhas = arquivo.readlines()

    #         for linha in linhas:
    #             if id in linha:
    #                 produto.getProduto().setQuantidade(novaQuant)

    #                 print(f"\nEstoque do produto {produto.getProduto().getId()} atualizado!")
    #                 produto.mostrarProdutos()

    def formaPagamento(self, valorFinal):
        opc = int(input("\nEscolha a forma de pagamento:\n1 - Cartão\n2 - Dinheiro3 - Pix/Outros\n"))

        if(opc == 1):
            return valorFinal + (valorFinal*0.5)
        elif(opc == 2):
            return valorFinal - (valorFinal*0.5)
        elif(opc == 3):
            return valorFinal
        else:
            print("\nOpção inválida!")

    def vender():

        valorFinal = 0

        while True:
            print("\n----CAIXA----\n")
            funcId = str(input("\nID funcionário: "))
            prodNome = str(input("\nInforme o nome do produto que deseja realizar a venda: "))
            quant = int(input("\nQuantidade: "))

            with open(caminho, 'r') as arquivo:
                linhas = arquivo.readlines()

            linhasSalvas = []
            produtoEncontrado = False

            for linha in linhas:
                verificacao = linha.split(",")
 
                if prodNome.strip() != verificacao[0].strip():
                    linhasSalvas.append(linha)
                else:
                    produtoEncontrado = True
                    verificacao[2] = str(int(verificacao[2]) - quant)
                    valorFinal = valorFinal + (quant*float(verificacao[1]))
                    novaLinha = ','.join(verificacao)

            if produtoEncontrado:
                with open (caminho, 'w') as arquivo:
                    arquivo.writelines(linhasSalvas)                                    
                    print(f"\nEstoque do produto atualizado!")
                with open (caminho, 'a') as arquivo:
                    arquivo.write(f"\n{novaLinha}")

            print(f"\nCOMPRA\nTotal = {valorFinal}")

            resp = str(input("\nFinalizar compra? (sim/não)"))

            if (resp.lower() == "sim"):
                break
                formaPagamento(valorFinal)
    
    