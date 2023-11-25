#from Usuario import Usuario
from Funcionario import Funcionario

print('\n\nPANIFICADORA\n')

# user = str(input('Usuário: '))
# senha = str(input('Senha: '))

# usuario = Usuario(user, senha)
# userEx = str(input("\nInforme qual usuário deseja alterar no sistema: "))
# usuario.alterarUser(userEx)
# verificado = usuario.logar(user, senha)

# funcionario = Funcionario("Lucas", "1234", "01", "Lucas Souza", "Entregador")
# funcionario = Funcionario("Vitoria", "6666", "02", "Vitória Lima", "Atentende")
# funcionario = Funcionario("João", "8888", "03", "João Lucas", "Caixa")
funcionario = Funcionario("Geral", "5555", "Gerailda", "04", "Vendedora")
id = (input("\nInforme o id do funcionário que deseja alterar: "))
funcionario.alterarFunc(id)

# if(verificado == True):
#     #os.system("cls")
#     print('\nBem-vindo ao Sistema\n')
#     while True:
#         print('\nPANIFICADORA\n')
#         print('\nSelecione a opção desejada:\n\n1 - Produtos\n2 - Funcionários\n3 - Vendas\n')
#         opcaoMenuPrinc = int(input())
        
#         if(opcaoMenuPrinc == 1):
#             print('\nGestão de Produtos\n')
#             print('\n1 - Cadastrar Novo Produto\n2 - Alterar Dados do Produto\n3 - Visualizar Estoque\n4 - Atualizar estoque')
#             opcaoMenuProd = int(input())

#             if(opcaoMenuProd  == 1):
#                 print('cadastro de produtos')
#             elif(opcaoMenuProd == 2):
#                 print('alteracao de produtos')
#             elif(opcaoMenuProd  == 3):
#                print('visualizar produtos')
#             elif(opcaoMenuProd  == 4):
#                 print('atualizar estoque')
#             else:
#                 print('\nOpção inválida')

#         if(opcaoMenuPrinc == 2):
#             print('\nGestão de Funcionários\n')
#             print('\n1 - Cadastrar Novo Funcionário\n2 - Alterar Dados do Funcionário\n3 - Visualizar Funcionários')
#             opcaoMenuFunc = int(input())

#             if(opcaoMenuFunc == 1):
#                 print('cadastro de funcionário')
#             elif(opcaoMenuFunc == 2):
#                 print('alteracao de funcionarios')
#             elif(opcaoMenuFunc == 3):
#                print('visualizar funcionários')
#             else:
#                 print('\nOpção inválida')

#         if(opcaoMenuPrinc == 3):
#             print('\nGestão de Vendas\n')
#             print('\n1 - Caixa\n2 - Atualizar Estoque\n3 - Visualizar Estoque')
#             opcaoMenuVend = int(input())

#             if(opcaoMenuVend == 1):
#                 print('cadastro de produtos')
#             elif( opcaoMenuVend == 2):
#                 print('atualizar estoque')
#             elif(opcaoMenuVend == 2):
#                 print('visualizar estoque')
#             else:
#                 print('\nOpção inválida')

#         resp = str(input('\nDeseja realizar outra operação? (sim/não)'))
#         if (resp.lower() == "nao" or resp.lower() == "não"):
#             print('\nSistema fechado!\n')
#             break
# else:
#     print('\nUsuário e/ou senha inválidos!')