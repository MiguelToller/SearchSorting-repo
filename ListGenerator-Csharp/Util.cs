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
    }
}
