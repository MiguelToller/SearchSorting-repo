
class Sorts:

    @staticmethod
    def bolha(lista):
        houve_troca = True
        qtd_comparacoes = 0
        qtd_trocas = 0
        while (houve_troca):    
            houve_troca = False
            for i in range (len(lista) - 1):
                qtd_comparacoes+=1
                if (lista[i] > lista[i+1]):
                    qtd_trocas+=1
                    houve_troca = True
                    tmp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tmp
                    
        return qtd_comparacoes, qtd_trocas # Medem a complexidade do algoritmo
    
    @staticmethod
    def selecao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0
        for i in range(len(lista) - 1):
            posMenor = i
            for j in range(i+1, len(lista)):
                qtd_comparacoes+=1
                if (lista[j] < lista[posMenor]):
                    posMenor = j
            if (i != posMenor):
                qtd_trocas+=1
                tmp = lista[i]
                lista[i] = lista[posMenor]
                lista[posMenor] = tmp
                
        return qtd_comparacoes, qtd_trocas
    
    
    @staticmethod
    def insercao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0

        for i in range(1, len(lista)):
            tmp = lista[i]
            for j in range(i - 1, -2, -1):
                qtd_comparacoes+=1
                if (tmp < lista[j]):
                    lista[j + 1] = lista[j]
                    qtd_trocas+=1
                else:
                    break

            lista[j + 1] = tmp
            qtd_trocas+=1
            
        return qtd_comparacoes, qtd_trocas
    

    @staticmethod
    def agitacao(lista):
        houve_troca = True
        inicio = 0
        fim = len(lista) - 1
        qtd_comparacoes = 0
        qtd_trocas = 0

        while houve_troca:
            houve_troca = False

            # Esquerda -> Direita
            for i in range(inicio, fim):
                qtd_comparacoes += 1
                if lista[i] > lista[i+1]:
                    qtd_trocas += 1
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    houve_troca = True

            if not houve_troca:
                break

            fim -= 1
            houve_troca = False

            # Direita -> Esquerda
            for i in range(fim, inicio, -1):
                qtd_comparacoes += 1
                if lista[i] < lista[i-1]:
                    qtd_trocas += 1
                    lista[i], lista[i-1] = lista[i-1], lista[i]
                    houve_troca = True

            inicio += 1

        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def pente(lista):
        houve_troca = True
        distancia = len(lista)
        qtd_comparacoes = 0
        qtd_trocas = 0

        while houve_troca or distancia > 1:
            # Determina a distancia
            distancia = max(1, int(distancia / 1.3))
            houve_troca = False

            # Percorre a lista comparando os elementos separados pela distancia
            for i in range(len(lista) - distancia):
                qtd_comparacoes += 1
                if lista[i] > lista[i + distancia]:
                    lista[i], lista[i + distancia] = lista[i + distancia], lista[i]
                    qtd_trocas += 1
                    houve_troca = True  

        return qtd_comparacoes, qtd_trocas
    
    def shell(vetor):
        n = len(vetor)
        qtd_comparacoes = 0
        qtd_trocas = 0
        distancia = 1
        referencia_tamanho = 3

        # Calcula o gap inicial usando a sequência de Knuth
        while distancia < n:
            distancia = referencia_tamanho * distancia + 1

        while distancia > 1:
            distancia = distancia // referencia_tamanho

            for i in range(distancia, n):
                tmp = vetor[i]
                j = i - distancia
                while j >= 0:
                    qtd_comparacoes += 1
                    if tmp < vetor[j]:
                        vetor[j + distancia] = vetor[j]
                        qtd_trocas += 1
                        j -= distancia
                    else:
                        break
                vetor[j + distancia] = tmp
                qtd_trocas += 1

        print("Quantidade de comparações:", qtd_comparacoes)
        print("Quantidade de trocas:", qtd_trocas)
        return vetor