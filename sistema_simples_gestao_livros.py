# Você foi contratado para desenvolver um sistema simples de
# gerenciamento de livros em uma biblioteca. O sistema deve permitir cadastrar novos livros, listar
# todos os livros disponíveis, buscar um livro pelo título, e gerar um gráfico com a quantidade de
# livros por gênero.

import matplotlib.pyplot as plt 

class Livros:
    #Atributos da classe Livros
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    #criação da lista vazia
    livros = []
    
    #função para adicioanr novos livros
    def cadastrar_livros():

      #Pegar informações
      titulo = input("Digite o titulo do livro: ")
      autor = input("Digite o autor do livro: ")
      genero = input("Digite o genero do livro: ")
      quantidade = int(input("Digite a quantidade do livro: "))

      livro = Livros(titulo, autor, genero, quantidade) #criando objeto

      Livros.livros.append(livro) #colocando na lista
      
      #mensagem de sucesso
      print("Livro cadastrado com sucesso!")

    #função para mostrar tudos os livros
    def listar_livros():
      # ira passar por toda a lista e mostrara as informações  
      for livro in Livros.livros:
        print(f"Titulo: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Genero: {livro.genero}")
        print(f"Quantidade: {livro.quantidade}")
        print("---------------------------------")
        print(" ")

    #Função para buscar o livro por nome
    def buscar_livro():
      # ira pedir o nome do livro
      nome_pesquisa = input("Digite o nome do livro que deseja buscar: ")

      # ira passar por toda a lista
      for livro in Livros.livros:
        if livro.titulo == nome_pesquisa: # ira verificar se nome é igual a nome_pesquisa
          print(f"O livro {livro.titulo}, esta no estoque!")

    #função de gerar grafico
    def gerar_grafico():
      quantidade_genero = {}

      #ira percorrer toda a lista
      for livro in Livros.livros:
        genero = livro.genero

        if genero in quantidade_genero: #caso o genero ja exista no dicionario conte +1
          quantidade_genero[genero] += 1
        else: # caso se nao, adicionar genero no dicionario com valor de 1
          quantidade_genero[genero] = 1

      # ira pegar o nomes  com .keys, e os valores com .values
      generos = list(quantidade_genero.keys())
      quantidades = list(quantidade_genero.values())

      #criando grafico
      plt.bar(generos, quantidades)

      #nomeando x e y
      plt.xlabel("Generos")
      plt.ylabel("Quantidade")

      #colocando titulo no grafico
      plt.title("Quantidade de Livros por Genero")

      #mostrar grafico
      plt.show()

while(True):
  
  #Menu
  print("Menu Biblioteca")
  print("1 - Cadastrar Livro")
  print("2 - Listar Livros")
  print("3 - Buscar Livro")
  print("4 - Gerar Grafico")
  print("5 - Sair")

  #ira pegar a opção
  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
      Livros.cadastrar_livros()
  elif opcao == 2:
      Livros.listar_livros()
  elif opcao == 3:
      Livros.buscar_livro()
  elif opcao == 4:
      Livros.gerar_grafico()
  elif opcao == 5:
      print("Saindo do Programa...")
      break
