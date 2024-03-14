# Caio Cesar Vieira | Exemplo 2 do capítulo 2

# Importação das bibliotecas (OpenCV)
import cv2

# Leitura da imagem com a função -imread(<nome_da_imagem>)- 
imagem = cv2.imread(r'ETAPA_1//Missao_2//Cap_2//Imagem//pordosol.jpg')

# Varredura da matriz composta pelos pixels da imagem, e modificando todos os
# pixels para a cor azul, representado no padrão BGR 

for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (255,0,0)

# Exibição da nova imagem
cv2.imshow("Imagem modificada", imagem)