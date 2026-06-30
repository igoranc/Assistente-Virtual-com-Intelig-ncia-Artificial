# Base de Conhecimento

> [!TIP]
> **Prompt usado para esta etapa:**
>
> Organize a base de conhecimento do agente **Renda Clara** usando os 4 arquivos da pasta `data/`. Explique para que serve cada arquivo e monte um exemplo de contexto formatado que será enviado para o LLM. Adapte a estrutura para um agente de educação e segurança financeira com foco em análise de gastos, prudência e reflexão orientada.

## Dados Utilizados

O projeto **Renda Clara** utiliza como base principal os arquivos mockados disponibilizados no desafio. Esses dados permitem simular um agente financeiro com foco em educação, racionalização de gastos e segurança financeira, sem depender de dados bancários reais.

| Arquivo | Formato | Para que serve no Renda Clara? |
|---|---|---|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, identificar dúvidas recorrentes, captar sinais de preocupação financeira e evitar respostas desconectadas do histórico do usuário. |
| `perfil_investidor.json` | JSON | Personalizar a leitura do contexto do usuário, considerando perfil financeiro, objetivos, características gerais e informações que ajudam a interpretar melhor o comportamento de consumo. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos e serviços disponíveis apenas para fins educativos, sem recomendação automática, permitindo que o agente explique possibilidades com prudência. |
| `transacoes.csv` | CSV | Analisar padrão de gastos, recorrência de despesas, categorias mais pesadas, sazonalidade e possíveis excessos incompatíveis com a realidade financeira do usuário. |

A lógica central do projeto está concentrada, sobretudo, em `transacoes.csv`, porque é nele que o agente observa o comportamento financeiro na série histórica disponível. Os demais arquivos funcionam como camadas de contexto, continuidade e prudência interpretativa.

---

## Adaptações nos Dados

Os dados mockados podem ser mantidos como base principal, mas o projeto **Renda Clara** prevê adaptações conceituais para ficar mais aderente ao seu caso de uso.

### Adaptações previstas

- Inclusão de categorias de gastos mais detalhadas em `transacoes.csv`, como moradia, alimentação, transporte, educação, saúde, lazer e compras não planejadas.
- Inclusão de campos contextuais no perfil do usuário, como estado civil, número de filhos, escolaridade, ocupação, cidade, bairro e faixa de renda estimada.
- Inclusão de sinais conversacionais no `historico_atendimento.csv`, como menções recorrentes a endividamento, ansiedade com contas ou dificuldade de controlar impulsos de compra.
- Uso de `produtos_financeiros.json` apenas como base educativa, sem transformar o agente em um recomendador automático de investimento ou crédito.
- Possibilidade de usar referências públicas complementares de renda, trabalho e território apenas como contexto interpretativo, nunca como instrumento de julgamento rígido.

### Princípio metodológico

As expansões não existem para tornar o agente mais invasivo, mas mais contextual. O foco do Renda Clara não é vigiar o usuário, e sim interpretar melhor o padrão de gastos dentro de sua realidade financeira, familiar e social.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos CSV e JSON são carregados no início da sessão da aplicação. Em um protótipo funcional, isso pode ser feito com `pandas.read_csv()` para arquivos tabulares e leitura de JSON com `json.load()`, abordagem compatível com a documentação do pandas para ingestão de dados estruturados.

```python
import pandas as pd
import json

perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))
```

Essa estratégia é suficiente para um chatbot simples em Streamlit, mantendo os dados em memória durante a sessão e atualizando o contexto conforme as perguntas do usuário.

### Como os dados são usados no prompt?

No **Renda Clara**, os dados **não devem ser despejados integralmente no system prompt**. Em vez disso, o projeto adota uma estratégia de **contexto montado dinamicamente**.

#### Estratégia recomendada

