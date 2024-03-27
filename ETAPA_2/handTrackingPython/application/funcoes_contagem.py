# Caio Cesar Vieira
# Script para salvar funções essenciais no pattern da mão, lembrando que nesse caso só vale para a mão ESQUERDA
# Na pasta HAND PATTERN, é possível analisar os padrões criados para essa contagem de 0 a 15

def dedo_levantado(superior, inferior):
    return superior < inferior


def contagem_dedos(pontos):
    dedao = dedo_levantado(pontos[4][0], pontos[2][0])
    indicador = dedo_levantado(pontos[8][1], pontos[6][1])
    medio = dedo_levantado(pontos[12][1], pontos[10][1])
    anelar = dedo_levantado(pontos[16][1], pontos[14][1])
    mindinho = dedo_levantado(pontos[20][1], pontos[18][1])

    if not dedao and indicador and not medio and not anelar and not mindinho:
        return 1
    if not dedao and indicador and medio and not anelar and not mindinho:
        return 2
    if dedao and indicador and medio and not anelar and not mindinho:
        return 3
    if not dedao and indicador and medio and anelar and mindinho:
        return 4
    if dedao and indicador and medio and anelar and mindinho:
        return 5
    if not dedao and indicador and medio and anelar and not mindinho:
        return 6
    if not dedao and indicador and medio and not anelar and mindinho:
        return 7
    if not dedao and indicador and not medio and anelar and mindinho:
        return 8
    if not dedao and not indicador and medio and anelar and mindinho:
        return 9
    if dedao and not indicador and not medio and not anelar and not mindinho:
        return 10
    if dedao and indicador and not medio and not anelar and not mindinho:
        return 11
    if dedao and indicador and not medio and not anelar and mindinho:
        return 12
    if not dedao and indicador and not medio and not anelar and mindinho:
        return 13
    if not dedao and not indicador and not medio and not anelar and mindinho:
        return 14
    if dedao and not indicador and not medio and not anelar and mindinho:
        return 15
    return 0
