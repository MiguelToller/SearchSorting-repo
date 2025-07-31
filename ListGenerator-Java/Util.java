import java.util.ArrayList;
import java.util.Random;

/**
 * Classe responsável por métodos de gestão de listas de números inteiros e listas de palavras
 */
public class Util {
    
    /**
     * método de classe que popula uma lista de números inteiros com valores aleatórios
     * @param lista
     * @param quantidade
     * @param inicio
     * @param fim
     */
    public static void popularAleatorioNumeros(ArrayList<Integer> lista, long quantidade, int inicio, int fim) {
        Random gerador = new Random();

        for(; quantidade > 0; quantidade--) {
            lista.add(gerador.nextInt(inicio, fim));
        }
    }

    /**
     * método de classe que gera palavras aleatórias
     * @param lista
     * @param quantidade
     * @param tamanho
     */
    public static void popularAleatorioPalavras(ArrayList<String> lista, long quantidade, int tamanho) {
        String letras = "abcdefghijklmnopqrstuvwxyz ";
        Random gerador = new Random();

        for(; quantidade > 0; quantidade--) {
           String palavraGerada = "";
           char letraSorteada;

           for(int i = 0; i < tamanho; i++) {
                letraSorteada = letras.charAt(gerador.nextInt(letras.length()));
                palavraGerada += letraSorteada;
           }
           lista.add(palavraGerada);
        }
    }

    /**
     * método de classe que exibe uma lista
     * @param lista
     */
    public static <T> void exibirLista(ArrayList<T> lista) {
        for(T item : lista) {
            System.out.println(item);
        }
    }
    
}
