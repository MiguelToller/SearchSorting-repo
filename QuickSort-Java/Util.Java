public class Util {
    private static int qtdComparacoes = 0;
    private static int qtdTrocas = 0;

    public static int particiona(int[] vetor, int ini, int fim) {
        int pivo = ini;

        while (fim > ini) {
            while (fim > pivo && vetor[fim] > vetor[pivo]) {
                fim--;
                qtdComparacoes++;
            }

            if (fim > pivo) {
                qtdTrocas++;
                int temp = vetor[pivo];
                vetor[pivo] = vetor[fim];
                vetor[fim] = temp;
                pivo = fim;
            }

            ini++;
            while (ini < pivo && vetor[ini] < vetor[pivo]) {
                ini++;
                qtdComparacoes++;
            }

            if (ini < pivo) {
                qtdTrocas++;
                int temp = vetor[pivo];
                vetor[pivo] = vetor[ini];
                vetor[ini] = temp;
                pivo = ini;
            }
        }
        return pivo;
    }

    public static void quickSort(int[] vetor, int ini, int fim) {
        if (ini < fim) {
            int pivo = particiona(vetor, ini, fim);

            if (ini < pivo - 1) {
                quickSort(vetor, ini, pivo - 1);
            }
            if (pivo + 1 < fim) {
                quickSort(vetor, pivo + 1, fim);
            }
        }
    }

    public static int[] getMetricas() {
        return new int[]{qtdComparacoes, qtdTrocas};
    }
}