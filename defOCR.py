from PIL import Image
import pytesseract
import numpy as np
import cv2
import imutils
from pytesseract import Output
import sys
#url = sys.argv[1]

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\felip\AppData\\Local\Tesseract-OCR\tesseract'
palavras = []

#imagem = cv2.imread('textopy.png')
#imagem = io.imread('https://www.grupoescolar.com/wp-content/uploads/2021/03/o-que-e-um-texto-D5.jpg')
url = 'https://firebasestorage.googleapis.com/v0/b/fapen-bank.appspot.com/o/imagem.jpeg?alt=media&token=e8f590a9-4b22-4276-bba9-f15bd44b03e5'
imagem = imutils.url_to_image(url)
imagemRGB = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

def destacaPalavras(caminho, confia, ling, color, tamBorda):
  imagem = imutils.url_to_image(url)
  rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
  res = pytesseract.image_to_data(rgb, config='3♥', lang=ling, output_type=Output.DICT)
  for ind in range(0,len(res['text'])):
    resConf = int(res['conf'][ind])
    if(resConf >= confia):
      xCoord = res['left'][ind]
      yCoord = res['top'][ind]
      larg = res['width'][ind]
      alt = res['height'][ind]
      cv2.rectangle(rgb, (xCoord,yCoord), (xCoord + larg, yCoord+alt),
                    color, tamBorda)
  return rgb

text=pytesseract.image_to_data(imagemRGB,config="",lang='por',output_type=Output.DICT)['text']

for dado in text:
    if(dado=='' or dado==' ' or dado=='   ' or dado=='   '):
        text.remove(dado)

print(text)

#imagem2 = destacaPalavras(url, 60, 'por', (255,1,1),2)

#cv2.imshow('', imagemRGB)
#cv2.waitKey(0)

