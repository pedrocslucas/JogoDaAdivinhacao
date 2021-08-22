#JOGO DO ADIVINHA 2.0v
import random as rd
from time import sleep

print('\033[2;34mJOGO DA ADIVINHAÇÃO 2.0v')

#CPU Sorteando o NÚMERO!!!
print('\033[1;97m!!!CPU SORTEANDO NÚMERO!!!')
sleep(0.5)
print('Aguarde', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(0.8)
numCPU = rd.randint(0,10)
print('\033[1;32mO número foi sorteado! Boa Sorte!')

#Escolha do Jogador!!!
tentativas = 0
while True:
    numPlayer = int(input('\033[1;97mEscolha um número entre 0 e 10:'))
    tentativas += 1
    if numPlayer == numCPU and tentativas == 1:
        print('\033[1;32mINCRÍVEL!!! Você precisou de apenas 1 tentativa para acertar')
        print(f'O número da CPU foi {numCPU}, e o número escolhido foi {numPlayer}')
        break
    elif numCPU > numPlayer:
        print('\033[1;33mMais... Tente outra vez!')
    elif numCPU < numPlayer:
        print('\033[1;33mMenos... Tente outra vez!')
    elif numPlayer == numCPU and tentativas != 1:
        print(f'\033[1;32mParabéns! \nVocê precisou de {tentativas} para acertar!')
        print(f'O número da CPU foi {numCPU}, e o número escolhido foi {numPlayer}')
        break

print('\033[4;91m!!!GAME OVER!!!')