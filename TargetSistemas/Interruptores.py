#Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

#Estados das lâmpadas [0] = apagada, [1] = acessa, [2] = quente
lampadas = ['apagada','apagada','apagada']
def interruptores():
    lampadas[0] = 'quente' #Lâmpada 1 esta quente
    lampadas[1] = 'apagada'#Lâmpada 2 permanece apagada
    lampadas[2] = 'acessa' #Lâmpada 3 é acessa

def identificar_lampadas():
    interruptores()

#identifica os interrupores
    if lampadas[0] == 'quente':
        print('A lâmpada 1 é controlada pelo interruptor 1')
    if lampadas[1] == 'apagada':
        print('A lâmpada 2 é controlada pelo interruptor 3')
    if lampadas[2] == 'acessa':
        print('A lâmpada 3 é controlada pelo interruptor 2')
        
identificar_lampadas()