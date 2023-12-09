from functions.Funcionario import Funcionario
from functions.Usuario import Usuario
from functions.Produto import Produto
from functions.Vendas import Vendas

# Menus 

def MenuPrincipal():
    print('\nSelecione a opção desejada:\n\n1 - Produtos\n2 - Funcionários\n3 - Vendas\n')
    opcaoMenuPrinc = int(input())
    if(opcaoMenuPrinc == 1):
        MenuDeProduto()
    elif(opcaoMenuPrinc == 2):
        MenuDeFuncionario()
    elif(opcaoMenuPrinc == 3):
        menuVendas()

def MenuDeProduto():

    condicao = True

    print("\n--------Menu de Produtos-------\n")
    print('\n1 - Cadastrar Novo Produto\n2 - Alterar Dados do Produto\n3 - Visualizar Estoque\n4 - Sair\n')
    opcaoMenuProd = int(input())

    if(opcaoMenuProd == 1):
        while condicao:

            print ("\nAdicione os parâmetros do produto\n")
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

    print("\nMenu de Funcionários")
    print('\n1 - Cadastrar Novo Funcionário\n2 - Alterar Dados do Funcionário\n3 - Visualizar Funcionários\n4 - Sair')
    opcaoMenuFunc = int(input())

    if(opcaoMenuFunc ==1 ):
        print("Adicione os dados do funcionário\n")
        id = (input("\nAdicionar o id do funcionário:"))
        nome = input("\nAdicione o nome do funcionário:")
        func = input("\nAdicione o a função do funcionário:")
        funcionario = Funcionario(id, nome, func)
        funcionario.salvar()
    elif(opcaoMenuFunc == 2):
        id = (input("\nInforme o ID do funcionário que deseja alterar: "))
        Funcionario.alterarFunc(id)
        MenuDeFuncionario()
    elif(opcaoMenuFunc == 3):
        Funcionario.exibir()
        MenuDeFuncionario()
    elif(opcaoMenuFunc == 4):
        MenuPrincipal()

def menuVendas():
    while True:
      
        Vendas.vender()
      
        resp = str(input("\nDeseja realizar outra opção? (sim/não)\n"))
        if (resp.lower() == 'nao'):
            break
# Código

print('\n\n--------PANIFICADORA--------\n')


user = str(input('Usuário: '))
senha = str(input('Senha: '))

usuario = Usuario(user, senha)
verificado = usuario.logar(user, senha)

if(verificado == True):
    print('\nBem-vindo ao Sistema\n')

    MenuPrincipal()
else:
    print("\nNão foi possível entrar no sistema. Tente Novamente!\n")