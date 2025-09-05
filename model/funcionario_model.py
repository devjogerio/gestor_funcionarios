import pandas as pd

class FuncionarioModel:
    def __init__(self, arquivo_excel='funcionarios.xlsx'):
        self.arquivo_excel = arquivo_excel
        self.df_original = None
        self.dados_filtrados = {}

    def carregar_dados(self):
        self.df_original = pd.read_excel(self.arquivo_excel, sheet_name='Dados')
        self.df_original['Salário'] = self.df_original['Salário'].apply(
            lambda x: f"{x:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        )
        return self.df_original

    def filtrar_por_termo(self, termo):
        termo = termo.lower()
        df_filtrado = self.df_original[self.df_original.apply(
            lambda row: termo in row.to_string(index=False).lower(), axis=1)]
        return df_filtrado

    def filtrar_por_departamento(self, df_filtrado, departamento):
        return df_filtrado[df_filtrado['Departamento'] == departamento]

    def exportar_para_excel(self, df, arquivo):
        df.to_excel(arquivo, index=False)

    def exportar_todos_departamentos(self, abas, arquivo):
        with pd.ExcelWriter(arquivo) as writer:
            for dept, df in abas.items():
                df.to_excel(writer, sheet_name=dept, index=False)
