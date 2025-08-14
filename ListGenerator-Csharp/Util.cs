using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ListGenerator_Csharp
{
    /// <summary>
    /// Classe responsável por métodos de gestão de listas de números inteiros e listas de palavras
    /// </summary>
    internal class Util
    {
        /// <summary>
        /// 
        /// </summary>
        /// método de classe que popula uma lista de números inteiros com valores aleatórios
        /// <param name="lista"></param>
        /// <param name="quantidade"></param>
        /// <param name="inicio"></param>
        /// <param name="fim"></param>
        public static void PopularAleatorioNumeros(List<int> lista, long quantidade, int inicio, int fim)
        {
            Random gerador = new Random();

            for (; quantidade > 0; quantidade--)
            {
                lista.Add(gerador.Next(inicio, fim));
            }
        }

        /// <summary>
        /// método de classe que gera palavras aleatórias
        /// </summary>
        /// <param name="lista"></param>
        /// <param name="quantidade"></param>
        /// <param name="tamanho"></param>
        public static void PopularAleatorioPalavras(List<string> lista, long quantidade, int tamanho)
        {
            string letras = "abcdefghijklmnopqrstuvwxyz ";
            Random gerador = new Random();

            for (; quantidade > 0; quantidade--)
            {
                string palavraGerada = "";
                char letraSorteada;

                for (int i = 0; i < tamanho; i++)
                {
                    letraSorteada = letras[gerador.Next(letras.Length)];
                    palavraGerada += letraSorteada;
                }
                lista.Add(palavraGerada);
            }
        }

        /// <summary>
        ///  método de classe que exibe uma lista
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="lista"></param>
        public static void ExibirLista<T>(List<T> lista)
        {
            foreach (T item in lista)
            {
                Console.WriteLine(item);
            }
        }

        /// <summary>
        /// método de classe que popula um arquivo com números inteiros aleatórios
        /// </summary>
        /// <param name="caminhoArquivo"></param>
        /// <param name="quantidade"></param>
        /// <param name="inicio"></param>
        /// <param name="fim"></param>
        public static void PopularNumeroDeArquivo(string caminhoArquivo, long quantidade, int inicio, int fim)
        {
            Random gerador = new Random();

            try
            {
                using (StreamWriter writer = new StreamWriter(caminhoArquivo))
                    for (; quantidade > 0; quantidade--)
                    {
                        int numero = gerador.Next(inicio, fim);
                        writer.WriteLine(numero);
                    }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        /// <summary>
        /// método de classe que popula um arquivo com palavras aleatórias
        /// </summary>
        /// <param name="caminhoArquivo"></param>
        /// <param name="quantidade"></param>
        /// <param name="tamanho"></param>
        public static void PopularPalavrasDeArquivo(string caminhoArquivo, long quantidade, int tamanho)
        {
            string letras = "abcdefghijklmnopqrstuvwxyz ";
            Random gerador = new Random();

            try
            {
                using (StreamWriter writer = new StreamWriter(caminhoArquivo))
                    for (; quantidade > 0; quantidade--)
                    {
                        string palavraGerada = "";
                        char letraSorteada;

                        for (int i = 0; i < tamanho; i++)
                        {
                            letraSorteada = letras[gerador.Next(letras.Length)];
                            palavraGerada += letraSorteada;
                        }
                        writer.WriteLine(palavraGerada);
                    }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        /// <summary>
        /// método de classe que lê o conteúdo de um arquivo .txt
        /// </summary>
        /// <param name="caminhoArquivo"></param>
        public static void LerArquivo(string caminhoArquivo)
        {
            try
            {
                using (StreamReader reader = new StreamReader(caminhoArquivo))
                {
                    string linha;
                    while ((linha = reader.ReadLine()) != null)
                    {
                        Console.WriteLine(linha);
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}
