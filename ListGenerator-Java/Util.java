import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
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

    /**
     * método de classe que popula um arquivo com números inteiros aleatórios
     * @param caminhoArquivo
     * @param quantidade
     * @param inicio
     * @param fim
     */
    public static void popularNumeroDeArquivo(String caminhoArquivo, long quantidade, int inicio, int fim) {
        Random gerador = new Random();

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(caminhoArquivo))) {
            for(; quantidade > 0; quantidade--) {
                int numero = gerador.nextInt(inicio, fim);
                writer.write(Integer.toString(numero));
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("Erro ao escrever no arquivo: " + e.getMessage());
        }
    }

    /**
     * método de classe que popula um arquivo com palavras aleatórias
     * @param caminhoArquivo
     * @param quantidade
     * @param tamanho
     */
    public static void popularPalavraDeArquivo(String caminhoArquivo, long quantidade, int tamanho) {
        String letras = "abcdefghijklmnopqrstuvwxyz ";
        Random gerador = new Random();

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(caminhoArquivo))) {
            for(; quantidade > 0; quantidade--) {
                String palavraGerada = "";
                char letraSorteada;

                for(int i = 0; i < tamanho; i++) {
                    letraSorteada = letras.charAt(gerador.nextInt(letras.length()));
                    palavraGerada += letraSorteada;
                }
                writer.write(palavraGerada);
                writer.newLine();
            }
        } catch (IOException e) {
            System.out.println("Erro ao escrever no arquivo: " + e.getMessage());
        }
    }

    /**
     * método de classe que lê o conteúdo de um arquivo .txt
     * @param caminhoArquivo
     */
    public static void lerArquivo(String caminhoArquivo) {
        try (BufferedReader reader = new BufferedReader(new FileReader(caminhoArquivo))) {
            String linha;
            while ((linha = reader.readLine()) != null) {
                System.out.println(linha);
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }

    /**
     * método de classe popula uma lista ordenada
     * @param lista
     * @param quantidade
     * @param inicio
     * @param fim
     */
    public static void popularNumerosOrdenado(ArrayList<Integer> lista, long quantidade, int inicio, int fim) {
        int numero = inicio;

        for(; quantidade > 0; quantidade--) {
            lista.add(numero);
            numero += 1;
        }
    }

}
