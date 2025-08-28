import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * E responsavel por testar a performance de diferentes algoritmos de ordenacao:
 */
public class Main {
    public static void main(String[] args) {

        List<Integer> lista = new ArrayList<>();

        // Teste do algoritmo de ordenacao por bolha
        System.out.println("Sort Bolha");
        List<Integer> lista2 = gerarLista(lista,10000);
        long tempoInicio = System.nanoTime();
        Sorts.bolha(lista2);
        long tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 2: " + (tempoFim - tempoInicio) / 1000000.0);
        
        // Teste do algoritmo de ordenacao por selecao
        System.out.println("Sort Selecao");
        List<Integer> lista3 = gerarLista(lista,10000);
        tempoInicio = System.nanoTime();
        Sorts.selecao(lista3);
        tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 3: " + (tempoFim - tempoInicio) / 1000000.0);

        // Teste do algoritmo de ordenacao por insercao
        System.out.println("Sort Insercao");
        List<Integer> lista4 = gerarLista(lista,10000);
        tempoInicio = System.nanoTime();
        Sorts.insercao(lista4);
        tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 4: " + (tempoFim - tempoInicio) / 1000000.0);

        // Teste do algoritmo de ordenacao padrao (Java)
        System.out.println("Sort Padrao");
        List<Integer> lista1 = gerarLista(lista,10000);
        tempoInicio = System.nanoTime();
        lista1.sort(Integer::compareTo);
        tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 1: " + (tempoFim - tempoInicio) / 1000000.0);
    }

    /**
     * Gera uma lista de inteiros aleatorios com o tamanho especificado.
     * @param lista
     * @param tamanho
     * @return
     */
    public static List<Integer> gerarLista(List<Integer> lista, int tamanho) {
        Random random = new Random();
        for (int i = 0; i < tamanho; i++) {
            lista.add(random.nextInt());
        }
        return lista;
    }
}