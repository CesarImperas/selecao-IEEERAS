# Caio Cesar Vieira ; Contador de dedos (0 a 15) da mão ESQUERDA

# Importando as bibliotecas
import cv2
import mediapipe as mp
from funcoes_contagem import contagem_dedos

# Iniciando a captura em tempo real pela webcam
video = cv2.VideoCapture(0)

# Responsável pelas configurações do mediapipe (h minúsculo)
hand = mp.solutions.hands

# Configuração/Detecção de quantas mãos serão utilizadas (nesse caso somente 1)
Hand = hand.Hands(max_num_hands=1)

# Responsável por desenhar os pontos na(s) mão(s)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    # Conversão da imagem de BGR para RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Processar a imagem com mediapipe
    results = Hand.process(imgRGB)

    # Extrair informações da imagem
    # Coordenadas dos pontos a serem identificados
    handsPoints = results.multi_hand_landmarks

    # Dimensão da imagem (webcam)
    h, w, _ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:

            # Desenhando agora os traços para as coordenadas das mãos (utilizando a variável mpDraw, passando a imagem, os pontos e a mão)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)

            # Enumerar cada ponto da mão
            for id, coord in enumerate(points.landmark):
                cx, cy = int(coord.x * w), int(coord.y * h)

                # Comando da linha abaixo serve como guia para os pontos da mão pela documentação do mediapipe
                # cv2.putText(img, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                # Incrementando na lista de pontos, as coordenadas x e y em tupla
                pontos.append((cx, cy))

        contador = 0
        if points:
            # Função responsável por pegar a lista das coordenadas dos pontos de cada mão, e realizar a contagem dos dedos levantados
            contador = contagem_dedos(pontos)

        cv2.rectangle(img, (80, 10), (240, 100), (255, 0, 0), -1)
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)

    # Exibição da captura com uma janela de nome "Imagem"
    cv2.imshow("Contagem dedos by Caio", img)
    cv2.waitKey(1)
