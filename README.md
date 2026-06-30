# Assistente-Virtual-com-Intelig-ncia-Artificial
Agente de IA criado para o desafio final da Bootcamp Bradesco - GenAI, Dados & Cybersegurança

# Renda Clara

Agente de IA Generativa voltado para educação e reflexão financeira, criado para ajudar usuários a entender melhor seus gastos, hábitos e conceitos básicos de finanças pessoais de forma simples, segura e contextualizada.

## 💡 O que é o Renda Clara?

O **Renda Clara** é um agente de IA com foco em educação financeira. Ele foi pensado para explicar conceitos, interpretar padrões de gastos e apoiar a leitura do contexto financeiro do usuário com linguagem acessível e exemplos práticos.

O agente **ensina e orienta a reflexão**, mas **não faz recomendação financeira personalizada** e não substitui um especialista certificado.

### O que o Renda Clara faz:
- Explica conceitos financeiros de forma clara e simples.
- Usa dados do cliente como exemplos práticos.
- Ajuda a interpretar padrões de gastos.
- Responde dúvidas sobre educação financeira.
- Reconhece limites quando não há informação suficiente.

### O que o Renda Clara NÃO faz:
- Não recomenda investimentos específicos.
- Não acessa dados bancários sensíveis.
- Não substitui consultoria profissional.
- Não inventa dados ausentes no contexto.

---

## 🏗️ Arquitetura

## Arquitetura

```mermaid
flowchart TD
    A[Usuário]
    B[Interface em Streamlit]
    C[Identificação da Intenção]
    D[Montagem do Contexto]
    E[LLM Local via Ollama]
    F[Base de Conhecimento]
    F1[transacoes.csv]
    F2[historico_atendimento.csv]
    F3[perfil_investidor.json]
    F4[produtos_financeiros.json]
    G[Camada de Validação]
    H[Resposta Educativa e Prudente]

    A --> B
    B --> C
    C --> D
    D --> E
    D --> F
    F --> F1
    F --> F2
    F --> F3
    F --> F4
    E --> G
    G --> H

### Descrição do fluxo

1. O usuário envia uma pergunta pela interface em Streamlit.
2. O agente identifica a intenção principal da solicitação.
3. O sistema monta um contexto dinâmico com base nos arquivos da base de conhecimento.
4. O LLM local processa a pergunta com base nesse contexto.
5. Uma camada de validação verifica segurança, aderência ao escopo e risco de alucinação.
6. O usuário recebe uma resposta educativa, clara e prudente.

---

## 📁 Estrutura do Projeto

```bash
├── data/                          # Base de conhecimento
│   ├── perfil_cliente.json        # Perfil do cliente
│   ├── transacoes.csv             # Histórico financeiro
│   ├── historico_atendimento.csv  # Interações anteriores
│   └── produtos_financeiros.json  # Produtos para ensino
│
├── docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md  # Caso de uso e persona
│   ├── 02-base-conhecimento.md    # Estratégia de dados
│   ├── 03-prompts.md              # Prompt principal e exemplos
│   ├── 04-metricas.md             # Avaliação de qualidade
│   └── 05-pitch.md                # Apresentação do projeto
│
├── src/
│   └── app.py                     # Aplicação principal
│
└── README.md
```

---

## 🚀 Como Executar

### 1. Instale as dependências
```bash
pip install streamlit pandas python-dotenv
```

### 2. Execute a aplicação
```bash
streamlit run src/app.py
```

---

## 🎯 Exemplo de Uso

**Pergunta:** “Onde estou gastando mais?”  
**Resposta do Renda Clara:** “Com base nas transações do período analisado, suas maiores despesas estão concentradas em moradia e alimentação. Isso pode ser um ponto de partida para entender como seu orçamento está distribuído.”

**Pergunta:** “O que é reserva de emergência?”  
**Resposta do Renda Clara:** “Reserva de emergência é um valor guardado para lidar com imprevistos, como problemas de saúde, desemprego ou despesas urgentes. Ela ajuda a evitar endividamento em momentos inesperados.”

---

## 📊 Métricas de Avaliação

| Métrica | Objetivo |
|--------|----------|
| Assertividade | O agente responde o que foi perguntado? |
| Segurança | O agente evita inventar informações? |
| Coerência | A resposta faz sentido para o perfil e para o contexto? |

---

## 🎬 Diferenciais

- **Personalização:** usa os dados do próprio cliente nos exemplos.
- **Clareza:** traduz conceitos financeiros para linguagem acessível.
- **Segurança:** evita extrapolar o contexto e admite incerteza.
- **Escopo definido:** atua como agente educativo, não como consultor financeiro.

---

## 📝 Documentação Completa

Toda a documentação técnica, base de conhecimento, prompts, métricas e pitch estão disponíveis na pasta [`docs/`](./docs).

---

## Tecnologias Utilizadas

- [Python 3.9+](https://python.org/) — linguagem principal do projeto.
- [Streamlit](https://streamlit.io/) — interface da aplicação.
- [python-dotenv](https://pypi.org/project/python-dotenv/0.13.0/) — gerenciamento de variáveis de ambiente [web:373].
- Arquivos `JSON` e `CSV` — base mockada para contexto e testes.

---

## Autor

**Igor Anacleto da Silva**  
Profissional com foco em análise de dados e projetos orientados por IA aplicados a contexto financeiro e educacional.
