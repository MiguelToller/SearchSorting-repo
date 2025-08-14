import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> listaNumeros = new ArrayList<>();
        ArrayList<String> listaPalavras = new ArrayList<>();

        /*
        Util.popularAleatorioNumeros(listaNumeros, 10, 0, 100);
        Util.popularAleatorioPalavras(listaPalavras, 5, 5);

        Util.exibirLista(listaNumeros);
        Util.exibirLista(listaPalavras);
        */

        /*
        String caminhoArquivo = "ListGenerator-Java/arquivo.txt";

        Util.popularNumeroDeArquivo(caminhoArquivo, 10000, 0, 1000);
        Util.lerArquivo(caminhoArquivo);

        //Util.popularPalavraDeArquivo(caminhoArquivo, 5, 5);
        //Util.lerArquivo(caminhoArquivo);
        */

        // Lista Numeros Aleatoria
        long tempoInicio = System.nanoTime();

        Util.popularAleatorioNumeros(listaNumeros, 10000, 0, 1000);
        Util.exibirLista(listaNumeros);

        long tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 1: " + ((tempoFim - tempoInicio)/10000000));

        // Pausa
        listaNumeros.clear();
        System.out.println("Aperte Enter.");
        var x = sc.nextLine();

        // Lista Numeros Ordenada
        tempoInicio = System.nanoTime();

        Util.popularNumerosOrdenado(listaNumeros, 10000, 0, 1000);
        Util.exibirLista(listaNumeros);

        tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 2: " + ((tempoFim - tempoInicio)/10000000));
    }
}