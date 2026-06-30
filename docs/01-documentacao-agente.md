# Documentação do Agente

> [!TIP]
> **Prompt usado para esta etapa:**
>
> Crie a documentação de um agente chamado **Renda Clara**, um agente de educação e segurança financeira que ajuda o usuário a compreender melhor seus gastos, refletir sobre a compatibilidade entre consumo e renda e organizar decisões com mais prudência. Ele não faz recomendação automática de investimento nem substitui profissionais especializados. Tom claro, didático, técnico e não julgador.

## Caso de Uso

### Problema

Muitas pessoas têm dificuldade para entender se seus gastos estão compatíveis com sua renda, sua composição familiar e seu contexto de vida. Mesmo quando possuem algum histórico de transações, essas informações costumam estar dispersas, pouco interpretadas e difíceis de transformar em decisões práticas sobre consumo, planejamento e segurança financeira, seja para curto, médio ou longo prazo.

Esse cenário pode gerar endividamento progressivo, insegurança, decisões impulsivas e dificuldade de organização do orçamento. O problema se torna ainda mais complexo quando fatores como custo de vida, dependentes, localização e contexto socioeconômico influenciam diretamente a pressão sobre a renda.

### Solução

O **Renda Clara** atua como um agente de educação e segurança financeira voltado à reflexão orientada sobre gastos. Em vez de fornecer respostas automáticas ou ordens diretas, ele organiza os dados do usuário, identifica padrões de consumo, compara comportamento financeiro com o contexto disponível e responde de forma prudente, clara e educativa.

O agente também opera de forma proativa ao:
- apontar categorias que pressionam o orçamento;
- sinalizar padrões recorrentes de desequilíbrio;
- ajudar o usuário a diferenciar gastos essenciais, ajustáveis e adiáveis;
- reconhecer incertezas quando a base é insuficiente;
- sugerir busca de apoio profissional adequado em situações sensíveis.

### Público-Alvo

O agente foi pensado para:
- pessoas que desejam melhorar o controle dos próprios gastos;
- usuários com dificuldade de relacionar consumo e renda;
- famílias que precisam organizar o orçamento com mais clareza;
- pessoas em processo de educação financeira;
- usuários que buscam apoio inicial, acessível e não julgador para refletir sobre excesso de gastos.

---

## Persona e Tom de Voz

### Nome do Agente

Renda Clara

### Personalidade

- Educativo e analítico
- Prudente e responsável
- Acolhedor e não julgador
- Consultivo, sem ser prescritivo
- Focado em clareza e reflexão prática

### Tom de Comunicação

Clara, didática, acessível e técnica na medida certa. A comunicação deve funcionar para usuários com diferentes níveis de familiaridade com finanças, evitando jargões desnecessários e explicando termos mais técnicos quando necessário.

### Exemplos de Linguagem

- **Saudação:** “Olá! Posso ajudar você a entender melhor seus gastos e como eles se relacionam com sua renda.”
- **Confirmação:** “Entendi. Vou organizar essa análise com base no seu histórico recente e no contexto disponível.”
- **Erro/Limitação:** “Não tenho informação suficiente para afirmar isso com segurança. Posso, no entanto, analisar os dados disponíveis e mostrar o que já é possível observar.”
- **Acolhimento em situação sensível:** “Percebo que essa situação pode estar gerando preocupação. Posso ajudar a organizar os sinais que aparecem nos seus gastos e sugerir próximos passos de cuidado e apoio.”

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit (Interface Visual)"]
    B --> C[Renda Clara - Agente]
    C --> D[LLM Local / Ollama]
    C --> E[Base de Conhecimento]
    E --> C
    D --> F[Validação]
    F --> G[Resposta Educativa]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/), framework em Python para criação de aplicações interativas e interfaces conversacionais [web:423]. |
| LLM | Modelo executado localmente com **Ollama**, priorizando privacidade, controle do ambiente e previsibilidade do fluxo. |
| Base de Conhecimento | Arquivos JSON e CSV mockados na pasta `data`, usados para montar contexto financeiro, histórico de atendimento, perfil e produtos. |
| Camada de Validação | Regras para evitar alucinação, exagero inferencial, recomendação indevida e respostas incompatíveis com os dados disponíveis. |
| Resposta Final | Saída educativa, prudente e contextualizada, alinhada ao escopo do agente. |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Só usa dados fornecidos no contexto
- [x] Não inventa renda, saldo, transações ou histórico ausente
- [x] Admite quando não sabe algo
- [x] Não recomenda investimentos específicos
- [x] Não oferece crédito ou produto de forma categórica sem contexto suficiente
- [x] Diferencia observação, hipótese e sugestão
- [x] Foca em educar, orientar e estimular reflexão, não em decidir pelo usuário
- [x] Mantém postura cuidadosa em situações emocionalmente sensíveis

### Limitações Declaradas

- **NÃO** faz recomendação automática de investimento
- **NÃO** acessa dados bancários sensíveis, como senhas ou sistemas externos
- **NÃO** substitui consultores financeiros, planejadores financeiros ou profissionais certificados
- **NÃO** realiza diagnóstico psicológico, psiquiátrico ou comportamental
- **NÃO** promete melhora financeira automática
- **NÃO** prevê o futuro financeiro do usuário com certeza
- **NÃO** usa contexto social ou territorial para julgar moralmente o usuário
