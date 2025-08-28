# Métodos de Ordenação

## BOLHA - Bubble Sort
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

## SELEÇÃO - Selection Sort
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

## INSERÇÃO - Insertion Sort - O(n^2)
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

## Qual o melhor método de ordenação?
**Depende:** tamanho da estrutura; de como a estrutura já está previamente ordenada;

## AGITAÇÃO - Shake Sort ou Cocktail
- É baseado no Bolha, ou seja, é uma tentantiva de melhorar o Bolha.
- Estável
- Memória Interna
- A estrutura possui 3 partes/porções (1a é a ordenada pelos menores; 2a é a desordenada; 3a é a ordenada pelos maiores)

De fato é a aplicação do bolha da esquerda para direita e depois da direita para esquerda

Há os índices/ponteiros ini e fim que marcam o início e o final da estrutura

Observação: 
    i) se a estrutura estiver ordenada ou quase, o agitação terá excelente desempenho, como o bolha
    ii) atenção a lista deve ser duplamente encadeada  

ini = 1
fim = 4

0   1   2   3   4   5   6
7   1   4   2   3   9   8
1   4   2   3   7   8   9
1   2   4   3   7   8   9
1   2   3   4   7   8   9
1   2   3   4   7   8   9

```java
void agitacao(List<> lista) {
    boolean houveTroca;
    int tmp;
    int ini = 0;
    int fim = lista.size();
    int qtdComparacoes = 0, qtdTrocas = 0;

    do {
        houveTroca = false;
        for (int i = 0; i < fim-1; i++){
            qtdComparacoes++;
            if (lista.get(i) > lista.get(i+1)) {
                qtdTrocas++;
                houveTroca = True;
                tmp = lista.get(i);
                lista.set(i, lista.get(i+1));
                lista.set(i+1, tmp);
            }
        }

        if (!houveTroca) {
            break;
        }
        fim--;

        houveTroca = False;
        for (int i = fim; i > ini+1; i--){
            qtdComparacoes++;
            if (lista.get(i) < lista.get(i-1)) {
                qtdTrocas++;
                houveTroca = True;
                tmp = lista.get(i);
                lista.set(i, lista.get(i-1);
                lista.set(i-1, tmp);
            }
        }
        ini++;

    } while (houveTroca);
}
```

## PENTE - Comb Sort
- É baseado no Bolha, ou seja, é uma tentantiva de melhorar o Bolha.
- Instável
- Memória Interna

ATENÇÃO: a partir deste método, há COMPARAÇÕES a uma distância X. Isso gera uma pré-organização da estrutura, diminuindo número de comparações e trocas.

A estrutura possui 2 porções/partes (1a é a ordenada; 2a é a desordenada)

Há as variáveis clássicas do bolha: i, houveTroca, tmp.
Há a variável distancia que é calculada pelo tamanho da estrutura dividido por 1.3

Adequado somente para listas ou estruturas prontas tipo lista de uma linguagem de programação

n = 7
0   1   2   3   4   5   6   
7   1   4   2   3   9   8       distancia = (int)n / 1.3 = 5
7   1   4   2   3   9   8       distancia = (int)distancia / 1.3 = 3
2   1   4   7   3   9   8       distancia = (int)distancia / 1.3 = 2
2   1   3   7   4   9   8       distancia = (int)distancia / 1.3 = 1
1   2   3   4   7   8   9       distancia = (int)distancia / 1.3 = 1
1   2   3   4   7   8   9

```java
void pente(List<> lista) {
    bool houveTroca;
    int tmp;
    int distancia = lista.Count();
    int qtdComparacoes = 0, qtdTrocas = 0;

    do {
        distancia = (int)distancia / 1.3;
        houveTroca = false;
        for (int i = 0; i+distancia < lista.Count(); i++){
            qtdComparacoes++;
            if (lista[i] > lista[i+distancia]) {
                qtdTrocas++;
                houveTroca = True;
                tmp = lista[i];
                lista[i] = lista[i+distancia];
                lista[i+distancia] = tmp;
            }
        }
    } while (houveTroca || distancia > 1);
}
```

6) SHELLSORT 
    É baseado no Inserção, ou seja, é uma tentativa de melhoria via o uso da ANÁLISE A DISTÂNCIA (tipo pente)
    Instável 
    Memória Interna

    Não é adequado para listas encadeadas

n = 7
0   1   2   3   4   5   6   
7   1   4   2   3   9   8       distancia = 4

```c#
void shell(Lista<> lista) {
    int i, j;
    int tmp;
    int qtdComparacoes = 0, qtdTrocas = 0;
    int distancia = 1;

    int referenciaTamanho = 3;

    do {
        distancia = referenciaTamanho * distancia + 1;
    } while (distancia < n);
    
    do {
        distancia = (int)(distancia / referenciaTamanho);
        
        for (i = distancia; i < n; i++) {
            tmp = vetor[i];
            for (j = i - distancia; j >= 0; j = j - distancia) {
                qtdComparacoes++;
                if (tmp < vetor[j]) {
                    vetor[j + distancia] = vetor[j];
                    qtdTrocas++;
                } else break;
            }
            vetor[j + distancia] = tmp;
            qtdTrocas++;
        }
    } while (distancia > 1);
}
```
