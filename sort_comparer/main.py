import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading
from sorts import Sorts

# Dicionário de métodos disponíveis
metodos = {
    "Bolha": Sorts.bolha,
    "Seleção": Sorts.selecao,
    "Inserção": Sorts.insercao,
    "Agitação": Sorts.agitacao,
    "Pente": Sorts.pente,
    "Shell": Sorts.shell
}

def comparar_thread():
    thread = threading.Thread(target=comparar)
    thread.start()

# Função que compara os dois métodos
def comparar():
    try:
        n = int(entry_qtd.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido maior que zero!")
        return

    metodo1_nome = combo1.get()
    metodo2_nome = combo2.get()

    if metodo1_nome not in metodos or metodo2_nome not in metodos:
        messagebox.showerror("Erro", "Escolha dois métodos válidos!")
        return

    # Gerar lista aleatória
    lista = [random.randint(1, 10000) for _ in range(n)]

    # Rodar método 1
    start = time.perf_counter()
    comp1, swaps1 = metodos[metodo1_nome](lista.copy())
    t1 = time.perf_counter() - start

    # Rodar método 2
    start = time.perf_counter()
    comp2, swaps2 = metodos[metodo2_nome](lista.copy())
    t2 = time.perf_counter() - start

    # Mostrar resultados
    msg = (f"{metodo1_nome}:\n  Tempo: {t1:.6f}s\n  Comparações: {comp1}\n  Trocas: {swaps1}\n\n"
           f"{metodo2_nome}:\n  Tempo: {t2:.6f}s\n  Comparações: {comp2}\n  Trocas: {swaps2}\n\n")

    if t1 < t2:
        msg += f"➡ {metodo1_nome} foi mais rápido!"
    elif t2 < t1:
        msg += f"➡ {metodo2_nome} foi mais rápido!"
    else:
        msg += "➡ Empate!"

    resultado.set(msg)


# ----- Interface Tkinter -----
janela = tk.Tk()
janela.title("Comparador de Algoritmos de Ordenação")
janela.geometry("500x400")

# Entrada de quantidade
tk.Label(janela, text="Quantidade de valores:").pack(pady=5)
entry_qtd = tk.Entry(janela)
entry_qtd.pack(pady=5)

# Combobox 1
tk.Label(janela, text="Método 1:").pack(pady=5)
combo1 = ttk.Combobox(janela, values=list(metodos.keys()), state="readonly")
combo1.pack(pady=5)

# Combobox 2
tk.Label(janela, text="Método 2:").pack(pady=5)
combo2 = ttk.Combobox(janela, values=list(metodos.keys()), state="readonly")
combo2.pack(pady=5)

# Botão
btn = tk.Button(janela, text="Comparar", command=comparar_thread)
btn.pack(pady=10)

# Resultado
resultado = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado, justify="left", anchor="w")
label_resultado.pack(pady=10, fill="both", expand=True)

janela.mainloop()