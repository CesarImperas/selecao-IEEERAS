# Caio Cesar Vieira | Exemplo 3,4 e 5 do capítulo 2

# Importação das bibliotecas (OpenCV)
import cv2

# Leitura da imagem com a função -imread(<nome_da_imagem>)- 
imagem = cv2.imread(r'ETAPA_1//Missao_2//Cap_2//Imagem//pordosol.jpg')

# Semelhante ao exemplo anterior, contudo mudando através do cálculo entre o valor de x e y, pelo módulo de 256
for y in range(0, imagem.shape[0]): #percorre linhas
    for x in range(0, imagem.shape[1]): #percorre colunas
        imagem[y, x] = (x%256,y%256,x%256)

# Exibição da nova imagem
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Gerando outra imagem, agora realizando o cálculo (x*y)%256 na cor verde
for y in range(0, imagem.shape[0], 1): 
    for x in range(0, imagem.shape[1], 1): 
        imagem[y, x] = (0,(x*y)%256,0)


cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Retornando a imagem original
imagem = cv2.imread(r'ETAPA_1//Missao_2//Cap_2//pordosol.jpg')

# Agora formando uma imagem, "saltando" as linhas e colunas em 10 pixels, inserindo um quadrado amarelo 5x5
for y in range(0, imagem.shape[0], 10): 
    for x in range(0, imagem.shape[1], 10): 
        imagem[y:y+5, x: x+5] = (0,255,255)

cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

