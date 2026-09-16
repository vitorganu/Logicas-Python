# Você foi contratado para desenvolver um sistema simples de gestão de
# notas de alunos. O sistema deve permitir que o usuário adicione notas, calcule a média das notas,
# determine a situação do aluno (aprovado ou reprovado), e exiba um relatório final. Utilize
# estruturas condicionais, de repetição e funções.

numeros = [] #criação da lista

# inserir dados ate numero[2]
numeros.insert(0, int(input("Digite o primeiro numero: ")))
numeros.insert(1, int(input("Digite o segundo numero: ")))
numeros.insert(2, int(input("Digite o terceiro numero: ")))

#calculo da media
media = ((numeros[0] + numeros[1] + numeros[2]) / 3)

# condições
if media >= 11: # caso a media for maior ou igual a 11 sera um valor invalido
  print("Valor Invalido!")
elif media >= 7: # se for maior ou igual a 7 vai ser aprovado
    print("Relatorio Final:")
    print("Situação: Aprovado!")
    print(f"Notas Inseridas: {numeros}, Media Final: {media}") #exibe as notas e a media
else: # caso nao cair nas outras condições, a situação sera reprovado
  print("Relatorio Final:")
  print("Situação: Reprovado! Tente Novamente na Proxima")
  print(f"Notas Inseridas: {numeros}, Media Final: {media}")



