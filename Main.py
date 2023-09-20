#Vetores com os dados de cadastros

codigodosprodutos=[0,1,2,3]
produtoscadastrados=['Banana','Água','Feijão','Arroz']
precodosprodutos=[2.50,1.10,4.90,3.20]
quantidadedosprodutos=[22,12,4,5]

#classe para fazer compras e fazer cupom

class compras:
  comprasNome=None
  ComprasCod=None
  ComprasQuantidadeProd=None
  ComprasPrecoProd=None

#vetor para fazer compras

listadecompras=[]

#proço do cupom

precodocupom=[]

#função de entrada do programa

def telageral():
    
    print("-"*100)
    print(" "*40,"PAINEL GERAL"," "*40)
    print(" ")
    print("-"*100)
    print(" ")
    print("Para cadastrar um produto, digite: a ")
    print(" ")
    print("Para visualizar o estoque, digite: b ")
    print(" ")
    print("Para realizar uma compra, digite: c ")
    print(" ")
    print("Para atualizar o cadastro de um produto, digite: d ")
    print(" ")
    print("Para consultar um produto, digite: e ")
    print(" ")
    print("Para Sair do Programa, digite: x")
    print(" ")
    return (input('\nDigite o código da operação que deseja fazer: '))

# função ver todos os produtos#  
def verestoque(): 
  print("-"*100)
  print(" "*37,"PRODUTOS CADASTRADOS"," "*40)
  print(" ")
  print("-"*100) 
  if (len(produtoscadastrados)) == 0 :
    print(" ")
    print("Não há produtos no estoque")
    print(" ")  
  else:
    print(" ")
    print("-"*100)
    print(" ")
    for i in range(len(produtoscadastrados)):
      print(f"[Código do Produto]: {codigodosprodutos[i]} [Nome]: {produtoscadastrados[i]} [Preço do produto]: {precodosprodutos[i]:.2f} Reais  [Quantidade em estoque]: {quantidadedosprodutos[i]} unidade(s)")

  
#cadastro de produto#

def cadastrarproduto():
  produtoscadastrados.append(input("\nInforme o Nome do produto: "))
  precodosprodutos.append(float(input("Informe o preço do produto: ")))
  quantidadedosprodutos.append(int(input("Informe a quantidade do produto a ser cadastrado: ")))
  codigodosprodutos.append(int((len(codigodosprodutos)*1)))
  print(" ")
  print("-"*100)
  print(" ")
  print("O produto foi cadastrado com sucesso")
  print(" ")
  print("-"*100)
  print(" ")
 
#atualizar produtos"

def atualizarprodutos():
  while True:
    while True:
      codPro = int(input("Digite o Código do Produto :"))
      if codPro in codigodosprodutos:
        print("-"*100)
        print(" ")
        print(f"Produto: {produtoscadastrados[codPro]}")
        print(" ")
        print("_"*100)
        precodosprodutos[codPro]=(float(input("Informe o novo preço do produto: ")))
        quantidadedosprodutos[codPro]=(int(input("Informe a nova quantidade do produto no estoque: ")))
        break
      else:  
        print("_"*100)
        print(" ")
        print("Produto não encontrado")
        print(" ")
        print("_"*100)
        break
    print(" ")
    print("_"*100)
    print(" ")
    print("PARA ATUALIZAR OUTRO PRODUTO DIGITE: a ")
    print("PARA VOLTAR AO MENU INICIAL DIGITE: x ")
    print(" ")
    print("_"*100)
    print(" ")
    Modulodeconsulta=input()
    if Modulodeconsulta == "x":
      break
    if Modulodeconsulta == "a":
      continue
    else:
      print(" ")
      print("_"*100)
      print(" ")
      print("OPÇÃO INVÁLIDA, O PROGRAMA IRÁ RETORNAR AO MENU INICIAL ")
      print(" ")
      print("_"*100)
      print(" ")
      break

#fazercompras