- O **system prompt** define comportamento, limites, tom de voz e política de segurança.
- Os **dados do usuário** entram como contexto variável, montado a cada interação.
- Apenas os dados relevantes para a pergunta atual são enviados ao modelo.
- Regras locais em Python podem filtrar:
  - últimas transações;
  - categorias predominantes;
  - frequência de gastos;
  - sinais de pressão orçamentária;
  - histórico recente de atendimento;
  - elementos importantes do perfil do usuário.

### Por que usar contexto dinâmico?

Esse modelo melhora:
- foco da resposta;
- eficiência do prompt;
- interpretabilidade;
- controle contra alucinação;
- privacidade e redução de ruído.

Também ajuda a separar melhor:
- **instruções permanentes** do agente;
- **dados variáveis** do usuário;
- **regras de segurança** aplicadas antes da resposta final.

---

## Exemplo de Contexto Montado

O exemplo abaixo mostra como os dados podem ser organizados e resumidos antes de serem enviados ao modelo. A ideia é preservar o que é mais relevante para a resposta, sem desperdiçar contexto com informação redundante.

```txt
DADOS DO USUÁRIO:
- Nome: João Silva
- Perfil financeiro: Moderado
- Objetivo principal: Organizar melhor os gastos e manter segurança financeira
- Estado civil: Casado
- Filhos: 2
- Ocupação: Analista administrativo
- Cidade: Vitória - ES
- Faixa de renda estimada: compatível com ocupação e contexto urbano local

HISTÓRICO DE ATENDIMENTO:
- Já relatou preocupação com aumento do cartão de crédito
- Já perguntou como reduzir despesas recorrentes
- Demonstra dificuldade em manter planejamento mensal

RESUMO DE GASTOS RECENTES:
- Moradia: R$ 1.850
- Alimentação: R$ 920
- Transporte: R$ 540
- Educação: R$ 430
- Saúde: R$ 310
- Lazer: R$ 680
- Compras não planejadas: R$ 740

PADRÕES IDENTIFICADOS:
- Crescimento de gastos variáveis nos últimos 3 meses
- Alta concentração de despesas em categorias discricionárias
- Indício de pressão sobre o orçamento familiar

PRODUTOS E RECURSOS DISPONÍVEIS PARA EXPLICAÇÃO:
- Ferramenta de metas financeiras
- Conta com organização de orçamento
- Conteúdos educativos sobre controle de gastos
- Produtos financeiros explicados apenas em caráter informativo

INSTRUÇÃO PARA O AGENTE:
Responda de forma educativa, prudente e clara. Não invente renda exata. Não diagnostique comportamento. Ajude o usuário a refletir sobre compatibilidade entre gastos e capacidade financeira, diferenciando observação, hipótese e sugestão.
```

---

## Critérios de Uso da Base

A base de conhecimento no **Renda Clara** segue quatro critérios principais:

### 1. Relevância
Só entram no contexto os dados realmente úteis para responder à pergunta do usuário.

### 2. Prudência
Dados incompletos não devem ser tratados como verdades definitivas.

### 3. Explicabilidade
As respostas precisam poder ser justificadas com base nos dados carregados.

### 4. Responsabilidade
O agente não deve usar contexto social, territorial ou familiar para rotular, constranger ou estigmatizar o usuário.

---

## Limitações da Base

Mesmo com os dados mockados e possíveis expansões, a base de conhecimento possui limitações que precisam ser explicitadas:

- Os dados não representam a totalidade da vida financeira do usuário.
- A renda pode estar ausente ou apenas parcialmente estimada.
- O contexto territorial é apenas referencial.
- O histórico de atendimento pode não capturar toda a subjetividade da situação.
- O agente não deve inferir compulsividade, sofrimento psíquico ou risco financeiro extremo com base em poucos sinais.
- Produtos financeiros presentes na base não devem ser tratados como recomendação automática.

Por isso, o **Renda Clara** opera com cautela e reconhece incerteza sempre que necessário.
