# Automação de Registro e Notificação de Leads com n8n

Este documento especifica o fluxo de automação desenvolvido para capturar leads via formulário, validar as informações, registrar os dados em uma planilha e notificar tanto o cliente quanto a equipe comercial.

---

## 🎯 Objetivo
Automatizar a entrada de leads provenientes do Google Forms, garantindo o armazenamento centralizado no Google Sheets e enviando confirmações automáticas via Gmail.

---

## 👥 Públicos Envolvidos
- **Cliente / Lead:** Recebe uma confirmação de recebimento (boas-vindas).
- **Equipe Comercial:** Recebe um alerta interno para acompanhamento do novo lead.

---

## 🛠️ Ferramentas Utilizadas
- **n8n:** Plataforma de orquestração do fluxo.
- **Google Forms:** Captação inicial do lead.
- **Google Sheets:** Banco de dados/planilha de registros.
- **Gmail:** Envio automatizado dos e-mails.

---

## 📐 Estrutura do Workflow

```text
[Google Forms Trigger] 
       │
       ▼
    [Filter] (Validação do e-mail)
       │
       ▼
[Google Sheets] (Registrar lead)
       │
       ▼
[Gmail - Boas-vindas] (E-mail para o cliente)
       │
       ▼
[Gmail - Notificação] (E-mail para o time comercial)
```

---

## ⚙️ Detalhamento dos Nós (Nodes)

### 1. Google Forms Trigger (Gatilho)
* **Função:** Capturar as respostas do formulário em tempo real.
* **Ação:** Inicia a execução sempre que um formulário é submetido.

### 2. Filter (Validação do E-mail)
* **Função:** Aplicar a regra de negócio que descarta cadastros sem e-mail válido.
* **Configuração:**
  * **Campo:** `{{ $json.email }}`
  * **Condição:** *Is Not Empty* **E** *Regex Match* (`/^[^\s@]+@[^\s@]+\.[^\s@]+$/`).
* **Regra:** Se o e-mail for inválido ou estiver em branco, o fluxo é encerrado imediatamente.

### 3. Google Sheets (Armazenamento)
* **Função:** Salvar os leads qualificados na planilha comercial.
* **Operação:** `Append Row`
* **Mapeamento de Colunas:**
  * Nome $\rightarrow$ `{{ $json.nome }}`
  * E-mail $\rightarrow$ `{{ $json.email }}`
  * Telefone $\rightarrow$ `{{ $json.telefone }}`
  * Data/Hora $\rightarrow$ `{{ $now }}`

### 4. Gmail — Boas-vindas (Cliente)
* **Função:** Confirmar o recebimento das informações para o lead.
* **Destinatário (`To`):** `{{ $json.email }}`
* **Assunto:** `Recebemos sua mensagem, {{ $json.nome }}!`
* **Conteúdo:**
  > Olá, {{ $json.nome }}!
  > 
  > Obrigado por entrar em contato. Recebemos seus dados e nossa equipe entrará em contato em breve.

### 5. Gmail — Notificação (Equipe Comercial)
* **Função:** Avisar os vendedores sobre a chegada de um novo lead.
* **Destinatário (`To`):** `vendas@suaempresa.com`
* **Assunto:** `🚨 Novo Lead Cadastrado: {{ $json.nome }}`
* **Conteúdo:**
  > Novo lead cadastrado no sistema:
  > - **Nome:** {{ $json.nome }}
  > - **E-mail:** {{ $json.email }}
  > - **Telefone:** {{ $json.telefone }}
  > 
  > Os dados foram salvos na planilha comercial.