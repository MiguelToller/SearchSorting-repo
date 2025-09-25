class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} ({self.idade})"


class Ordenacao:
    @staticmethod
    def criterio(p):
        """Define o critério de ordenação: nome (crescente), depois idade (crescente)."""
        return (p.nome, p.idade)

    # Bubble Sort
    @staticmethod
    def bolha(lista):
        houve_troca = True
        fim = len(lista)
        while houve_troca:
            houve_troca = False
            for i in range(fim - 1):
                if Ordenacao.criterio(lista[i]) > Ordenacao.criterio(lista[i + 1]):
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    houve_troca = True
            fim -= 1

    # Quick Sort
    @staticmethod
    def quick(lista):
        def _quick(lst):
            if len(lst) <= 1:
                return lst
            pivo = lst[len(lst) // 2]
            menores = [x for x in lst if Ordenacao.criterio(x) < Ordenacao.criterio(pivo)]
            iguais = [x for x in lst if Ordenacao.criterio(x) == Ordenacao.criterio(pivo)]
            maiores = [x for x in lst if Ordenacao.criterio(x) > Ordenacao.criterio(pivo)]
            return _quick(menores) + iguais + _quick(maiores)

        return _quick(lista)

    # Comb Sort (Pente)
    @staticmethod
    def pente(lista):
        gap = len(lista)
        shrink = 1.3
        houve_troca = True

        while gap > 1 or houve_troca:
            gap = int(gap / shrink)
            if gap < 1:
                gap = 1

            houve_troca = False
            for i in range(len(lista) - gap):
                if Ordenacao.criterio(lista[i]) > Ordenacao.criterio(lista[i + gap]):
                    lista[i], lista[i + gap] = lista[i + gap], lista[i]
                    houve_troca = True


def main():
    lista = [
        Pessoa('Alex', 25),
        Pessoa('Alex', 13),
        Pessoa('Charlie', 20),
        Pessoa('Alex', 15),
        Pessoa('Brian', 25)
    ]

    print("\n--- Bubble Sort ---")
    lista1 = lista.copy()
    Ordenacao.bolha(lista1)
    print(lista1)

    print("\n--- Quick Sort ---")
    lista2 = Ordenacao.quick(lista.copy())
    print(lista2)

    print("\n--- Pente (Comb Sort) ---")
    lista3 = lista.copy()
    Ordenacao.pente(lista3)
    print(lista3)


if __name__ == "__main__":
    main()