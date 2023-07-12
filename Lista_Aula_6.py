# Exercicios

# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.

nome = input("Digite uma palavra:")

for caract in nome:
    print(caract)


# 2.Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string: Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "
nome = input("Digite uma palavra:")
nome_lista = list(nome)
print(nome_lista)


# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'

nome = "aeIt"
nome = nome.replace("a", "4")
nome = nome.replace("e", "3")
nome = nome.replace("I", "1")
nome = nome.replace("t", "7")
print(nome)

# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".

nome = input("Digite uma palavra:")
nome_novo = nome[::-1]
print(nome_novo)

# 5. Escreva um programa que duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.

nome = "Carla"
nome_lista = list(nome)
print(nome_lista)
nome_lista[3] = "i"
nome_lista[4] = "o"

print(nome_lista)
nome = "".join(nome_lista)
print(nome)

# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto..
nome = "Paulo"
print(nome.find("l"))
