import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
    
        ArrayList<Integer> listaNumeros = new ArrayList<>();
        ArrayList<String> listaPalavras = new ArrayList<>();

        /*
        Util.popularAleatorioNumeros(listaNumeros, 10, 0, 100);
        Util.popularAleatorioPalavras(listaPalavras, 5, 5);

        Util.exibirLista(listaNumeros);
        Util.exibirLista(listaPalavras);
        */

        String caminhoArquivo = "ListGenerator-Java/arquivo.txt";

        Util.popularNumeroDeArquivo(caminhoArquivo, 5, 0, 10);
        Util.lerArquivo(caminhoArquivo);

        Util.popularPalavraDeArquivo(caminhoArquivo, 5, 5);
        Util.lerArquivo(caminhoArquivo);
    }
}