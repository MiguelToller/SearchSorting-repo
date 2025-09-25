def heapify(arr, n, i):
    """Mantém a propriedade de heap máximo"""
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Verifica se o filho da esquerda é maior que a raiz
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    # Verifica se o filho da direita é maior que o maior até agora
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    # Se o maior não for a raiz, troca e continua o heapify
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


def heap_sort(arr):
    n = len(arr)

    # Passo 1: Construir o heap (reorganizar o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Passo 2: Extrair elementos um a um do heap
    for i in range(n - 1, 0, -1):
        # Troca a raiz (maior) com o último elemento
        arr[i], arr[0] = arr[0], arr[i]
        # Reduz o heap e aplica heapify novamente
        heapify(arr, i, 0)


# Exemplo de uso
valores = [12, 11, 13, 5, 6, 7]
print("Array original:", valores)

heap_sort(valores)
print("Array ordenado:", valores)