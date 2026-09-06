# 📚 Sistema de Gestão de Alunos (CLI)

Um sistema de terminal (CLI) simples e modular desenvolvido em Python para gerenciamento de alunos, cálculo de médias acadêmicas e acompanhamento de situação escolar.

Este projeto foi construído focando em boas práticas de programação, separação de responsabilidades e reutilização de código.

---

## 🚀 Funcionalidades

- **[1] Cadastrar Aluno:** Registra o nome e duas notas, calculando automaticamente a média e definindo a situação (*APROVADO*, *RECUPERAÇÃO* ou *REPROVADO*).
- **[2] Listar Alunos:** Exibe um relatório formatado no terminal com todos os alunos cadastrados.
- **[3] Buscar Aluno:** Consulta os dados e notas individuais de um aluno específico pelo nome.
- **[4] Atualizar Notas:** Permite redefinir as notas de um aluno, recalculando sua média e situação automaticamente.
- **[5] Remover Aluno:** Exclui o registro de um aluno do sistema mediante confirmação.
- **[0] Sair:** Encerra a aplicação com mensagem de despedida.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Python 3**
- **Arquitetura Modular:** Separação entre a lógica de negócios (`funcoes.py`) e a interface do usuário (`menuprincipal.py`).
- **Estruturas de Dados:** Uso de dicionários aninhados (`dict`) e listas (`list`) para controle em memória.
- **Interface Cross-Platform:** Limpeza de tela dinâmica compatível com Windows (`cls`) e Linux/macOS (`clear`).

---


#🔧 Como Executar o Projeto
Certifique-se de ter o Python 3 instalado em sua máquina.

Clone este repositório ou baixe os arquivos em uma pasta local.

Abra o terminal no diretório do projeto e execute:

Bash
python menuprincipal.py
📌 Próximos Passos (Roadmap)
[ ] Implementar persistência de dados em arquivos JSON.

[ ] Adicionar tratamento de exceções (try/except) para validação de entradas.

[ ] Migrar a persistência para um banco de dados SQLite.

[ ] Refatorar a aplicação utilizando Programação Orientada a Objetos (POO).


## 📁 Estrutura do Projeto

```text
Gestao de alunos/
│
├── funcoes.py          # Lógica das operações do sistema (CRUD)
├── menuprincipal.py    # Interface do terminal e controle do fluxo (main)
└── README.md           # Documentação do projeto


---
