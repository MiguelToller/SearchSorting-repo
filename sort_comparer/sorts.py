class Sorts:

    @staticmethod
    def bolha(lista):
        houve_troca = True
        qtd_comparacoes = 0
        qtd_trocas = 0
        while houve_troca:    
            houve_troca = False
            for i in range(len(lista) - 1):
                qtd_comparacoes += 1
                if lista[i] > lista[i+1]:
                    qtd_trocas += 1
                    houve_troca = True
                    lista[i], lista[i+1] = lista[i+1], lista[i]
        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def selecao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0
        for i in range(len(lista) - 1):
            posMenor = i
            for j in range(i+1, len(lista)):
                qtd_comparacoes += 1
                if lista[j] < lista[posMenor]:
                    posMenor = j
            if i != posMenor:
                qtd_trocas += 1
                lista[i], lista[posMenor] = lista[posMenor], lista[i]
        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def insercao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0
        for i in range(1, len(lista)):
            tmp = lista[i]
            for j in range(i - 1, -1, -1):  # corrigido aqui
                qtd_comparacoes += 1
                if tmp < lista[j]:
                    lista[j + 1] = lista[j]
                    qtd_trocas += 1
                else:
                    break
            lista[j + 1] = tmp
            qtd_trocas += 1
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
            distancia = max(1, int(distancia / 1.3))
            houve_troca = False
            for i in range(len(lista) - distancia):
                qtd_comparacoes += 1
                if lista[i] > lista[i + distancia]:
                    lista[i], lista[i + distancia] = lista[i + distancia], lista[i]
                    qtd_trocas += 1
                    houve_troca = True  
        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def shell(lista):
        n = len(lista)
        qtd_comparacoes = 0
        qtd_trocas = 0
        distancia = 1
        referencia_tamanho = 3
        while distancia < n:
            distancia = referencia_tamanho * distancia + 1
        while distancia > 1:
            distancia //= referencia_tamanho
            for i in range(distancia, n):
                tmp = lista[i]
                j = i - distancia
                while j >= 0:
                    qtd_comparacoes += 1
                    if tmp < lista[j]:
                        lista[j + distancia] = lista[j]
                        qtd_trocas += 1
                        j -= distancia
                    else:
                        break
                lista[j + distancia] = tmp
                qtd_trocas += 1
        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def quicksort(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0

        def _quicksort(lista, inicio, fim):
            nonlocal qtd_comparacoes, qtd_trocas
            if inicio < fim:
                pivo, comp, troc = partition(lista, inicio, fim)
                qtd_comparacoes += comp
                qtd_trocas += troc
                _quicksort(lista, inicio, pivo - 1)
                _quicksort(lista, pivo + 1, fim)

        def partition(lista, inicio, fim):
            comp = 0
            troc = 0
            pivo = lista[fim]
            i = inicio - 1
            for j in range(inicio, fim):
                comp += 1
                if lista[j] <= pivo:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]
                    troc += 1
            lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
            troc += 1
            return i + 1, comp, troc

        _quicksort(lista, 0, len(lista) - 1)
        return qtd_comparacoes, qtd_trocas

