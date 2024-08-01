import random

def menu():
    print("     Bem vindo ao jogo da Forca!\n")
    print(f"{"-"*15} Menu {"-"*15}\n")

def menu_dificuldade():
    print("Selecione a dificuldade desejada [1 / 3]: ")
    print("1- Fácil")
    print("2- Médio")
    print("3- Difícil")

    opcao = input("Digite a opção desejada: ")
    return opcao

def informacoes_do_jogador(jogador, tentativas, erros):
    print(f"Jogador: {jogador}")
    print(f"Tentativas restantes: {tentativas}")
    print(f"Erros: {erros}")

def solicitar_opcao():

    print("\nEscolha uma opção:\n")
    print("1 - Chutar uma letra")
    print("2 - Chutar a palavra\n")

    opcao = input("Digite a opção desejada [1 / 2]: ")
    return opcao

def verificar_letra(palavra, palpite):
    if palpite not in palavra:

        return False
    
    return True


def palavra_correta(jogador, vitorias, derrotas):
    vitorias += 1
    arquivo = open("historico.txt", "w")
    arquivo.write(f"Jogador: {jogador}\n")
    arquivo.write(f"Vitorias: {vitorias}\n")
    arquivo.write(f"Derrotas: {derrotas}\n")
    arquivo.close()

def palavra_errada(jogador, vitorias, derrotas):
    derrotas += 1
    arquivo = open("historico.txt", "w")
    arquivo.write(f"Jogador: {jogador}\n")
    arquivo.write(f"Vitorias: {vitorias}\n")
    arquivo.write(f"Derrotas: {derrotas}\n")
    arquivo.close()


def main():

    dificuldade = menu_dificuldade()
    
    if dificuldade == '1':
        with open("palavras_facil.txt", "r", encoding="utf-8") as arquivo:
            palavras = arquivo.read()
            palavras = palavras.split((','))
            palavra_aleatoria = random.choice(palavras).upper()
        tentativas = 6

    if dificuldade == '2':
        with open("palavras_medio.txt", "r", encoding="utf-8") as arquivo:
            palavras = arquivo.read()
            palavras = palavras.split((','))
            palavra_aleatoria = random.choice(palavras).upper()
        tentativas = 4

    if dificuldade == '3':
        with open("palavras_dificil.txt", "r", encoding="utf-8") as arquivo:
            palavras = arquivo.read()
            palavras = palavras.split((','))
            palavra_aleatoria = random.choice(palavras).upper()
        tentativas = 2

    letras_certas = ["_" for letra in palavra_aleatoria] # Compreensão de lista
    erros = 0
    vitorias = 0
    derrotas = 0
    acertos = 0
    aux = len(palavra_aleatoria)

    menu()
    print(palavra_aleatoria)
    jogador = input("Como deseja ser chamado?: ").upper()

    
    try:

        while tentativas > 0:

            informacoes_do_jogador(jogador, tentativas, erros)
            print("\nA palavra é: ", " ".join(letras_certas))
            
            opcao = solicitar_opcao()
            
            if opcao == '1':

                palpite = input("Digite a letra: ").upper()
                contem_letra = verificar_letra(palavra_aleatoria, palpite)
                if contem_letra:
                    for i in range(len(palavra_aleatoria)):
                        if palavra_aleatoria[i] == palpite:
                            letras_certas[i] = palpite
                            acertos += 1
                    if acertos == aux:
                        print(f"Parabéns! Você advinhou a palavra: {palavra_aleatoria.upper()}")
                        palavra_correta(jogador, vitorias, derrotas)
                        break

                else:
                    erros += 1
                    tentativas -= 1
                    print(f"Você errou pela {erros}° vez. Tente novamente!\n")

            elif opcao == '2':

                palpite = input("Digite a palavra: ").upper()
                    
                if palpite == palavra_aleatoria:
                    print(f"Parabéns! Você advinhou a palavra: {palavra_aleatoria.upper()}")
                    palavra_correta(jogador, vitorias, derrotas)
                else:
                    print(f"Você perdeu! A palavra era: {palavra_aleatoria.upper()}")
                    palavra_errada(jogador, vitorias, derrotas)
                break
            else:
                print("Opção inválida!!!\n")
        else:
            print(f"Você perdeu! A palavra era: {palavra_aleatoria.upper()}")
            palavra_errada(jogador, vitorias, derrotas)
    except Exception as e:
        print(f"Erro inesperado {e}")


main()