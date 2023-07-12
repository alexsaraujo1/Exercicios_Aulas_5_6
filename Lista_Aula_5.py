# 1. Adicione os números de 1 a 10 à lista "minha_lista" utilizando um loop, em seguida imprima esses valores na tela e por fim
# mostre o tamanho dessa lista.


minha_lista = print(list(range(1, 11, 1)))

# 2 modo de fazer

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista:
    print(i)

    quantidade = len(lista)

    print(f"A lista possui {quantidade} elementos.\n")


# 2. Crie uma lista com os números pares de 0 a 20 e em seguida atenda os seguintes comandos:
# a) Inverta a ordem dos elementos da lista.
lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista = lista_pares[::-1]
print(lista)


# b) Remova os números múltimos de 5 da lista.
lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

lista_pares.remove(10)
lista_pares.remove(20)
print(lista_pares)

# Obs.como colocar 2 removes juntos


# 3. Crie uma lista chamada "lista_concatenada" que seja a concatenação das listas criadas na questão 1 e na questão 2.

lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [2, 4, 6, 8, 12, 14, 16, 18]

lista_concatenada = lista_pares + lista2
print(lista_concatenada)

# 4. Remova todos os elementos da lista "lista_concatenada".

lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [2, 4, 6, 8, 12, 14, 16, 18]

lista_concatenada = lista_pares + lista2
lista_concatenada.clear

# 5. Crie uma lista chamada "lista_repetida" com 5 repetições da lista "lista_concatenada".

lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [2, 4, 6, 8, 12, 14, 16, 18]

lista_repetida = lista_pares + lista2 * 5
print(lista_repetida)

# 6. Copie a lista "lista_concatenada" para uma nova lista chamada "copia_lista_concatenada" sem utilizar o operador de atribuição direta.

lista_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [2, 4, 6, 8, 12, 14, 16, 18]

lista_concatenada = lista_pares + lista2

copia_lista_concatenada = list(lista_concatenada)
print(lista_concatenada)


# 7. Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra.
# Apresente as duas listas preenchidas.

nome1 = input("Informe primeiro nome")
idade1=int(input("Informe sua idade"))

nome2 = input("Informe segundo nome")
idade2=int(input("Informe sua idade"))

nome3 = input("Informe terceiro nome")
idade3=int(input("Informe sua idade"))

nome4 = input("Informe quarto nome")
idade4=int(input("Informe sua idade"))

nome5 = input("Informe quinto nome")
idade5=int(input("Informe sua idade"))

print(
    "A primeira pessoa é :",
    nome1,
    "a segunda pessoa é:",
    nome2,
    "a terceira pessoa é:",
    nome3,
    "a quarta pessoa é:",
    nome4,
    "a quinta pessoa é:",
    nome5,
)

Falta as idades


# 8.Faça um script que leia números do usuário, enquanto ele não digitar 0.
# Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0,
# o valor máximo e o valor mínimo.

numeros = int(input("Informe um numero"))

print(min(numeros))
print(max(numeros))
print(sum(numeros))

OBS.: Faltou terminar.

# 9.Faça um script que informe o fatorial de um número.
# Utilize obrigatoriamente o comando for

# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
# Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)

# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.

# 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade
# de divisores desse número e quais são eles.
