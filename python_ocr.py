from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'C://Users//roberto.silva//AppData//Local//Programs//Tesseract-OCR//tesseract.exe'

imagem_1="imagem_1.png"
imagem_2="imagem_2.png"

pytesseract.image_to_string(imagem_1)
pytesseract.image_to_string(imagem_2)
