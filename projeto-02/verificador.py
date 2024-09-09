# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def verifica_a(string):
    string_lower = string.lower()
#verifica a exitência da letra 'a'
    if 'a' in string_lower:
        print("............................")
        print("A letra 'a' foi encontrada.")
    else:
        print("..............................")
        print("A letra 'a' não foi encontrada")
#conta a quantida de vezes que aparece
    qtd_a = string_lower.count('a')
    print('.............................................')
    print(f"A letra 'a' aparece {qtd_a} vez(es) na frase")
#entrada usuário
string = input("Digite uma frase: ")

verifica_a(string)
