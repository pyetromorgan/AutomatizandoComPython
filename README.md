# Automação de Cadastro de Produtos com Python

Este projeto automatiza o processo de login e cadastro de produtos em um sistema web utilizando **Python**, **PyAutoGUI** e **Pandas**.

A automação lê os dados de um arquivo `.csv` e preenche automaticamente o formulário de cadastro, reduzindo o tempo gasto em tarefas repetitivas e minimizando erros de digitação.

---

## Funcionalidades

- Abre o Google Chrome automaticamente.
- Acessa a página de login.
- Realiza o login no sistema.
- Lê os dados de um arquivo `produtos.csv`.
- Preenche o formulário de cadastro para cada produto.
- Envia o cadastro.
- Repete o processo para todos os produtos da planilha.

---

## Tecnologias Utilizadas

- Python 3
- PyAutoGUI
- Pandas
- Time

---

## Estrutura do Projeto

```
.
├── automacao.py
├── produtos.csv
└── README.md
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta do projeto:

```bash
cd seu-repositorio
```

Instale as dependências:

```bash
pip install pyautogui pandas
```

---

## Como Executar

Execute o arquivo principal:

```bash
python automacao.py
```

---

## Formato do Arquivo CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

| Coluna |
|---------|
| codigo |
| marca |
| tipo |
| categoria |
| preco_unitario |
| custo |
| obs |

Exemplo:

| codigo | marca | tipo | categoria | preco_unitario | custo | obs |
|--------|--------|------|-----------|----------------|--------|-----|
| MOLO000251 | Logitech | Mouse | 1 | 25.95 | 6.50 | USB |

---

## Observações

- O projeto utiliza coordenadas fixas do mouse (`pyautogui.click(x, y)`).
- Caso a resolução da tela seja diferente da utilizada no desenvolvimento, será necessário atualizar as coordenadas.
- Não utilize o computador durante a execução da automação, pois qualquer movimentação do mouse pode interferir no processo.
- O tempo de carregamento da página pode variar. Se necessário, aumente os valores de `time.sleep()`.

---

## Possíveis Melhorias

- Utilizar reconhecimento de imagem (`pyautogui.locateOnScreen`) em vez de coordenadas fixas.
- Ler as credenciais por variáveis de ambiente.
- Adicionar tratamento de erros.
- Implementar logs da execução.
- Criar uma interface gráfica.
- Utilizar Selenium ou Playwright para uma automação web mais robusta.

---

## Bibliotecas

- **PyAutoGUI** → Automação de mouse e teclado.
- **Pandas** → Leitura e manipulação da planilha CSV.
- **Time** → Controle do tempo entre as ações.

