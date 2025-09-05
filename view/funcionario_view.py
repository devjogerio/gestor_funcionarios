import tkinter as tk
from tkinter import ttk, filedialog

class FuncionarioView:
    def __init__(self, controller):
        self.controller = controller
        self.janela = tk.Tk()
        self.janela.title("Gestão de Funcionários")
        self.titulo = tk.Label(self.janela, text="Projeto: Gestão de Funcionários", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=10)
        self.frame_filtro = tk.Frame(self.janela)
        self.frame_filtro.pack(pady=5)
        self.label_filtro = tk.Label(self.frame_filtro, text="Filtrar:")
        self.label_filtro.pack(side='left', padx=5)
        self.entrada_filtro = tk.Entry(self.frame_filtro)
        self.entrada_filtro.pack(side='left', padx=5, fill='x', expand=True)
        self.entrada_filtro.bind("<KeyRelease>", lambda event: self.controller.aplicar_filtro())
        self.caderno = ttk.Notebook(self.janela)
        self.caderno.pack(expand=True, fill='both')
        self.frame_botoes = tk.Frame(self.janela)
        self.frame_botoes.pack(pady=10)
        self.botao_exportar_aba = tk.Button(self.frame_botoes,
            text="Exportar Dados Filtrados da Aba Ativa",
            command=self.controller.exportar_dados_filtrados_aba_ativa)
        self.botao_exportar_aba.pack(side='left', padx=5)
        self.botao_exportar_todas = tk.Button(self.frame_botoes,
            text="Exportar Todas as Abas",
            command=self.controller.exportar_todas_abas)
        self.botao_exportar_todas.pack(side='left', padx=5)
        self.abas = {}

    def criar_abas(self, departamentos):
        for dept in departamentos:
            aba = ttk.Frame(self.caderno)
            self.caderno.add(aba, text=dept)
            self.abas[dept] = aba

    def limpar_aba(self, aba):
        for widget in aba.winfo_children():
            widget.destroy()

    def mostrar_dados(self, dept, df):
        aba = self.abas[dept]
        self.limpar_aba(aba)
        tree = ttk.Treeview(aba, columns=list(df.columns), show='headings')
        tree.pack(expand=True, fill='both')
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))

    def mainloop(self):
        self.janela.mainloop()

    def get_termo_filtro(self):
        return self.entrada_filtro.get()

    def get_aba_ativa(self):
        return self.caderno.tab(self.caderno.select(), "text")

    def ask_saveasfilename(self):
        return filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
