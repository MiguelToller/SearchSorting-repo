qtd_comparacoes = 0
qtd_trocas = 0

def particiona(vetor, ini, fim):
    global qtd_comparacoes, qtd_trocas

    pivo = ini

    while fim > ini:
        # Direita para esquerda
        while fim > pivo and vetor[fim] > vetor[pivo]:
            fim -= 1
            qtd_comparacoes += 1

        if fim > pivo:
            qtd_trocas += 1
            vetor[pivo], vetor[fim] = vetor[fim], vetor[pivo]
            pivo = fim

        # Esquerda para direita
        ini += 1
        while ini < pivo and vetor[ini] < vetor[pivo]:
            ini += 1
            qtd_comparacoes += 1

        if ini < pivo:
            qtd_trocas += 1
            vetor[pivo], vetor[ini] = vetor[ini], vetor[pivo]
            pivo = ini

    return pivo

def quick_sort(vetor, ini, fim):
    if ini < fim:
        pivo = particiona(vetor, ini, fim)

        if ini < pivo - 1:
            quick_sort(vetor, ini, pivo - 1)
        if pivo + 1 < fim:
            quick_sort(vetor, pivo + 1, fim)

def get_metricas():
    return qtd_comparacoes, qtd_trocas