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
}