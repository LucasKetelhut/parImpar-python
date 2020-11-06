import random
import time
computador=random.randint(0,10)
escolhajogador=escolhacomputador=''
soma=jogador=cont=0
perdeu=''

print('=-'*15)
print('  VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*15)

while True:
    jogador=int(input('Digite um valor: '))
    escolhajogador=str(input('Você quer PAR ou ÍMPAR? [P/I]: ')).strip().upper()
    soma=computador+jogador
    print('-'*65)
    print(f'Você jogou {jogador} e o computador jogou {computador}! Somando temos {soma}!',end=' ')
    print('DEU PAR!' if soma%2==0 else 'DEU ÍMPAR!')
    print('-'*65)
    if escolhajogador=='P':
        escolhacomputador='I'
        if soma % 2 == 0:
            print('Você VENCEU!')
            time.sleep(1)
            print('Vamos jogar novamente...')
            time.sleep(1)
            cont+=1
        else:
            print('Você PERDEU!')
            perdeu='True'
    if escolhajogador=='I':
        escolhacomputador='P'
        if soma % 2 != 0:
            print('Você VENCEU!')
            time.sleep(1)
            print('Vamos jogar novamente...')
            time.sleep(1)
            cont+=1
        else:
            print('Você PERDEU!')
            perdeu='True'
    if perdeu=='True':
        break
    print('='*30)
print(f'GAME OVER! Você conseguiu vencer {cont} vez(es)!')                        
