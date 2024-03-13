# Caio Cesar Vieira | Exemplo do capítulo 1

# Importação das bibliotecas (OpenCV)
import cv2 

# Leitura da imagem com a função -imread(<nome_da_imagem>)- 
imagem = cv2.imread('entrada.jpg') 
print('Largura em pixels: ', end='') 
print(imagem.shape[1]) #largura da imagem 
print('Altura em pixels: ', end='') 
print(imagem.shape[0]) #altura da imagem 
print('Qtde de canais: ', end='') 
print(imagem.shape[2]) 

# Mostra a imagem com a função -imshow(<nome_da_janela, <imagem>)- 
cv2.imshow("Nome da janela", imagem) 

cv2.waitKey(0) #espera pressionar qualquer tecla

# Salvar a imagem no disco com função -imwrite(<novo_nome>, <imagem>)- 
cv2.imwrite("saida.jpg", imagem)