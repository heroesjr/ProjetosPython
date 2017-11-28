from collections import Counter
arq = open('caminho_geral_do_arquivo', 'r')
texto_longo = arq.read()
palavras = texto_longo
contador = Counter(palavras)
for i in contador.items():
        print(i)
