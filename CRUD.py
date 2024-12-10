from menu import *
from validacoes import *

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

estoque = validar_estoque_inicial(estoque_inicial)

def cadastrar_produtos():
  """
  Cadastra novos produtos no estoque.
  Solicita ao usuário a descrição, código, quantidade, custo e preço de venda do produto.
  Verifica se o código já existe no estoque antes de cadastrar.
  Retorna ao menu principal quando o usuário digita "fim".
  """
  while True:
    descricao = input('Informe o produto a ser cadastrado (escreva "fim" para terminar): ').lower()
    if descricao in ["fim", ""]:
      break
    
    codigo = validar_entrada('int', 'Informe o código do produto: ', 'Código deve ser um número inteiro.')
    if any(p['codigo'] == codigo for p in estoque):
      print("Erro: Já existe um produto com esse código. Tente novamente.")
      continue
    
    quantidade_estoque = validar_entrada('int', 'Informe a quantidade em estoque do produto: ', 'Quantidade não informada ou inválida.')
    custo = validar_entrada('float', 'Informe o custo do produto: ', 'Custo deve ser um número real.')
    preco_venda = validar_entrada('float', 'Informe o preço de venda do produto: ', 'Preço de venda deve ser um número real.')
    
    produto = {
      'descricao': descricao,
      'codigo': codigo,
      'quantidade_estoque': quantidade_estoque,
      'custo': custo,
      'preco_venda': preco_venda
    }
    
    estoque.append(produto)

def listar_produtos():
  """
  Lista todos os produtos cadastrados no estoque.
  Exibe os campos: descrição, código, quantidade, custo e preço de venda em formato tabular.
  Retorna uma mensagem indicando que não há produtos caso o estoque esteja vazio.
  """
  if not estoque:
    print("Nenhum produto cadastrado.")
    return
  
  print(f"{'Descrição'.ljust(30)}{'Código'.ljust(10)}{'Quantidade'.ljust(12)}{'Custo'.ljust(10)}{'Preço de Venda'.ljust(15)}")
  print("-" * 90)
  
  for i in estoque:
    print(f"{i['descricao'].ljust(30)}{str(i['codigo']).ljust(10)}{str(i['quantidade_estoque']).ljust(12)}{str(i['custo']).ljust(10)}{str(i['preco_venda']).ljust(15)}")

def ordenar_estoque():
  """
  Ordena o estoque com base na quantidade em ordem crescente ou decrescente.
  Solicita ao usuário o tipo de ordenação desejada.
  Lista os produtos após a ordenação.
  """
  while True:  
    ordem = input('Qual ordem você gostaria: crescente ou decrescente? ').lower()
    if ordem == 'crescente':
      estoque_ordenado = sorted(estoque, key=lambda x: x['quantidade_estoque'])
      break
    elif ordem == 'decrescente':
      estoque_ordenado = sorted(estoque, key=lambda x: x['quantidade_estoque'], reverse=True)
      break
    else:
      print("Opção de ordenação inválida! Escolha 'crescente' ou 'decrescente'.")
      continue 
    
  listar_produtos(estoque_ordenado)

def buscar_produtos(user):
  """
  Busca produtos no estoque por código ou descrição.
  
  Parâmetros:
  - user (str): Código ou descrição do produto fornecido pelo usuário.
  
  Retorna:
  - Exibe os produtos encontrados ou uma mensagem indicando que não foram encontrados.
  """
  produto_encontrado = False 
  
  if user.isdigit():
    user = int(user)
    for produto in estoque:
      if user == produto['codigo']:
        print(produto)
        produto_encontrado = True
        
  else:
    user = user.lower()
    for produto in estoque:
      if user in produto['descricao']: 
        print(produto)
        produto_encontrado = True
        
  if not produto_encontrado:
      print('Nenhum produto encontrado com o código fornecido.')
  

def remover_produtos():
  """
  Remove produtos do estoque pelo código.
  Solicita ao usuário o código do produto a ser removido e o exclui do estoque, se encontrado.
  Retorna ao menu principal ao digitar "fim".
  """
  while True:  
    user = input("Informe o código do item que deseja remover (escreva fim para sair): ").lower()
    if user=='fim':
      break 
    elif not user.isdigit():
      print('O código deve ser um número inteiro. Tente novamente')
      continue
    user = user.replace(',','.')
    produto_encontrado = False
    user = int(user)
    for x in estoque:
      if user == x['codigo']:
        estoque.remove(x)
        print(f'Produto com código {user} foi removido com sucesso.')
        produto_encontrado = True
        break
    if not produto_encontrado:
      print(f'Nenhum produto encontrado com o código {user}. Tente novamente.')
      
