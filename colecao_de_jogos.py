import random

def jogo_de_adivinhacao():
    alvo = 34
    quantidadeTentativas = 5
    jogadorAcertou = False

    while quantidadeTentativas > 0 and not jogadorAcertou:
    
        try:
            chute = (input("Digite um número inteiro entre 0 e 100: "))

            if chute == alvo:
                print("Parabéns, você acertou!!!")
                jogadorAcertou =True
            elif chute > alvo:
                print("Errou, o número é menor")
                quantidadeTentativas -= 1
            else:
                print("Errou, o número é maior")
                quantidadeTentativas = quantidadeTentativas - 1

        except:
            print("Valor informado não é um numero inteiro")

    if not jogadorAcertou:
        print("Que pena, o número era " + str(alvo))


def jogo_jokenpo():
    

    print("Bem-vindo ao Jokenpo!")

    # Jogada do Jogador 1 (computador escolhe aleatoriamente)
    jogador1 = random.choice(["papel", "pedra", "tesoura"])

    # Entrada do Jogador 2 (garantindo uma escolha válida)
    while True:
        jogador2 = str(input("Escolha sua jogada: (pedra/papel/tesoura)")).lower()

        if jogador2 in ["pedra", "papel", "tesoura"]:
            break
    else:
        print("Escolha inválida! por favor, escolha 'pedra', 'papel' ou 'tesoura'")


    print(f"Jogador1 escolheu: {jogador1}")
    print(f"Jogador2 escolheu: {jogador2}")

    # Verificação do resultado
    if jogador1 == jogador2:
        print("Empate!")
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or(jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
            print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")
        


def jogo_perguntas_respostas():
    print("Jogo de perguntas e respostas")

    perguntaRespostas = {
    "Qual o maior animal terrestre?": "elefante africano",
    "Qual é o país mais populoso do mundo?": "china",
    "Quantos planetas existem no sistema solar?": "Oito"
    }

    pontuacao = 0

    for pergunta, respostaCerta in perguntaRespostas.items():
        respostaDoJogador = input(pergunta + " ").lower()

        if respostaDoJogador == respostaCerta.lower():
            print("Você acertou!\n")
            pontuacao += 1
        else:
            print(f"Você errou! A resposta correta é: {respostaCerta}\n")

            print(f"Fim do jogo! Sua pontuação {pontuacao} de {len(perguntaRespostas)} perguntas.")


print('''Iniciar - Selecionar jogo:

1 - Jogo de Adivinhação
2 - Jokenpo
3 - Quizz
0 - Sair
''')

jogo_em_andamento = True

while jogo_em_andamento:
    codigo_jogo = input("O que vamos jogar hoje? ")
    if codigo_jogo == "1":
        jogo_de_adivinhacao()
    elif codigo_jogo == "2":
        jogo_jokenpo()
    elif codigo_jogo == "3":
        jogo_perguntas_respostas()
    elif codigo_jogo == "0":
        print("Encerrando")
        jogo_em_andamento = False
    else:   
        print("Opção invalida")
