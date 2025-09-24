import tkinter as tk
from tkinter import ttk, messagebox, filedialog
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

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo com números",
        filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )
    if caminho:
        arquivo_selecionado.set(caminho)

def comparar_thread():
    thread = threading.Thread(target=comparar)
    thread.start()

def comparar():
    metodo1_nome = combo1.get()
    metodo2_nome = combo2.get()

    if metodo1_nome not in metodos or metodo2_nome not in metodos:
        messagebox.showerror("Erro", "Escolha dois métodos válidos!")
        return

    if not arquivo_selecionado.get():
        messagebox.showerror("Erro", "Selecione um arquivo com números primeiro!")
        return

    # Ler lista do arquivo selecionado
    try:
        with open(arquivo_selecionado.get(), "r") as f:
            conteudo = f.read().strip()
            lista = [int(x) for x in conteudo.split()]
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado!")
        return
    except ValueError:
        messagebox.showerror("Erro", "Arquivo contém valores inválidos!")
        return

    if not lista:
        messagebox.showerror("Erro", "O arquivo está vazio!")
        return

    # Rodar método 1
    start = time.perf_counter()
    comp1, swaps1 = metodos[metodo1_nome](lista.copy())
    t1 = time.perf_counter() - start

    # Rodar método 2
    start = time.perf_counter()
    comp2, swaps2 = metodos[metodo2_nome](lista.copy())
    t2 = time.perf_counter() - start

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
janela.geometry("550x450")

# StringVar DEPOIS do root:
arquivo_selecionado = tk.StringVar()
resultado = tk.StringVar()

# Selecionar arquivo
tk.Label(janela, text="Arquivo com os números:").pack(pady=5)
frame_arquivo = tk.Frame(janela)
frame_arquivo.pack(pady=5)
entry_arquivo = tk.Entry(frame_arquivo, textvariable=arquivo_selecionado, width=40, state="readonly")
entry_arquivo.pack(side="left", padx=5)
btn_arquivo = tk.Button(frame_arquivo, text="Selecionar arquivo", command=selecionar_arquivo)
btn_arquivo.pack(side="left", padx=5)

# Combobox 1
tk.Label(janela, text="Método 1:").pack(pady=5)
combo1 = ttk.Combobox(janela, values=list(metodos.keys()), state="readonly")
combo1.pack(pady=5)

# Combobox 2
tk.Label(janela, text="Método 2:").pack(pady=5)
combo2 = ttk.Combobox(janela, values=list(metodos.keys()), state="readonly")
combo2.pack(pady=5)

# Botão Comparar
btn = tk.Button(janela, text="Comparar", command=comparar_thread)
btn.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, textvariable=resultado, justify="left", anchor="w")
label_resultado.pack(pady=10, fill="both", expand=True)

janela.mainloop()