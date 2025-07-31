import random

class Util:
    """_summary_
        Classe responsável por métodos de gestão de listas de números inteiros e listas de palavras
    """

    @staticmethod
    def popular_aleatorio_numeros(lista, quantidade, inicio, fim):
        """_summary_
        método de classe que popula uma lista de números inteiros com valores aleatórios
            
        Args:
            lista (int):
            quantidade (int): 
            inicio (int): 
            fim (int): 
        """
        for _ in range(quantidade):
            numero = random.randrange(inicio, fim)
            lista.append(numero)

    @staticmethod
    def popular_aleatorio_palavras(lista, quantidade, tamanho):
        """_summary_
        método de classe que gera palavras aleatórias

        Args:
            lista (string):
            quantidade (int):
            tamanho (int):
        """
        letras = "abcdefghijklmnopqrstuvwxyz "

        for _ in range(quantidade):
            palavra_gerada = ""
            
            for _ in range(tamanho):
                letra_sorteada = random.choice(letras)
                palavra_gerada += letra_sorteada
            
            lista.append(palavra_gerada)

    @staticmethod
    def exibir_lista(lista):
        """_summary_
        exibe uma lista

        Args:
            lista (any):
        """
        for item in lista:
            print(item)