def cumpomdecompra():
  while True:  
    while True:
      produtocomprado=int(input("Digite o Código do produto que deseja comprar, ou digite -1 para finalizar procedimento: "))
      if produtocomprado in codigodosprodutos:
        print(" ")
        print("_"*100)
        print(" ")
        print(produtoscadastrados[produtocomprado])
        print(" ")
        print("_"*100)
        print(" ")
        listacompras=compras()
        listacompras.ComprasCod=codigodosprodutos[produtocomprado]
        listacompras.ComprasNome=(produtoscadastrados[produtocomprado])
        while True:
          quantidade=int(input("Quantidade do produtos: "))
          print('_'*100)
          if quantidade <= quantidadedosprodutos[produtocomprado]:
            listacompras.ComprasQuantidadeProd=int(quantidade)
            listacompras.ComprasPrecoProd=float(precodosprodutos[produtocomprado])
            listadecompras.append(listacompras)
            break
          else:
            print(" ")
            print("_"*100)
            print(" ")
            print("A quantidade informada é superior ao nosso estoque. Digite uma quantidade Válida")
            print(" ")
            print("_"*100)
            print(" ")
            continue
      if produtocomprado == -1:
        break
      else:
        print(" ")
        continue
    print("_"*100)
    print(" ")          
    print("PARA FINALIZAR COMPRA E IMPRIMIR CUPOM DIGITE: a ")
    print("_"*100)
    print(" ")
    print("PARA VOLTAR AO MENU INICIAL DIGITE: x ")
    print(" ")
    print("_"*100)
    print(" ")
    Modulodeconsulta=input()
    if Modulodeconsulta == "x":
      break
    if Modulodeconsulta == "a":
      while True:
        print("-"*100)
        print(" "*40,"CUPOM FISCAL"," "*40)
        print(" ")
        print("-"*100)
        print(" ")
        print("|Código do Produto|        |Nome|                    |Preço do produto|          |QTD.|        ")
        precototalfinal=0
        for numerodecompras in range(len(listadecompras)):
          print("-"*100)
          precodacomprax=(listadecompras[numerodecompras].ComprasQuantidadeProd)*(listadecompras[numerodecompras].ComprasPrecoProd)
          print(f"        {listadecompras[numerodecompras].ComprasCod}                   {listadecompras[numerodecompras].ComprasNome}                {listadecompras[numerodecompras].ComprasPrecoProd:.2f} reais                   {listadecompras[numerodecompras].ComprasQuantidadeProd}")   
          precototalfinal+=precodacomprax
          print("-"*100)
          print(f"TOTAL:                                               {precodacomprax:.2f}                      ")
          print("-"*100)
        break        
      print(f" O Valor total da compra é:                        {precototalfinal:.2f}                          ")
      break
    else:
      print(" ")
      print("_"*100)
      print(" ")
      print("OPÇÃO INVÁLIDA, DIGITE UM CÓDIGO VÁLIDO ")
      print(" ")
      print("_"*100)
      print(" ")
      continue




#consulta de produto    
def consultarproduto():
  while True:
    while True:
      consultacod=int(input("Digite o Código do Produto que irá ser consultado: "))
      print(" ")
      print("_"*100)
      print(" ")
      if consultacod in codigodosprodutos:
        print("-"*100)
        print(" ")
        print(f"Produto: {produtoscadastrados[consultacod]}")
        print(" ")
        print("_"*100)
        print(f"[Código do Produto]: {codigodosprodutos[consultacod]} [Nome]: {produtoscadastrados[consultacod]} [Preço do produto]: {precodosprodutos[consultacod]:.2f} Reais  [Quantidade em estoque]: {quantidadedosprodutos[consultacod]} unidade(s)")
        break
      else:  
        print("_"*100)
        print(" ")
        print("Produto não existe no sistema")
        print(" ")
        print("_"*100)
        break
    print(" ")
    print("_"*100)
    print(" ")
    print("PARA CONSULTAR OUTRO PRODUTO DIGITE: a ")
    print("PARA VOLTAR AO MENU INICIAL DIGITE: x ")
    print(" ")
    print("_"*100)
    print(" ")
    Modulodeconsulta=input()
    if Modulodeconsulta == "x":
      break
    if Modulodeconsulta == "a":
      continue
    else:
      print(" ")
      print("_"*100)
      print(" ")
      print("OPÇÃO INVÁLIDA, O PROGRAMA IRÁ RETORNAR AO MENU INICIAL ")
      print(" ")
      print("_"*100)
      print(" ")
      break
    


# programa rodando
modulopainel=0
while modulopainel != -1:
    selecaodousuario = telageral()
    if selecaodousuario == "a":
      cadastrarproduto()

    if selecaodousuario == "b":
      verestoque()
    
    if selecaodousuario == "c":
      cumpomdecompra()

    if selecaodousuario == "d":
      atualizarprodutos()

    if selecaodousuario == "e":
      consultarproduto()   

    if selecaodousuario == "x":
      modulopainel=-1
    else:
      print(" ")
      print("-"*100)
      print(" ")
      print(" ")
      print(" ")
      print("-"*100)
      print(" ")
