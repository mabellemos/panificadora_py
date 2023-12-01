from Produto import Produto
from Funcionario import Funcionario

class Vendas:
    def __init__(self, produto, funcionario, valorFinal):
        self._produto = Produto()
        self._funcionario = Funcionario()
        self._valorFinal = 0

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
    def atualizarEstoque(self, produtoId, quantidade):
        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                if id in linha:
                    produto.getProduto().setQuantidade(novaQuant)

                    print(f"\nEstoque do produto {produto.getProduto().getId()} atualizado!")
                    produto.mostrarProdutos()

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

    def vender(self, produto):
        while True:
            print("\nVENDAS\n")
            funcId = str(input("\nID funcionário: "))
            prodId = str(input("\nInforme o id do produto que deseja realizar a venda: "))
            quant = int(input("\nQuantidade: "))

            atualizarEstoque(prodId, quant)

            valorFinal = valorFinal + (quant*produto.getProduto().getValor())

            print(f"\nCOMPRA\nTotal = {valorFinal}")

            resp = str(input("\nFinalizar compra? (sim/não)"))

            if (resp.lower() == "sim"):
                break
                formaPagamento(valorFinal)
    
    