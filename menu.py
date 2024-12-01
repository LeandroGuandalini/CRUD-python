def exibir_menu():  
  """
  Exibe o menu de opções disponíveis para o usuário.
  
  O menu inclui as seguintes opções:
  - Sair
  - Adicionar produto
  - Atualizar estoque
  - Listar produtos
  - Buscar produtos
  - Remover produtos
  - Ordenar produtos
  - Exibir produtos esgotados
  - Listar produtos com estoque baixo
  - Atualizar preços de venda
  - Calcular valor do estoque
  - Calcular lucro do estoque
  - Gerar relatório
  
  A função não recebe parâmetros e não retorna valores.
  """
  print('\nBem vindo ao sistema de produtos! ')
  print('[0] - Sair ')
  print('[1] - Adicionar produto ')
  print('[2] - Atualizar estoque ')
  print('[3] - Listar produtos ')
  print('[4] - Buscar produtos ')
  print('[5] - Remover produtos ')
  print('[6] - Ordenar produtos ')
  print('[7] - Exibir produtos esgotados ')
  print('[8] - Listar produtos com estoque baixo ')
  print('[9] - Atualizar preços de venda ')
  print('[10] - Calcular valor do estoque ')
  print('[11] - Calcular lucro do estoque ')
  print('[12] - Gerar relatório ')

def entrar_opcao():
  """
  Exibe o menu e aguarda o usuário inserir uma opção válida.
  
  A função chama a função `exibir_menu` para exibir as opções e então solicita
  que o usuário insira uma opção. Caso a entrada não seja válida (não seja um número
  inteiro ou esteja fora do intervalo de opções), a função exibirá uma mensagem de erro
  e continuará pedindo a entrada até receber uma opção válida.
  
  Retorna:
      int: A opção escolhida pelo usuário (um número inteiro entre 0 e 12).
  """
  while True:
    exibir_menu()
    opcao = input('\nQual ação deseja realizar? ')
    if opcao.isdigit() and (int(opcao) in range(13)):
      return int(opcao)
    else:
      print("\nErro: opção inválida. Tente novamente.")

