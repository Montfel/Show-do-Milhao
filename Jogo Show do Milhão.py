import pygame
from time import sleep
from random import randint, choice, choices


def tocar_musica(musica):
    pygame.mixer.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()


perguntas = list()
alternativas = list()
respostas = list()
opcoes = list()
repeticao = list()
contador_perguntas = 0
mil = 'mil'
pulos = contador_eliminar = contador_universitario = 3
show = open('ShowQuestionario.txt', 'r', encoding='utf8')
for line in show:
    line.strip()
    if line.endswith('?\n'):
        perguntas.append(line)
    elif line.startswith('1 ') or line.startswith('2 ') or line.startswith('3 ') or line.startswith('4 '):
        alternativas.append(line)
    elif line.startswith('1') or line.startswith('2') or line.startswith('3') or line.startswith('4'):
        respostas.append(line.translate(str.maketrans('', '', '\n')))
while True:
    if 0 <= contador_perguntas <= 4:
        aleatorio = randint(0, 99)
        dinheiro_acertar = contador_perguntas + 1
        dinheiro_parar = contador_perguntas
        while aleatorio in repeticao:
            aleatorio = randint(0, 99)
        repeticao.append(aleatorio)
    elif 5 <= contador_perguntas <= 9:
        aleatorio = randint(100, 199)
        dinheiro_acertar = 10 * (contador_perguntas - 4)
        dinheiro_parar = 5 * (contador_perguntas - 4)
        while aleatorio in repeticao:
            aleatorio = randint(100, 199)
        repeticao.append(aleatorio)
    elif 10 <= contador_perguntas <= 14:
        aleatorio = randint(200, 298)
        dinheiro_acertar = 100 * (contador_perguntas - 9)
        dinheiro_parar = 50 * (contador_perguntas - 9)
        while aleatorio in repeticao:
            aleatorio = randint(200, 298)
        repeticao.append(aleatorio)
    elif contador_perguntas == 15:
        aleatorio = randint(200, 298)
        dinheiro_acertar = '1 milhão'
        dinheiro_parar = 0
        while aleatorio in repeticao:
            aleatorio = randint(200, 298)
        mil = ''
    aleresp = aleatorio * 4
    tocar_musica('ShowPerguntas.mp3')
    if 10 <= contador_perguntas <= 15:
        tocar_musica('ShowSuspense.mp3')
    print(f'Pergunta número {contador_perguntas + 1}:')
    sleep(2)
    print(perguntas[aleatorio])
    for c in alternativas[aleresp:aleresp + 4]:
        sleep(1)
        print(c, end='')
    sleep(1)
    if contador_perguntas != 15:
        print(f'''\n5 Para chamar os Universitários ({contador_universitario} restante(s))
6 Para eliminar uma alternativa ({contador_eliminar} restante(s))
7 Para Pular ({pulos} pulo(s) restante(s))''')
    print(f'\nAcertar R$ {dinheiro_acertar}{mil}, Parar R$ {dinheiro_parar}{mil}, Errar R$ {(dinheiro_parar/2):.1f}{mil}')
    sleep(0.5)
    resp = input('\nQual a resposta? ')
    sleep(0.5)
    while resp == '5' and contador_universitario == 0 or resp == '6' and contador_eliminar == 0 or resp == '7' and pulos == 0:
        print('\nVocê não pode mais escolher essa opção')
        resp = input('Escolha novamente: ')
    if contador_perguntas != 15:
        if resp == '5' and contador_universitario > 0:
            contador_universitario -= 1
            opcoes = [1, 2, 3, 4]
            opcoes.remove(int(respostas[aleatorio]))
            opcoes.remove(choice(opcoes))
            opcoes.remove(choice(opcoes))
            opcoes.append(int(respostas[aleatorio]))
            print(f'\nOs universitários escolheram a resposta {choices(opcoes, weights=[25, 75])[0]}')
            resp = input('\nQual a sua resposta? ')
        elif resp == '6' and contador_eliminar > 0:
            contador_eliminar -= 1
            opcoes = [1, 2, 3, 4]
            opcoes.remove(int(respostas[aleatorio]))
            opcoes.remove(choice(opcoes))
            opcoes.append(int(respostas[aleatorio]))
            opcoes.sort()
            print()
            for c in range(3):
                print(alternativas[aleresp + opcoes[c] - 1], end='')
            resp = input('\nQual a sua resposta? ')
        elif resp == '7' and pulos > 0:
            pulos -= 1
            print('-' * 30)
            continue
    while resp not in '1234':
        print('\nVocê não pode mais pedir ajuda.')
        resp = input('Escolha novamente entre as opções acima: ')
    sleep(0.5)
    print('\nA Resposta está E', end='')
    sleep(2)
    if resp == respostas[aleatorio]:
        print('xata!')
        sleep(0.5)
        contador_perguntas += 1
        if contador_perguntas == 16:
            tocar_musica('ShowAbertura.mp3')
            print('\nVocê é um novo milionário!!!')
            sleep(50)
            break
        print('-' * 30)
    else:
        print('rrada!')
        tocar_musica('ShowDerrota.mp3')
        print('\nO jogo acabou!')
        print(f'Você ganhou R${dinheiro_parar/2}{mil}')
        sleep(4)
        break