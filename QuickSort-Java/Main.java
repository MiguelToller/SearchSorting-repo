public class Main {
    public static void main(String[] args) {
        int[] vetor = {9, 4, 6, 2, 7, 5};
        Util.quickSort(vetor, 0, vetor.length - 1);

        System.out.println("Vetor ordenado:");
        for (int num : vetor) {
            System.out.print(num + " ");
        }
        System.out.println();

        int[] metricas = Util.getMetricas();
        System.out.println("Comparações: " + metricas[0]);
        System.out.println("Trocas: " + metricas[1]);
    }
}