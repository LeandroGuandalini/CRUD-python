def validar_estoque_inicial(estoque_inicial):
  """
  Valida e converte os dados de estoque inicial em uma lista de dicionários.

  A função recebe uma string de estoque inicial no formato específico, onde os produtos 
  são separados por '#' e as propriedades de cada produto (descrição, código, quantidade, custo, preço)
  são separadas por ';'. A função então converte esses dados em um formato estruturado (lista de dicionários).

  Parâmetros:
  estoque_inicial (str): String contendo os dados dos produtos, separados por '#', e as propriedades de cada produto separadas por ';'.

  Retorna:
  list: Lista de dicionários com os dados dos produtos, incluindo 'descricao', 'codigo', 'quantidade_estoque', 'custo', e 'preco_venda'.
  """
  estoque_inicial = estoque_inicial.split('#')
  estoque = []
  for i in estoque_inicial:
    descricao, codigo, quantidade_estoque,custo,preco_venda = i.split(';')
    estoque.append({
      'descricao': descricao.lower(),
      'codigo': int(codigo),
      'quantidade_estoque': int(quantidade_estoque),
      'custo': float(custo),
      'preco_venda': float(preco_venda)
    })
  return estoque

def validar_entrada(tipo, mensagem, erro_msg):
  """
  Valida a entrada do usuário para garantir que seja do tipo esperado e maior que zero.

  A função solicita uma entrada do usuário e verifica se o valor é do tipo esperado (int ou float) e se é maior 
  que zero. Caso contrário, exibe uma mensagem de erro e solicita novamente.

  Parâmetros:
  tipo (str): O tipo esperado para a entrada. Pode ser 'int' ou 'float'.
  mensagem (str): A mensagem a ser exibida para o usuário, pedindo a entrada.
  erro_msg (str): A mensagem de erro a ser exibida caso a entrada não seja válida.

  Retorna:
  int/float: O valor inserido pelo usuário, convertido para o tipo especificado ('int' ou 'float').
  """
  while True:
    entrada = input(mensagem)
    if not entrada:
      print(erro_msg)
      continue
    try:
      if tipo == 'int':
        entrada = int(entrada)
        if entrada <= 0:
          print('Número inválido, precisa ser inteiro e maior que zero. Tente novamente')
        else:
          return entrada
      elif tipo == 'float':
        entrada = float(entrada)
        if entrada <= 0:
          print('Número inválido, precisa ser maior que zero. Tente novamente')
        else:
          return entrada
    except ValueError:
      print(f'{erro_msg} Tente novamente.')
      
def validar_alteracao(produto, quantidade_alterada=None, novo_preco=None):
  """
  Valida alterações de quantidade e preço de um produto.

  Parâmentros:
  produto (dict): O dicionário do produto que será alterado.
  quantidade_alterada (int, optional): A alteração na quantidade de estoque. Pode ser negativa ou positiva.
  novo_preco (float, optional): O novo preço de venda do produto.

  Returns:
  bool: True se todas as alterações forem válidas, False caso contrário.
  """
  if quantidade_alterada is not None:
    nova_quantidade = produto['quantidade_estoque'] + quantidade_alterada
    if nova_quantidade < 0:
      print("Erro: A alteração resultaria em estoque negativo.")
      return False

  if novo_preco is not None:
    preco2 = produto['preco_venda'] + novo_preco
    if preco2 < produto['custo']:
      print("Erro: O preço de venda não pode ser menor que o custo do item.")
      return False

  return True