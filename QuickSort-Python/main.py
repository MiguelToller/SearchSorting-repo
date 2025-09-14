from util import quick_sort, get_metricas

vetor = [9, 4, 6, 2, 7, 3, 8, 1, 5]
quick_sort(vetor, 0, len(vetor) - 1)

comparacoes, trocas = get_metricas()

print("Vetor ordenado:", vetor)
print("Comparações:", comparacoes)
print("Trocas:", trocas)