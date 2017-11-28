from collections import Counter
arq = open('C:/Users/luiz.junior/Desktop/ocr.txt', 'r')
texto_longo = arq.read()
palavras = texto_longo
contador = Counter(palavras)
for i in contador.items():
        print(i)
