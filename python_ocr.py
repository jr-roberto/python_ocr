from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'<SEU_CAMINHO_DO_EXECUTAVEL_PYTESSERACT>//tesseract.exe'

imagem_1="imagem_1.png"
imagem_2="imagem_2.png"

print("Imagem 1 :",pytesseract.image_to_string(imagem_1))
# >> '118,86\n'

print("Imagem 2 :",pytesseract.image_to_string(imagem_2))
# >> ''
