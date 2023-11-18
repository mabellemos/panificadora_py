from Materia import Materia



condicao = True

Materia.mostrarMateria()

# while condicao:
#     print ("Adicione os parâmetros da materia\n")
#     nome = input("Adicione o nome: ")
#     quantidade = float(input("\nAdicione a quantidade em kg: "))
#     fornecedor = input("\nAdicione o fornecedor : ")

#     materia = Materia(nome, quantidade, fornecedor)
#     materia.cadastrarMateria()

#     alternativa = input("Deseja continuar adicionando produtos?(s/n)")

#     if alternativa.lower() == "n":
#         condicao = False    

# while condicao:
#     print ("Qual o nome do produto que vc pretende excluir:\n")
#     nome = input("\nAdicione o nome: ")

#     Materia.excluirProduto(nome)

#     alternativa = input("Deseja continuar excluindo produtos?(s/n)")

#     if alternativa.lower() == "n":
#         condicao = False

while condicao: 
    nomeE = input("Qual o produto que você deseja alterar: ")
    print("Adicione os novos valores\n")
    nome = input("Adicione o nome: ")
    quantidade = float(input("\nAdicione o valor: "))
    fornecedor = input("\nQual o tipo da validade: ")

    materia = Materia(nome, quantidade, fornecedor)
    materia.alterarMateria(nomeE)

    alternativa = input("Deseja continuar adicionando produtos?(s/n)")
    if alternativa.lower() == "n":
        condicao = False