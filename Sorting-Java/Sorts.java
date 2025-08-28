import java.util.List;

/**
 * Contem implementações de 3 algoritmos classicos de ordenacao:
 * - Ordenação por bolha (Bubble Sort)
 * - Ordenação por selecao (Selection Sort)
 * - Ordenação por insercao (Insertion Sort)
 */
public class Sorts {

    /**
     * O algoritmo percorre repetidamente a lista, comparando elementos adjacentes e trocando-os 
     * de lugar se estiverem na ordem errada. O processo é repetido ate que nao haja mais trocas.
     * @param list
     */
    public static void bolha(List<Integer> list) {

        int n = list.size();
        boolean trocou;
        int trocas = 0;
        int comparacoes = 0;

        do {
            trocou = false;
            for (int i = 0; i < n - 1; i++) {
                comparacoes++;
                if (list.get(i) > list.get(i + 1)) {
                    int temp = list.get(i);
                    list.set(i, list.get(i + 1));
                    list.set(i + 1, temp);
                    trocou = true;
                    trocas++;
                }
            }
            n--;
        } while (trocou);

        System.out.println("Quantidade de comparacoes: " + comparacoes);
        System.out.println("Quantidade de trocas: " + trocas);
    }

    /**
     * O algoritmo percorre a lista e, a cada iteracao, seleciona o menor elemento da parte nao ordenada 
     * e o coloca na posicao correta, trocando-o com o elemento na posicao atual.
     * @param list
     */
    public static void selecao(List<Integer> list) {

        int n = list.size();
        int trocas = 0;
        int comparacoes = 0;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                comparacoes++;
                if (list.get(j) < list.get(minIndex)) {
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                int temp = list.get(i);
                list.set(i, list.get(minIndex));
                list.set(minIndex, temp);
                trocas++;
            }
        }
        System.out.println("Quantidade de comparacoes: " + comparacoes);
        System.out.println("Quantidade de trocas: " + trocas);
    }

    /**
     * O algoritmo percorre a lista da esquerda para a direita, pegando cada elemento e o inserindo 
     * na posicao correta dentro da parte ja ordenada da lista.
     * @param list
     */
    public static void insercao(List<Integer> list) {

        int n = list.size();
        int trocas = 0;
        int comparacoes = 0;

        for (int i = 1; i < n; i++) {
            int key = list.get(i);
            int j = i - 1;

            while (j >= 0 && list.get(j) > key) {
                comparacoes++;
                list.set(j + 1, list.get(j));
                j--;
                trocas++;
            }
            list.set(j + 1, key);
            if (j >= 0) {
                comparacoes++;
            }
        }
        System.out.println("Quantidade de comparacoes: " + comparacoes);
        System.out.println("Quantidade de trocas: " + trocas);
    }

    public static void agitacao(List<Integer> lista) {
        boolean houveTroca;
        int tmp;
        int ini = 0;
        int fim = lista.size() - 1;
        int qtdComparacoes = 0, qtdTrocas = 0;

        do {
            houveTroca = false;
            for (int i = ini; i < fim; i++) {
                qtdComparacoes++;
                if (lista.get(i) > lista.get(i + 1)) {
                    qtdTrocas++;
                    houveTroca = true;
                    tmp = lista.get(i);
                    lista.set(i, lista.get(i + 1));
                    lista.set(i + 1, tmp);
                }
            }
            if (!houveTroca) break;

            fim--;
            houveTroca = false;
            for (int i = fim; i > ini; i--) {
                qtdComparacoes++;
                if (lista.get(i) < lista.get(i - 1)) {
                    qtdTrocas++;
                    houveTroca = true;
                    tmp = lista.get(i);
                    lista.set(i, lista.get(i - 1));
                    lista.set(i - 1, tmp);
                }
            }
            ini++;
        } while (houveTroca);

        System.out.println("Quantidade de comparacoes: " + qtdComparacoes);
        System.out.println("Quantidade de trocas: " + qtdTrocas);
    }

    public static void pente(List<Integer> lista) {
        boolean houveTroca;
        int distancia = lista.size();
        int qtdComparacoes = 0, qtdTrocas = 0;

        do {
            // Reduz a distancia
            distancia = (int)(distancia / 1.3);
            if (distancia < 1) {
                distancia = 1;
            }

            houveTroca = false;

            for (int i = 0; i + distancia < lista.size(); i++) {
                qtdComparacoes++;
                if (lista.get(i) > lista.get(i + distancia)) {
                    qtdTrocas++;
                    houveTroca = true;
                    
                    // Troca elementos
                    int tmp = lista.get(i);
                    lista.set(i, lista.get(i + distancia));
                    lista.set(i + distancia, tmp);
                }
            }
        } while (houveTroca || distancia > 1);

        System.out.println("Quantidade de comparacoes: " + qtdComparacoes);
        System.out.println("Quantidade de trocas: " + qtdTrocas);
    }

}