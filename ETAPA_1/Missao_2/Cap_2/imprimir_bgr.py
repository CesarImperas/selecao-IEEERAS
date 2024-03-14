# Caio Cesar Vieira | Exemplo 1 do capítulo 2

# Importação das bibliotecas (OpenCV)
import cv2

# Leitura da imagem com a função -imread(<nome_da_imagem>)- 
imagem = cv2.imread(r'ETAPA_1//Missao_2//Cap_2//Imagem//pordosol.jpg')
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB

# Exibir na tela as cores correspondente ao pixel (0,0)
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)