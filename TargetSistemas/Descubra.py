#Descubra a lógica e complete o próximo elemento: a) 1, 3, 5, 7, ___ b) 2, 4, 8, 16, 32, 64, ____ c) 0, 1, 4, 9, 16, 25, 36, ____ d) 4, 16, 36, 64, ____ e) 1, 1, 2, 3, 5, 8, ____ f) 2,10, 12, 16, 17, 18, 19, ____

#incremeto de número impares
def proximo_a():
    seq_a = [1,3,5,7]
    return seq_a[-1] + 2

#potência de 2
def proximo_b():
    seq_b = [2,4,8,16,32,64]
    return seq_b[-1] * 2

#quadrado perfeito
def proximo_c():
    seq_c = [0,1,4,9,16,25,36]
    n = len(seq_c)
    return n**2 

#quadrados de números pares
def proximo_d():
    seq_d = [4,16,36,64]
    n = len(seq_d) +1
    return (n*2) **2

#sequência Fibonacci
def proximo_e():
    seq_e = [1,1,2,3,5,8]
    return seq_e[-1] + seq_e[-2]

#Multiplos de 2 após sequência de números
def proximo_f():
    seq_f = [2,10,12,16,17,18,19]
    return 20


print('..............R E S U L T A D O...............')
print('a) 1, 3, 5, 7, ___')
print(f'Proximo numero da sequência: {proximo_a()}')
print('..............................................')
print('b) 2, 4, 8, 16, 32, 64, ____ ')
print(f'Proximo numero da sequência: {proximo_b()}')
print('..............................................')
print('c) 0, 1, 4, 9, 16, 25, 36, ____')
print(f'Proximo numero da sequência: {proximo_c()}')
print('..............................................')
print('d) 4, 16, 36, 64, ____')
print(f'Proximo numero da sequência: {proximo_d()}')
print('..............................................')
print('e) 1, 1, 2, 3, 5, 8, ____')
print(f'Proximo numero da sequência: {proximo_e()}')
print('..............................................')
print('f) 2,10, 12, 16, 17, 18, 19, ____')
print(f'Proximo numero da sequência: {proximo_f()}')
print('..............................................')