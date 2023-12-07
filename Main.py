# #Importação das classes
# from Usuario import Usuario
# from Vendas import Vendas
# from Produto import Produto
# from Funcionario import Funcionario

# #Arrays
# produtos = []
# funcionarios = []
# vendas = []

# #Instanciamento dos objetos
# objProdutos = Produtos()
# objVendas = Vendas()
# objFuncionarios = Funcionarios()

# #Entrada no sistema por autenticação
# print('\n\nPANIFICADORA\n')

# user = str(input('Usuário: '))
# senha = str(input('Senha: '))

# usuario = Usuario(user, senha)
# verificado = usuario.logar(user, senha)

# if(verificado == True):
#     print('\nBem-vindo ao Sistema\n')
#     while True:
#         print('\nPANIFICADORA\n')
#         print('\nSelecione a opção desejada:\n\n1 - Produtos\n2 - Funcionários\n3 - Vendas\n')
#         opcaoMenuPrinc = int(input())
        
#         if(opcaoMenuPrinc == 1):
#             print('\nGestão de Produtos\n')
#             print('\n1 - Cadastrar Novo Produto\n2 - Alterar Dados do Produto\n3 - Visualizar Estoque\n4 - Sair')
#             opcaoMenuProd = int(input())

#             if(opcaoMenuProd  == 1):
#                 numP = int(input("\nInforme quantos produtos deseja cadastrar: "))

#                 for i in range(numP):
#                     produtos.append(objProdutos.cadastrarProdutos())

#             elif(opcaoMenuProd == 2):
#                 idP = int(input("\nInforme o ID do produto que deseja alterar: "))
#                 produtos.append(objProdutos.alterarProduto(id))
#             elif(opcaoMenuProd  == 3):
#                 produtos.append(objProdutos.mostrarProdutos())
#             elif(opcaoMenuProd  == 4):
#                 break
#             else:
#                 print('\nOpção inválida')

#         if(opcaoMenuPrinc == 2):
#             print('\nGestão de Funcionários\n')
#             print('\n1 - Cadastrar Novo Funcionário\n2 - Alterar Dados do Funcionário\n3 - Visualizar Funcionários')
#             opcaoMenuFunc = int(input())

#             if(opcaoMenuFunc == 1):
#                 quantF = int(input("\nInforme a quantidade de funcionários que deseja cadastrar: "))

#                 for i in range(quantF):
#                     funcionarios.append(objFuncionarios.salvar())
#             elif(opcaoMenuFunc == 2):
#                 funcionarios.append(objFuncionariosalterarFunc())
#             elif(opcaoMenuFunc == 3):
#                 funcionarios.append(objFuncionarios.exibir())
#             else:
#                 print('\nOpção inválida')

#         if(opcaoMenuPrinc == 3):
#             print('\nGestão de Vendas\n')
#             print('\n1 - Caixa\n2 - Atualizar Estoque\n3 - Visualizar Estoque')
#             opcaoMenuVend = int(input())

#             if(opcaoMenuVend == 1):
#                 vendas.append(objVendas.vender())
#             elif( opcaoMenuVend == 2):
#                 vendas.append(objVendas.atualizarEstoque())
#             elif(opcaoMenuVend == 2):
#                 produtos.append(objProdutos.mostrarProdutos())
#             else:
#                 print('\nOpção inválida')

#         resp = str(input('\nDeseja realizar outra operação? (sim/não)'))
#         if (resp.lower() == "nao" or resp.lower() == "não"):
#             print('\nSistema fechado!\n')
#             break
# else:
#     print('\nUsuário e/ou senha inválidos!')

#Entrada no sistema por autenticação

# Imports

from Funcionario import Funcionario
from Usuario import Usuario
from functions.Produto import Produto

# Menus 

def MenuPrincipal():
    print('\nSelecione a opção desejada:\n\n1 - Produtos\n2 - Funcionários\n3 - Vendas\n')
    opcaoMenuPrinc = int(input())
    if(opcaoMenuPrinc == 1):
        MenuDeProduto()
    elif(opcaoMenuPrinc == 2):
        MenuDeFuncionario()
    elif(opcaoMenuPrinc == 3):
        print("\nMenu de Vendas: ")

def MenuDeProduto():

    condicao = True

    print("\nMenu de Produtos")
    print('\n1 - Cadastrar Novo Produto\n2 - Alterar Dados do Produto\n3 - Visualizar Estoque\n4 - Sair')
    opcaoMenuProd = int(input())

    if(opcaoMenuProd == 1):
        while condicao:

            print ("Adicione os parâmetros do produto\n")
            nome = input("Adicione o nome:")
            valor = float(input("\nAdicione o preço:"))
            unidade = int(input("\nAdicione as unidades:"))
            validade = input("\nAdicione a validade:")

            produto = Produto(nome, unidade, valor, validade)
            produto.cadastrarProduto()

            alternativa = input("\nDeseja continuar adicionando produtos?(s/n): ")

            if alternativa.lower() == "n":
                condicao = False
        MenuPrincipal()    
    elif(opcaoMenuProd == 2):
        while condicao: 
            nomeE = input("Qual o produto que você deseja alterar:")
            print("Adicione os novos valores\n")
            nome = input("\nAdicione o nome:")
            valor = float(input("\nAdicione o valor:"))
            unidade = int(input("\nAdicione a unidade:"))
            validade = input("\nQual o tipo da validade:")

            produto = Produto(nome, valor, unidade, validade)
            produto.alterarProduto(nomeE)

            alternativa = input("Deseja continuar adicionando produtos?(s/n)")
            if alternativa.lower() == "n":
                condicao = False
        MenuDeProduto()      
    elif(opcaoMenuProd == 3):
         Produto.mostrarProdutos()
         MenuDeProduto()
    elif(opcaoMenuProd == 4):
        MenuPrincipal()

def MenuDeFuncionario():    
    # condicao = True

    print("\nMenu de Funcionários")
    print('\n1 - Cadastrar Novo Funcionário\n2 - Alterar Dados do Funcionário\n3 - Visualizar Funcionários\n4 - Sair')
    opcaoMenuFunc = int(input())

    if(opcaoMenuFunc ==1 ):
        quantF = int(input("\nInforme a quantidade de funcionários que deseja cadastrar: "))
        for i in range(quantF):
            funcionarios.append(objFuncionarios.salvar())
    elif(opcaoMenuFunc == 2):
        id = (input("\nInforme o ID do funcionário que deseja alterar: "))
        Funcionario.alterarFunc(id)
    elif(opcaoMenuFunc == 3):
        Funcionario.exibir()
    elif(opcaoMenuFunc == 4):
        MenuPrincipal()

# Código

print('\n\n--------PANIFICADORA--------\n')

user = str(input('Usuário: '))
senha = str(input('Senha: '))

usuario = Usuario(user, senha)
verificado = usuario.logar(user, senha)

if(verificado == True):
    print('\nBem-vindo ao Sistema\n')

    MenuPrincipal()




