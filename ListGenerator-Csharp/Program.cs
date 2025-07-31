namespace ListGenerator_Csharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> listaNumeros = new List<int>();
            List<string> listaPalavras = new List<string>();

            Util.PopularAleatorioNumeros(listaNumeros, 10, 0, 100);
            Util.PopularAleatorioPalavras(listaPalavras, 5, 5);

            Util.ExibirLista(listaNumeros);
            Util.ExibirLista(listaPalavras);
        }
    }
}
