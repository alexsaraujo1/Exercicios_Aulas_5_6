# Exercicios

# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.

nome = input("Digite uma palavra:")
nome_lista = list(nome)
print(nome_lista)

________2 forma:

nome = input("Digite uma palavra:")

print(nome.split("\n"))

OBS.: Não estou conseguindo separar as letras

# 2.Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string: Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "
nome = input("Digite uma palavra:")
nome_lista = list(nome)
print(nome_lista)



# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'

# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".

nome = input("Digite uma palavra:")
nome_novo = nome[::-1]
print(nome_novo)

# 5. Escreva um programa que duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.

# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto..
