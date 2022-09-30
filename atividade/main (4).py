import random


# função que lê as perguntas
def inserir_perguntas():
    questao = []
    questoes = []
    arquivo = open("perguntas (2).txt", "r")
    frases = arquivo.readlines()
    arquivo.close()
    for frase in frases:
        questao.append(frase)
        if len(questao) == 5:
            questoes.append(questao)
            questao = []
    return questoes


# Função utilizada para atualização do banco de perguntas do quiz
def atualizar_pergunta(perguntas, opcoes):
    frase = "perguntas (2).txt"
    arquivo = open(frase, "a")
    arquivo.write("\n" + perguntas + "\n")
    opcoes = opcoes.split("/")
    for x in opcoes:
        arquivo.write(x + "\n")


# Sorteando as perguntas aleatoriamente
def perguntas_aleatorias(missoes):
    missao = random.choice(missoes)
    return missao


# Verifica se o usuário respondeu certo
def validacao_resposta(resposta, missao):
    if resposta in missao[4]:
        validacao = True
    else:
        validacao = False
    return validacao


pontuacao_total = 0


# Irá atribuir a pontuação ao histórico do jogador
def pontuacao_jogador(jogador, pontos):
    pontos_jogador = []
    pontos_jogador.append(jogador)
    pontos_jogador.append(pontos)
    return pontos_jogador


# Contador que irá atribuir pontuações diferentes ao jogador
def pontuacao(missao, pontos, jogador):
    posicao = []
    if "Normal" in missao[0]:
        pontos += 10
    elif "Medium" in missao[0]:
        pontos += 15
    elif "Hard" in missao[0]:
        pontos += 20
    global pontuacao_total
    pontuacao_total += pontos
    posicao.append(jogador)
    posicao.append(pontuacao_total)
    return posicao

# Irá interagir com o usuário para dar início ao game.

pontuacao_jogador1 = 0
jogador1_pontos = 0
resposta = 5
rank = []

# Ponto de início para o usuário interagir com o programa do Quiz
while resposta != 0:
    print("Bem vindo ao mundo Geek, você está preparado?!")
    jogador0 = input("Digite o nome do jogador: ")
    print("Menu: \n1- Para iniciar sua jornada \n2- Para introduzir seu conhecimento no nosso banco \n0- Caso você queira desistir e não tenha coragem!")
    resposta = int(input())
    resposta_da_missao = inserir_perguntas()
    n = len(resposta_da_missao)

    # Irá verificar a resposta do usuário e dará início as perguntas do quiz.
    if resposta == 1:
        for x in range(0, n):
            pergunta = perguntas_aleatorias(resposta_da_missao)
            resposta_da_missao.remove(pergunta)
            for linha in (range(0, len(pergunta) - 1)):
                print(f"{pergunta[linha]}", end ='')
            resposta1 = input().upper()
            if resposta1 == "0":
                resposta = 0
                break
            correta = validacao_resposta(resposta1, pergunta)
            if resposta1 == "":
                correta = False
            if correta:
                print("Parabéns, jovem guerreiro! Você acertou")
                rank = pontuacao(pergunta, pontuacao_jogador1, jogador0)
                jogador1_pontos = rank[1]
                pontuacao_jogador(jogador0, jogador1_pontos)

            else:
                print("Que pena, continue lutando, você irá conseguir!")

            # Adiciona uma pergunta diretamente no arquivo!
    if resposta == 2:
            questao = input("Digite o conhecimento que deseja somar conosco: ")
            print("Pedimos que você insira neste modelo as alternativas - [A - Harry Potter/B- Voldemort/C- Bilbo Bolseiro/C")
                
            print("As alternativas devem ser colocadas separadas por uma barra e a resposta correta em letra maiúscula!")
            opcoes = input("Digite as alternativas da sua questão: ")
            atualizar_pergunta(questao, opcoes)

    if resposta == 0:
        break

print("Você irá fugir do desafio? Ok, até a proxima!")

