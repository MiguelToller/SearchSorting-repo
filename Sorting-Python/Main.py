import time

from Util import Util
from Sorts import Sorts

lista_bolha = []
lista_normal = []
lista_selecao = []
lista_insercao = []
lista_agitacao = []

tamanho = 10000

Util.popular_lista_aleatoria(lista_bolha, tamanho, 10000, 20000)
lista_normal.extend(lista_bolha)
lista_selecao.extend(lista_bolha)
lista_insercao.extend(lista_bolha)
lista_agitacao.extend(lista_bolha)

# Sort
tempoInicio = time.perf_counter()
lista_normal.sort()
tempoFim = time.perf_counter()
tempo_sort = tempoFim - tempoInicio
print("Tempo da rotina ordenar por sort nativo: ",  tempo_sort, "s")        

# Bolha
tempoInicio = time.perf_counter()
qtd_comparacoes, qtd_trocas = Sorts.bolha(lista_bolha)
tempoFim = time.perf_counter()
tempo_bolha = tempoFim - tempoInicio
print("Tempo da rotina ordenar por bolha: ", tempo_bolha , "s")      
print('Comparacoes:', qtd_comparacoes)
print('Trocas:', qtd_trocas)  

# Selecao
tempoInicio = time.perf_counter()
qtd_comparacoes, qtd_trocas = Sorts.selecao(lista_selecao)
tempoFim = time.perf_counter()
tempo_selecao = tempoFim - tempoInicio
print("Tempo da rotina ordenar por selecao: ", tempo_selecao , "s")      
print('Comparacoes:', qtd_comparacoes)
print('Trocas:', qtd_trocas)  

# Insercao
tempoInicio = time.perf_counter()
qtd_comparacoes, qtd_trocas = Sorts.insercao(lista_insercao)
tempoFim = time.perf_counter()
tempo_insercao = tempoFim - tempoInicio
print("Tempo da rotina ordenar por insercao: ", tempo_insercao , "s")      
print('Comparacoes:', qtd_comparacoes)
print('Trocas:', qtd_trocas)  


# Agitacao
tempoInicio = time.perf_counter()
qtd_comparacoes, qtd_trocas = Sorts.agitacao(lista_agitacao)
tempoFim = time.perf_counter()
tempo_agitacao = tempoFim - tempoInicio
print("Tempo da rotina ordenar por agitacao: ", tempo_agitacao , "s")      
print('Comparacoes:', qtd_comparacoes)  
print('Trocas:', qtd_trocas)  