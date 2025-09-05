from model.funcionario_model import FuncionarioModel
from view.funcionario_view import FuncionarioView

class FuncionarioController:
    def __init__(self):
        self.model = FuncionarioModel()
        self.view = FuncionarioView(self)
        self.abas = {}
        self.df_original = self.model.carregar_dados()
        self.view.criar_abas(self.df_original['Departamento'].unique())
        self.aplicar_filtro()

    def aplicar_filtro(self):
        termo = self.view.get_termo_filtro()
        df_filtrado = self.model.filtrar_por_termo(termo)
        for dept in self.df_original['Departamento'].unique():
            df_dept = self.model.filtrar_por_departamento(df_filtrado, dept)
            self.abas[dept] = df_dept
            self.view.mostrar_dados(dept, df_dept)

    def exportar_dados_filtrados_aba_ativa(self):
        aba_ativa = self.view.get_aba_ativa()
        df_exportar = self.abas.get(aba_ativa)
        if df_exportar is not None:
            arquivo = self.view.ask_saveasfilename()
            if arquivo:
                self.model.exportar_para_excel(df_exportar, arquivo)

    def exportar_todas_abas(self):
        arquivo = self.view.ask_saveasfilename()
        if arquivo:
            self.model.exportar_todos_departamentos(self.abas, arquivo)

    def run(self):
        self.view.mainloop()

if __name__ == "__main__":
    app = FuncionarioController()
    app.run()