def exibir_esgotados():
  """
  Exibe produtos que possuem quantidade em estoque igual a zero.
  Lista os produtos esgotados ou uma mensagem indicando que não há produtos com essa característica.
  """
  esgotados = list(filter(lambda x: x['quantidade_estoque'] == 0, estoque))
  if not esgotados:
    print('\nNão há nenhum produto com esses parâmetros')
  else:
    print(f"{'Descrição'.ljust(30)}{'Código'.ljust(10)}{'Quantidade'.ljust(12)}{'Custo'.ljust(10)}{'Preço de venda'.ljust(15)}")
    print('-' * 90)
    for produto in esgotados:
      print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).ljust(10)}{str(produto['quantidade_estoque']).ljust(12)}{str(produto['custo']).ljust(10)}{str(produto['preco_venda']).ljust(15)}")
  
def listar_estoque_baixo():
  """
  Lista produtos cujo estoque está abaixo de um valor mínimo definido pelo usuário.
  Por padrão, o valor mínimo é 5.
  """
  while True:
    user = input('\nInforme o valor mínimo de estoque (caso deixar em branco, o padrão será 5):')
    
    if user.isdigit():
      user = int(user)
      break
    elif user == '':
      user = 5
      break
    else:
      print('Valor inválido. Tente novamente!')
  estoque_baixo = list(filter(lambda x: x['quantidade_estoque'] <= user, estoque))
  
  if not estoque_baixo:
    print('\nNão há nenhum produto com esses parâmetros')
  else:
    print(f"{'Descrição'.ljust(30)}{'Código'.ljust(10)}{'Quantidade'.ljust(12)}{'Custo'.ljust(10)}{'Preço de venda'.ljust(15)}")
    print('-' * 90)
    for produto in estoque_baixo:
      print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).ljust(10)}{str(produto['quantidade_estoque']).ljust(12)}{str(produto['custo']).ljust(10)}{str(produto['preco_venda']).ljust(15)}")

def atualizar_estoque():
  """
  Atualiza a quantidade em estoque de um produto.
  Solicita ao usuário o código do produto e o novo valor para o estoque. 
  Atualiza a quantidade caso o produto seja encontrado. Caso contrário, exibe uma mensagem de erro.
  """
  while True:
    user = input('Informe o código do produto a ser atualizado (digite fim para terminar): ')
    if user.lower() == 'fim':
      print("Saindo da atualização de estoque.")
      break
    try: 
      user = int(user)
      produto_encontrado = False
      for produto in estoque:
        if user == produto['codigo']:
          produto_encontrado = True
          while True:
            quantidade_nova = input('Informe mudança de quantidade do produto (digite fim para terminar): ')
            if quantidade_nova.lower() == 'fim':
              print("Saindo da alteração deste produto.")
              break
            try: 
              quantidade_nova = int(quantidade_nova)
              if validar_alteracao(produto, quantidade_alterada=quantidade_nova):
                produto['quantidade_estoque'] += quantidade_nova
                print(f"Estoque atualizado com sucesso! Novo estoque: {produto['quantidade_estoque']}")
                return
            except ValueError:
              print( 'Quantidade inválida. Tente novamente')
          break
      if not produto_encontrado: 
        print('Código não encontrado. Tente novamente')
        continue
      break
    except ValueError:
      print('Erro: Código precisa ser um número. Tente novamente')

def atualizar_precos ():
  """
  Atualiza o preço de venda de um produto no estoque.
  Solicita ao usuário o código do produto e o novo preço de venda. 
  Atualiza o preço caso o produto seja encontrado. Caso contrário, exibe uma mensagem de erro.
  """
  while True:
    user = input('Informe o código do produto a ser atualizado (digite fim para terminar): ')
    if user.lower() == 'fim':
      print("Saindo da atualização de preços.")
      break
    try: 
      user = int(user)
      produto_encontrado = False
      for produto in estoque:
        if user == produto['codigo']:
          produto_encontrado = True
          while True:
            preco_novo = input('Informe mudança de preço do produto (digite fim para terminar): ')
            if preco_novo.lower() == 'fim':
              print("Saindo da alteração deste produto.")
              return
            try: 
              preco_novo = preco_novo.replace(',','.')
              preco_novo = float(preco_novo)
              if validar_alteracao(produto, novo_preco=preco_novo):
                produto['preco_venda'] += preco_novo
                print(f"Preço atualizado com sucesso! Novo preço: {produto['preco_venda']}")
                return
            except ValueError:
              print( 'Preço inválida. Tente novamente')
              break
      if not produto_encontrado: 
        print('Código não encontrado. Tente novamente')
        continue
      break
    except ValueError:
      print('Erro: Código precisa ser um número. Tente novamente')
      
