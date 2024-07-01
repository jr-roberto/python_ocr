from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'<SEU_CAMINHO_DO_EXECUTAVEL_PYTESSERACT>//tesseract.exe'

# SOLUÇÃO 1
def tratando_img(imagem):
    from PIL import Image
    import numpy as np

    # Abrir a imagem
    # imagem = Image.open(r'C:\Users\roberto.silva\projetos\robo_mega_lancamento_nf\PYTHON_OCR\imagem_2_result.png')

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
    # imagem_alterada.save('imagem_alterada.png')

    return imagem_alterada

imagem_1="imagem_1.png"
imagem_2="imagem_2.png"

print("Imagem 1 :",pytesseract.image_to_string(imagem_1))
# >> '118,86\n'

print("Imagem 2 :",pytesseract.image_to_string(imagem_2))
# >> ''
