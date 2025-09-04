## O que é ordenação e por que é importante ordenar estrutura de dados?
Ordenação é o processo de organizar um conjunto de dados em uma determinada ordem, geralmente crescente ou decrescente, com base em algum critério.
Ordenar estruturas de dados é importante para melhorar o desempenho e a eficiência de várias operações, como busca e análise de dados.

## Explique o que é estabilidade e complexidade, quais métodos estudados são estáveis e instáveis?
Um algoritmo de ordenação é estável quando ele mantém a ordem relativa dos elementos com valores iguais.
A complexidade mede o desempenho do algoritmo, especialmente em termos de tempo de execução e uso de memória.

## Dos métodos estudados, quais suas complexidades? Como é avaliada a complexidade de um método de ordenação?
| Método           | Memória          | Estabilidade | Complexidade           | Porção Ordenada |
|-----------------|-----------------|-------------|----------------------|----------------|
| Bubble Sort      | Interna         | Estável     | O(n²)                | Final          |
| Selection Sort   | Interna         | Instável    | O(n²)                | Inicial        |
| Insertion Sort   | Interna         | Estável     | O(n²), ótimo O(n)    | Inicial        |
| Comb Sort        | Interna         | Instável    | O(n²) pior caso      | Final          |
| Shake Sort       | Interna         | Estável     | O(n²)                | Inicial/Final  |
| Shell Sort       | Interna         | Instável    | O(n log² n)          | Null           | 
| Heap Sort        | Interna         | Instável    | O(n log n)           | Final          |
| Merge Sort       | Interna/Externa | Estável     | O(n log n)           | Total          |
| Quick Sort       | Interna         | Instável    | O(n log n) médio     | Indefinida     |
| Bucket Sort      | Interna         | Estável     | O(n + k)             | Grupos         |
| Radix Sort       | Interna         | Estável     | O(n·k)               | Final          |

## Dos métodos estudados, qual o melhor método de ordenação?
Para grandes volumes de dados: Merge Sort ou Quick Sort (apesar de instável, é muito rápido).
Para dados pequenos ou quase ordenados: Insertion Sort.
Quando estabilidade é essencial: Merge Sort ou Radix Sort.
Comb Sort é uma melhoria do Bubble Sort, mas ainda é O(n²) no pior caso — não é o melhor método para dados grandes.

## Faça um método na sua linguagem de preferência que retorne true/True se a lista enviada como parâmetro está ordenada, o false/False caso contrário

``` python
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
```

## Da a sequência de valores na estrutura abaixo, contabilize quantas comparações e quantas trocas há para os métodos: 
- bolha
- seleção
- pente

### Bolha
```
0   1   2   3   4   5   6   7   8  
30  90  10  20  80  10  20  40  10
30  10  20  80  10  20  40  10  90
10  20  30  10  20  40  10  80  90
10  20  10  20  30  10  40  80  90
10  10  20  20  10  30  40  80  90
10  10  20  10  20  30  40  80  90
10  10  10  20  20  30  40  80  90
```

### Seleção
```
0   1   2   3   4   5   6   7   8  
30  90  10  20  80  10  20  40  10 i=0
10  90  30  20  80  10  20  40  10 i=1
10  10  30  20  80  90  20  40  10 i=2
10  10  10  20  80  90  20  40  30 i=3
10  10  10  20  80  90  20  40  30 i=4
10  10  10  20  20  90  80  40  30 i=5
10  10  10  20  20  30  80  40  90 i=6
10  10  10  20  20  30  40  80  90
```

### Pente
```
0   1   2   3   4   5   6   7   8  
30  90  10  20  80  10  20  40  10
```
