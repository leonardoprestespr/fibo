# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

#Gerar sequencia Fibonacci até o valor 'n'

def sequncia_fibonacci(n): 
    fibo_sequencia = [0,1]
    while fibo_sequencia [-1] < n:
        fibo_sequencia.append(fibo_sequencia [-1] + fibo_sequencia [-2])
    return fibo_sequencia

#Checar numero fornecido pelo usuário

def checar_numero(numero):
    fibo_sequencia = sequncia_fibonacci(numero)

    if numero in fibo_sequencia:
        return f"o número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertece à sequência de Fibonacci. "
    
#solicita ao usuario infomar o número
def fibonacci_check ():
    while True:
      user_input = input("Digite um número para verificar se pertence a sequência de Fibonacci (ou escreva 'sair' para encerrar): ")
      
      if user_input.lower() == 'sair': 
          print('Encerrando o programa.....')
          break
#tenta converter a entrada para um número inteiro
      try: 
          numero = int(user_input)
          resultado = checar_numero(numero)
          print(resultado)
      except ValueError:
          print("Entrada inválida. Por favor, digite um número válido ou 'sair' para encerrar. ")

fibonacci_check()
          


