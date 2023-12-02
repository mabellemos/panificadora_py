#Importação das classes
from Usuario import Usuario
from Vendas import Vendas
from Produto import Produto
from Funcionario import Funcionario

#Arrays
produtos = []
funcionarios = []
vendas = []

#Entrada no sistema por autenticação
# print('\n\nPANIFICADORA\n')

# user = str(input('Usuário: '))
# senha = str(input('Senha: '))

# usuario = Usuario(user, senha)
# verificado = usuario.logar(user, senha)
verificado = True
if(verificado == True):
    print('\nBem-vindo ao Sistema\n')
    while True:
        print('\nPANIFICADORA\n')
        print('\nSelecione a opção desejada:\n\n1 - Produtos\n2 - Funcionários\n3 - Vendas\n')
        opcaoMenuPrinc = int(input())
        
        if(opcaoMenuPrinc == 1):
            print('\nGestão de Produtos\n')
            print('\n1 - Cadastrar Novo Produto\n2 - Alterar Dados do Produto\n3 - Visualizar Estoque\n4 - Sair')
            opcaoMenuProd = int(input())

            if(opcaoMenuProd  == 1):
                numP = int(input("\nInforme quantos produtos deseja cadastrar: "))
                print("\nCADASTRO DE PRODUTOS\n")
                for i in range(numP):
                    objProdutos = Produto()

                    # dic = {
                    #     "id": objProdutos.getId(),
                    #     "nome": objProdutos.getNome(),
                    #     "valor": objProdutos.getValor(),
                    #     "unidade": objProdutos.getUnidade(),
                    #     "validade": objProdutos.getValidade()
                    # }
                    

                    objProdutos.cadastrarProduto()
                    produtos.append(objProdutos)
            elif(opcaoMenuProd == 2):
                idP = int(input("\nInforme o ID do produto que deseja alterar: "))
                
                for i in range(len(produtos)):
                    if (produtos[i].getId() == idP):
                        nome = str(input("\nInforme o novo nome do produto: "))
                        valor = float(input("\nInforme o novo valor do produto: "))
                        unidade = str(input("\nInforme a nova unidade do produto: "))
                        validade = str(input("\nInforme a nova validade do produto: "))
                         
                        produtos[i].setNome(nome)
                        produtos[i].setValor(valor)
                        produtos[i].setUnidade(unidade)
                        produtos[i].setValidade(validade)

                        produtos[i].alterarProduto(idP)
            elif(opcaoMenuProd  == 3):
                for i in range(len(produtos)):
                    produtos[i].mostrarProdutos()
            elif(opcaoMenuProd  == 4):
                break
            else:
                print('\nOpção inválida')

        if(opcaoMenuPrinc == 2):
            print('\nGestão de Funcionários\n')
            print('\n1 - Cadastrar Novo Funcionário\n2 - Alterar Dados do Funcionário\n3 - Visualizar Funcionários')
            opcaoMenuFunc = int(input())

            if(opcaoMenuFunc == 1):
                quantF = int(input("\nInforme a quantidade de funcionários que deseja cadastrar: "))

                for i in range(quantF):
                    funcionarios.append(objFuncionarios.salvar())
            elif(opcaoMenuFunc == 2):
                funcionarios.append(objFuncionariosalterarFunc())
            elif(opcaoMenuFunc == 3):
                funcionarios.append(objFuncionarios.exibir())
            else:
                print('\nOpção inválida')

        if(opcaoMenuPrinc == 3):
            print('\nGestão de Vendas\n')
            print('\n1 - Caixa\n2 - Atualizar Estoque\n3 - Visualizar Estoque')
            opcaoMenuVend = int(input())

            if(opcaoMenuVend == 1):
                vendas.append(objVendas.vender())
            elif( opcaoMenuVend == 2):
                vendas.append(objVendas.atualizarEstoque())
            elif(opcaoMenuVend == 2):
                produtos.append(objProdutos.mostrarProdutos())
            else:
                print('\nOpção inválida')

        resp = str(input('\nDeseja realizar outra operação? (sim/não)'))
        if (resp.lower() == "nao" or resp.lower() == "não"):
            print('\nSistema fechado!\n')
            break
else:
    print('\nUsuário e/ou senha inválidos!')