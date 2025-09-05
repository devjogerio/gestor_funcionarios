# Projeto Gestão de Funcionários

Este projeto é uma aplicação desktop em Python para gestão de funcionários, utilizando interface gráfica com Tkinter e manipulação de dados com Pandas. O projeto está estruturado seguindo o padrão MVC (Model-View-Controller).

## Estrutura de Pastas

- `model/`      - Lógica de dados e manipulação de arquivos (Pandas, leitura/escrita Excel)
- `view/`       - Interface gráfica (Tkinter)
- `controller/` - Lógica de controle, integração entre model e view
- `funcionarios.xlsx` - Base de dados dos funcionários
- `Projeto_Abas_Gestao_de_Funcionarios.py` - Script principal (pode ser refatorado para usar MVC)

## Como executar


1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o sistema:
   ```bash
   python main.py
   ```

## Funcionalidades
- Visualização de funcionários por departamento
- Filtro de busca
- Exportação de dados filtrados para Excel
- Exportação de todos os departamentos para um único arquivo Excel

## Sobre o padrão MVC
- **Model:** Responsável pela manipulação dos dados (leitura, filtro, exportação)
- **View:** Responsável pela interface gráfica e interação com o usuário
- **Controller:** Faz a ponte entre Model e View, controlando o fluxo da aplicação

## Observações
- O arquivo `funcionarios.xlsx` deve conter uma aba chamada `Dados`.
- O projeto pode ser expandido para incluir mais funcionalidades conforme necessário.

---

### Dependências principais

- pandas
- openpyxl
- tk

Desenvolvido por [devjogerio].
