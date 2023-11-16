from Produto import Produto

condicao = True

while condicao:
    print ("Adicione os parâmetros do produto\n")
    nome = input("Adicione o nome: ")
    valor = float(input("\nAdicione o preço: "))
    unidade = int(input("\nAdicione as unidades: "))
    validade = input("\nAdicione a validade: ")

    produto = Produto(nome, unidade, valor, validade)
    produto.cadastrarProduto()

    alternativa = input("Deseja continuar adicionando produtos?(s/n)")

    if alternativa.lower() == "n":
        condicao = False

# while condicao:
#     print ("Qual o nome do produto que vc pretende excluir:\n")
#     nome = input("\nAdicione o nome: ")

#     Produto.excluirProduto(nome)

#     alternativa = input("Deseja continuar excluindo produtos?(s/n)")

#     if alternativa.lower() == "n":
#         condicao = False

# print("Fim do código")

# Produto.mostrarProdutos()

# while condicao: 
#     nomeE = input("Qual o produto que você deseja alterar: ")
#     print("Adicione os novos valores\n")
#     nome = input("Adicione o nome: ")
#     valor = float(input("\nAdicione o valor: "))
#     unidade = int(input("\nAdicione a unidade: "))
#     validade = input("\nQual o tipo da validade: ")

#     produto = Produto(nome, valor, unidade, validade)
#     produto.alterarProduto(nomeE)

#     alternativa = input("Deseja continuar adicionando produtos?(s/n)")
#     if alternativa.lower() == "n":
#         condicao = False