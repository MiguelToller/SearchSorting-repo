# Métodos de Ordenação

## 1) BOLHA - Bubble Sort
- Estável  
- Memória Interna  
- Alta complexidade (muito esforço) - O(n^2)  
- A estrutura possui 2 partes/porções (1ª é a desordenada; 2ª parte é a ordenada)  
- Adequado para listaes e listas  

Trabalha com o conceito de trocas, ou seja, enquanto houver trocas, o algoritmo não para.  
É considerado bolha, porque 'leva' os maiores para o final da estrutura.  

**Observação:** se a estrutura estiver ordenada ou quase, o bolha terá excelente desempenho.  

0 1 2 3 4 5 6
7 1 4 2 3 9 8
1 4 2 3 7 8 9
1 2 3 4 7 8 9
1 2 3 4 7 8 9

```java
void bolha(List<> lista) {
    boolean houveTroca;
    int tmp;
    int qtdComparacoes = 0, qtdTrocas = 0;

    do {
        houveTroca = False;
        for (int i = 0; i < lista.size()-1; i++){
            qtdComparacoes++;
            if (lista.get(i) > lista.get(i+1)) {
                qtdTrocas++;
                houveTroca = True;
                tmp = lista.get(i);
                lista.set(i, lista.get(i+1));
                lista.set(i+1, tmp);
            }
        }
    } while (houveTroca);
}
```

## 2) SELEÇÃO - Selection Sort
- Instável
- Memória Interna
- Alta complexidade (muito esforço) - O(n^2)
- A estrutura possui 2 partes/porções (1a é a ordenada; 2a parte é a desordenada)
- Adequado para listaes e listas

Trabalha com conceito de trocas não contíguas. É considerado seleção porque ele seleciona os menores para
o início da estrutura

**Observação:** se a estrutura estiver ordenada, o método vai funcionar/processar como se a estrutura estivesse desordenada.

0   1   2   3   4   5   6    posMenor = 1
7   1   4   2   3   9   8
1   7   4   2   3   9   8
1   2   4   7   3   9   8
1   2   3   7   4   9   8
1   2   3   4   7   9   8
1   2   3   4   7   9   8
1   2   3   4   7   8   9
1   2   3   4   7   8   9  

```java
void selecao(List<> lista) {
    int posMenor;
    int qtd_comparacoes = 0, qtd_trocas = 0;
    for (int i = 0; i < lista.size()-1; i++) {
        posMenor = i;
        for (int j = i+1; j < lista.size(); j++) {
            qtd_comparacoes++;
            if (lista.get(j) < lista.get(posMenor)) {
                posMenor = j;
            }
        }
        if (i != posMenor) {
            qtd_trocas++;
            tmp = lista.get(i);
            lista.set(i, lista.get(posMenor));
            lista.set(posMenor, tmp);
        }
    }
}
```

## 3) INSERÇÃO - Insertion Sort - O(n^2)
- Estável
- Memória Interna
- Alta complexidade - O(n^2)
- A estrutura possui 2 partes/porções (1a é a ordenada; 2a parte é a desordenada)
- Adequado para listaes e listas

Trabalha com o conceito de inserção na porção inicial, com isso, pode diminuir o número de comparações

**Observação:** i) se a estrutura estiver ordenada ou quase, o inserção terá excelente desempenho

0   1   2   3   4   5   6
7   1   4   2   3   9   8
1   7   4   2   3   9   8
1   4   7   2   3   9   8
1   2   4   7   3   9   8
1   2   3   4   7   9   8
1   2   3   4   7   9   8
1   2   3   4   7   8   9   

```java
void insercao(Lista<> lista) {
    int i, j;
    int tmp;
    int qtdComparacoes = 0, qtdTrocas = 0;

    for (i = 1; i < n; i++) {
        tmp = lista.get(i);
        for (j = i - 1; j >= 0; j--) {
            qtdComparacoes++;
            if (tmp < lista.get(j)) {
                lista.set(j + 1, lista.get(j));
                qtdTrocas++;
            } else break;
        }
        lista.set(j + 1, tmp);
        qtdTrocas++;
    }
}
```

Qual o melhor método de ordenação?
Depende: tamanho da estrutura; de como a estrutura já está previamente ordenada;