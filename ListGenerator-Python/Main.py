from Util import Util

lista_numeros = []
lista_palavras = []

'''
Util.popular_aleatorio_numeros(lista_numeros, 5, 0, 10)
Util.popular_aleatorio_palavras(lista_palavras, 5, 5)
    
Util.exibir_lista(lista_numeros)
Util.exibir_lista(lista_palavras)
'''

caminho_arquivo = "ListGenerator-Python/arquivo.txt"

Util.popular_numero_arquivo(caminho_arquivo, 5, 0, 10)
Util.ler_arquivo(caminho_arquivo)

Util.popular_palavra_arquivo(caminho_arquivo, 5, 5)
Util.ler_arquivo(caminho_arquivo)