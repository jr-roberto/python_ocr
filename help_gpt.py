# https://chatgpt.com/share/9a598a49-f414-4960-a670-ecf9d0e5d1ce
from PIL import Image
import numpy as np

# Abrir a imagem
imagem = Image.open('caminho_para_a_imagem.jpg')

# Converter a imagem para array numpy
imagem_np = np.array(imagem)

# Definir a cor que será substituída e a nova cor
cor_antiga = np.array([247, 243, 247])
nova_cor = np.array([255, 255, 255])

# Encontrar os pixels que correspondem à cor antiga e substituí-los pela nova cor
mask = np.all(imagem_np == cor_antiga, axis=-1)
imagem_np[mask] = nova_cor

# Escurecer os pixels que são diferentes da cor antiga
imagem_np[~mask] = (imagem_np[~mask] * 0.5).astype(np.uint8)

# Converter o array numpy de volta para uma imagem
imagem_alterada = Image.fromarray(imagem_np)

# Salvar a imagem alterada
imagem_alterada.save('imagem_alterada.jpg')
