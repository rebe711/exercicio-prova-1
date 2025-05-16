import math
def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    numero = int(input("Digite um número: "))
    if (numero % 2 == 0):
        print("Par")
    else:
        print("Impar")


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """

    texto = input("digite o texto: ")
    tamanho = len(texto)
    meio = math.ceil(tamanho / 2)
    print(texto[meio:tamanho])


def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    n = int(input("Digite um número: "))
    for i in range(1, 11):
        print(n * i, end = ' ')



def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
preposicoes = ['da', 'de', 'do', 'das', 'dos', 'e']
nome = input("Digite um nome: ").split()

resultado = []
for palavra in nome:
    if palavra in preposicoes:
        resultado.append(palavra)
    else:
        resultado.append(palavra[0].upper() + palavra[1:])
        
print(' '.join(resultado))


def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    lados = input("Digite os lados do triângulo: ").split()
    a, b,c = map(float, lados)
    if a + b > c and a + c > b and b + c > a  :
        if a == b == c:
            print("Triângulo equilátero.")
        elif a == b or a == c or c == b:
            print("Triãngulo isóceles.")
        else: 
            print("Triângulo escaleno.")
    else:
        print("Tente novamente.")


def q6():
    pass

def q7():
    pass

def q8():
    pass

def q9():
    pass

def q10():
    pass

if __name__ == "__main__":
    q4()