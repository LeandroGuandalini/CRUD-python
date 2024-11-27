estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

def validar_estoque_inicial(estoque_inicial):
  estoque_inicial = estoque_inicial.split('#')
  estoque = []
  for i in estoque_inicial:
    descricao, codigo, quantidade_estoque,custo,preco_venda = i.split(';')
    estoque.append({
      'descricao': descricao,
      'codigo': int(codigo),
      'quantidade_estoque': int(quantidade_estoque),
      'custo': float(custo),
      'preco_venda': float(preco_venda)
    })
  return estoque
    

estoque = validar_estoque_inicial(estoque_inicial)

def validar_entrada(tipo, mensagem, erro_msg):
  while True:
    entrada = input(mensagem)
    if not entrada:
      print(erro_msg)
      continue
    try:
      if tipo == 'int':
        return int(entrada)
      elif tipo == 'float':
        entrada = entrada.replace(',', '.')
        return float(entrada)
    except ValueError:
      print(f'{erro_msg} Tente novamente.')

def cadastrar_produtos(estoque):
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

def listar_produtos(estoque):
  if not estoque:
    print("Nenhum produto cadastrado.")
    return
  
  print(f"{'Descrição'.ljust(30)}{'Código'.ljust(10)}{'Quantidade'.ljust(12)}{'Custo'.ljust(10)}{'Preço de Venda'.ljust(15)}")
  print("-" * 77)
  
  for i in estoque:
    print(f"{i['descricao'].ljust(30)}{str(i['codigo']).ljust(10)}{str(i['quantidade_estoque']).ljust(12)}{str(i['custo']).ljust(10)}{str(i['preco_venda']).ljust(15)}")

def ordenar_estoque(estoque):
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


ordenar_estoque(estoque)