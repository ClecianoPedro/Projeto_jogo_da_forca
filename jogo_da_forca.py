import random

def menu():
    print(f'{'-'*15} Menu {'-'*15}')

def menu_dificuldade():
    print('     Bem vindo ao jogo da Forca!\n')
    print(f'{'-'*15} Menu {'-'*15}\n')
    print('Selecione a dificuldade desejada [1 / 3]: \n')
    print('1- Fácil')
    print('2- Médio')
    print('3- Difícil')

    return input('\nDigite a opção desejada: ')

def informacoes_do_jogador(jogador, tentativas, erros, letras_tentadas):
    print(f'Jogador: {jogador}')
    print(f'Tentativas restantes: {tentativas}')
    print(f'Erros: {erros}')
    print(f'Letras tentadas: {' '.join(letras_tentadas)}')

def verifica_letra(palavra, palpite):
    if palpite in palavra:

        return True
    
    return False

def atualiza_historico(jogador, tentativas, erros, letras_tentadas, vitoria, palavra):
    arquivo = open('historico.txt', 'a')
    arquivo.write(f'\nJogador: {jogador}\n')
    arquivo.write(f'Tentativas restantes: {tentativas}\n')
    arquivo.write(f'Erros: {erros}\n')
    arquivo.write(f'Letras tentadas: {letras_tentadas}\n')
    arquivo.write(f'Palavra: {palavra}\n')

    if vitoria:
        arquivo.write('Resultado: Acertou\n')
    else:
        arquivo.write('Resultado: Errou\n')
    arquivo.close()

def escolhe_palavra(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        palavras = arquivo.read()
        palavras = palavras.split((','))
        palavra = random.choice(palavras).upper()
        return palavra

def main():
    letras_tentadas = []
    erros = 0
    continuar = True
    dificuldade = menu_dificuldade()

    while dificuldade < '1' or dificuldade > '3':
        print('\nOpcão inválida!\n')
        dificuldade = menu_dificuldade()
    
    if dificuldade == '1':
        nome_arquivo = 'palavras_facil.txt'
        tentativas = 6

    elif dificuldade == '2':
        nome_arquivo = 'palavras_medio.txt'
        tentativas = 4

    else:
        nome_arquivo = 'palavras_dificil.txt'
        tentativas = 2
    
    palavra_aleatoria = escolhe_palavra(nome_arquivo)
    palavra_oculta = ['_' for letra in palavra_aleatoria]
    print(palavra_aleatoria)
    jogador = input('\nComo deseja ser chamado: ').upper()

    while len(jogador) == 0:
        print('Nome inválido!')
        jogador = input('\nComo deseja ser chamado: ').upper()
 
    try:
        while tentativas > 0 and continuar:
            
            informacoes_do_jogador(jogador, tentativas, erros, letras_tentadas)
            print('\nA palavra é: ', ' '.join(palavra_oculta))  

            palpite = input('\nDigite uma letra ou a palavra inteira: ').upper()
        
            if palpite.isnumeric() or len(palpite) == 0:
                print('\nO palpite não é uma letra\n')

            elif  palpite in letras_tentadas:
                print('\nA letra digitada já foi tentada!\n')

            elif len(palpite) > 1 and len(palpite) < len(palavra_aleatoria):
                print('Digite apenas uma letra ou chute a palavra inteira!\n')

            elif len(palpite) > len(palavra_aleatoria):
                print('A quantidade de letras excede o tamanho da palavra!\n')

            elif palpite == palavra_aleatoria:
                print(f'\nParabéns! Você advinhou a palavra: {palavra_aleatoria.upper()}')
                letras_tentadas = ' '.join(palpite)
                atualiza_historico(jogador, tentativas, erros, letras_tentadas, True, palavra_aleatoria)
                continuar = False

            elif verifica_letra(palavra_aleatoria, palpite):
                for i in range(len(palavra_aleatoria)):

                    if palavra_aleatoria[i] == palpite:
                        palavra_oculta[i] = palpite
                        if palpite not in letras_tentadas:
                            letras_tentadas.append(palpite)

                    if '_' not in palavra_oculta:
                        print(f'\nParabéns! Você advinhou a palavra: {palavra_aleatoria.upper()}')
                        letras_tentadas = ' '.join(letras_tentadas)
                        atualiza_historico(jogador, tentativas, erros, letras_tentadas, True, palavra_aleatoria)
                        continuar = False

            elif verifica_letra (palavra_aleatoria, palpite) == False and len(palpite) == len(palavra_aleatoria):
                erros = 1
                print(f'\nVocê perdeu! A palavra era: {palavra_aleatoria.upper()}')
                letras_tentadas = ' '.join(palpite)
                continuar = False

            elif verifica_letra(palavra_aleatoria, palpite) == False:
                erros += 1
                tentativas -= 1
                letras_tentadas.append(palpite)
                print(f'\nVocê errou pela {erros}° vez. Tente novamente!\n')

        if tentativas == 0:
            print(f'\nVocê perdeu! A palavra era: {palavra_aleatoria.upper()}')
            letras_tentadas = ' '.join(letras_tentadas)
            atualiza_historico(jogador, tentativas, erros, letras_tentadas, False, palavra_aleatoria)

    except Exception as e:
        print(f'Erro inesperado: {e}')

main()