def calcular_valor_estoque():
  """
  Calcula o valor total do estoque.
  
  Para cada produto no estoque, multiplica a quantidade em estoque pelo preço de venda
  e acumula o valor total.
  
  Exibe o valor total do estoque no final.
  """
  valores_totais = map(lambda x: x['quantidade_estoque'] * x['preco_venda'], estoque)
  total = sum(valores_totais)
  print(f'O valor total do estoque é de R${total:.2f}')
  
def calcular_lucro():
  """
  Calcula o lucro total do estoque.
  
  Para cada produto no estoque, calcula o lucro como a diferença entre
  o valor total de venda e o total de custo.
  Soma os lucros de todos os produtos.
  
  Exibe o lucro total do estoque no final.
  """
  lucros = map(lambda x: (x['preco_venda'] - x['custo']) * x['quantidade_estoque'], estoque)
  total = sum(lucros)
  print(f'O lucro total do estoque é de R${total:.2f}')
  
def gerar_relatorio():
  """
  Gera e exibe um relatório detalhado do estoque.
  
  Para cada produto no estoque, exibe os campos:
  - Descrição
  - Código
  - Quantidade em estoque
  - Custo unitário
  - Preço de venda
  - Valor total (quantidade x preço de venda)
  
  Calcula e exibe também os totais de custo e faturamento do estoque.
  Caso o estoque esteja vazio, exibe uma mensagem apropriada.
  """
  if not estoque:
    print("Estoque vazio. Nenhum relatório a exibir.")
    return

  # Cabeçalho do relatório
  print("\n" + "=" * 120)
  print(f"{'Descrição'.ljust(30)}{'Código'.rjust(15)}{'Quantidade'.rjust(15)}{'Custo'.rjust(15)}{'Preço'.rjust(25)}{'Valor Total'.rjust(20)}")
  print("=" * 120)

  custo_total = 0
  faturamento_total = 0

  # Linhas do relatório
  for produto in estoque:
    descricao = produto['descricao']
    codigo = produto['codigo']
    quantidade = produto['quantidade_estoque']
    custo = produto['custo']
    preco_venda = produto['preco_venda']
    valor_total = quantidade * preco_venda

    # Soma para os totais
    custo_total += quantidade * custo
    faturamento_total += valor_total

    # Exibir os dados do produto
    print(f"{descricao.ljust(30)}{str(codigo).rjust(15)}{str(quantidade).rjust(15)}"
          f"{f'R$ {custo:.2f}'.rjust(15)}{f'R$ {preco_venda:.2f}'.rjust(25)}{f'R$ {valor_total:.2f}'.rjust(20)}")

  # Rodapé com os totais
  print("=" * 120)
  print(f"{'Custo Total:'.ljust(54)}{f'R$ {custo_total:.2f}'.rjust(12)}")
  print(f"{'Faturamento Total:'.ljust(54)}{f'R$ {faturamento_total:.2f}'.rjust(12)}")
  print("=" * 120)
    
def main():
  """
  Função principal do sistema.
  
  Exibe um menu de opções e permite ao usuário interagir com o sistema.
  As opções incluem funcionalidades como:
  - Cadastrar produtos
  - Atualizar estoque
  - Listar produtos
  - Buscar produtos
  - Remover produtos
  - Ordenar estoque
  - Exibir produtos esgotados
  - Listar produtos com estoque baixo
  - Atualizar preços
  - Calcular valor total do estoque
  - Calcular lucro total do estoque
  - Gerar relatório completo do estoque
  
  O loop principal continua até que o usuário escolha a opção de encerrar o programa.
  """
  while True:
    opcao = entrar_opcao()
    if opcao == 0:  # Opção para sair
      print("Encerrando o sistema. Até mais!")
      break
    match(opcao):
      case 1: 
        cadastrar_produtos()
      case 2: 
        atualizar_estoque()
      case 3: 
        listar_produtos()
      case 4: 
          user = input("Informe o nome do produto ou o código que deseja procurar: ")
          buscar_produtos(user)
      case 5: 
        remover_produtos()
      case 6: 
        ordenar_estoque()
      case 7: 
        exibir_esgotados()
      case 8: 
        listar_estoque_baixo()
      case 9: 
        atualizar_precos()
      case 10: 
        calcular_valor_estoque()
      case 11: 
        calcular_lucro()
      case 12: 
        gerar_relatorio()
      case _:  # Caso padrão (opção não reconhecida)
        print("Opção inválida. Tente novamente.")
      
main()