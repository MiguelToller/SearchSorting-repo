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

    @staticmethod
    def popular_numero_arquivo(caminho_arquivo, quantidade, inicio, fim):
        """_summary_
        método de classe que popula um arquivo com números inteiros aleaatórios
        Args:
            caminhoArquivo (string): 
            quantidade (int): 
            inicio (int): 
            fim (int): 
        """
        try:
            with open(caminho_arquivo, "w") as arquivo:
                for _ in range(quantidade):
                    numero = random.randint(inicio, fim)
                    arquivo.write(f"{numero}\n")
        except IOError as e:
            print(f"Erro ao escrever no arquivo: {e}")

    @staticmethod
    def popular_palavra_arquivo(caminho_arquivo, quantidade, tamanho):
        """_summary_
        método de classe que popula um arquivo com palavras aleatórias
        Args:
            caminho_arquivo (string): 
            quantidade (int): 
            tamanho (int): 
        """
        letras = "abcdefghijklmnopqrstuvwxyz "
        
        try:
            with open(caminho_arquivo, "w") as arquivo:
                for _ in range(quantidade):
                    palavra_gerada = ""
                    
                    for _ in range(tamanho):
                        letra_sorteada = random.choice(letras)
                        palavra_gerada += letra_sorteada
                    
                    arquivo.write(f"{palavra_gerada}\n")
                    
        except IOError as e:
            print(f"Erro ao escrever no arquivo: {e}")
            
    
    @staticmethod
    def ler_arquivo(caminho_arquivo):
        """_summary_
        método de classe que lê o conteúdo de um arquivo .txt
        Args:
            caminho_arquivo (string): 
        """
        try:
            with open(caminho_arquivo, "r") as arquivo:
                for linha in arquivo:
                    print(linha, end='')
        except IOError as e:
            print(f"Erro ao ler o arquivo: {e}")