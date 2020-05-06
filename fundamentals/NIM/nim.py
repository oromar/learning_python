def computador_escolhe_jogada(n, m):
    x = m + 1
    for i in range(1, x):
        if (n - i) % x == 0:
            return i   
    if n > m:
        return m
    return n

def usuario_escolhe_jogada(n, m):
    a = m + 1
    while a > m or a <= 0 or a > n:
        a = int(input('Quantas peças você vai tirar? '))
        if a > m or a <= 0 or a > n:
            print('Oops! Jogada inválida! Tente de novo')
    return a

def partida():
    n = int(input('Quantas peças?  '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m + 1) == 0:
        print('Você começa')
        jog = usuario_escolhe_jogada(n, m)
        print('Você tirou', jog, 'peças')
        n -= jog
        if n ==0:
            print('Fim do jogo! Você ganhou!')
            return 'Jogador'        
    else:
        print('Computador começa!')

    while n > 0:
        pc = computador_escolhe_jogada(n, m)
        print('O computador tirou', pc, 'peças')    
        n -= pc
        if n == 0: 
            print ('Fim do jogo! O computador ganhou!')
            return 'Computador'
        print('Agora resta(m)', n, 'peças no tabuleiro')

        jog = usuario_escolhe_jogada(n, m)
        print('Você tirou', jog, 'peças')
        n -= jog
        if n ==0:
            print('Fim do jogo! Você ganhou!')
            return 'Jogador'
        print('Agora resta(m)', n, 'peças no tabuleiro')        
        

def campeonato():
    jogador = 0
    pc = 0
    for i in range(1, 4):        
        print('***** Rodada', i,'*****')
        ganhou = partida()
        if ganhou == 'Jogador':
            jogador += 1
        else:
            pc += 1

    print('Placar: Você', jogador, 'X', pc, 'Computador')


def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    a = int(input('Escolha o tipo de jogo:'))
    if a == 1:
        print('Voce escolheu uma partida isolada!')
        partida()
    else:
        print('Voce escolheu um campeonato!')
        campeonato()

main()

