def exibir_menu():  
  print('\nBem vindo ao sistema de produtos! ')
  print('[0] - Sair ')
  print('[1] - Adicionar produto ')
  print('[2] - Atualizar produto ')
  print('[3] - Listar produtos ')
  print('[4] - Buscar produtos ')
  print('[5] - Remover produtos ')
  print('[6] - Ordenar produtos ')

def entrar_opcao():
  while True:
    exibir_menu()
    opcao = input('\nQual ação deseja realizar? ')
    if opcao.isdigit() and int(opcao) in range(7):
      return int(opcao)
    else:
      print("\nErro: opção inválida. Tente novamente.")

