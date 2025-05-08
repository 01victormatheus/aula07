def imprime_nome(nome):
    print(f"nome:{nome}")

def solicitarnome():
    nome=input("digite seu nome: ")
    return nome

def piramide(num):
    for x in range(0, num + 1, 1):
        for i in range(0, x):
            print(x, end=" ")
    print()
def contavogais(texto):
    vogais="aeiouAEIOU"
    cont = 0
    for x in range(0, len(texto)):
        if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
            cont = cont + 1
    print(cont)
def estoque (produto,qtd,valor):
        total = qtd * valor
        print(total)
def numero(num):
    if num!=0:
        if num>0:
            return "p"
        else:
            return "n"
    else:
        return "z"
def soma(*a):
    soma=0
    for x in range(len(a)):
         soma=soma+a[x]
    print(soma)