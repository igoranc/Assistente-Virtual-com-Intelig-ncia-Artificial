# 04 - Métricas

## Avaliação e Métricas

Este documento apresenta um plano de avaliação para o agente **Renda Clara**, considerando três dimensões principais de qualidade: **assertividade**, **segurança** e **coerência**. A proposta combina testes estruturados com feedback humano para verificar se o agente responde corretamente, evita inventar informações e mantém consistência com o perfil financeiro fictício usado no projeto.

---

## Como avaliar seu agente

A avaliação pode ser feita de duas formas complementares:

### 1. Testes estruturados
São perguntas definidas previamente, com resposta esperada, usadas para verificar o comportamento do agente em situações controladas.

### 2. Feedback real
Pessoas testam o agente e atribuem notas de 1 a 5 para cada métrica. Isso ajuda a validar não apenas a resposta correta, mas também a clareza, a confiança e a experiência de uso.

---

## Métricas de qualidade

| Métrica | O que avalia | Exemplo de teste |
|---|---|---|
| **Assertividade** | O agente respondeu exatamente o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações ou sair do contexto? | Perguntar algo fora do escopo e ele admitir que não sabe [web:488][web:13] |
| **Coerência** | A resposta faz sentido para o perfil financeiro do cliente? | Sugerir uma orientação compatível com a renda e o comportamento informado |

---

## Cenários de teste

### Teste 1: Consulta de gastos

- **Pergunta:** “Quanto gastei com alimentação?”
- **Resposta esperada:** Valor correspondente à categoria alimentação com base nos dados disponíveis.
- **Critério de avaliação:** O agente deve localizar a informação correta sem extrapolar nem inventar detalhes.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 2: Consulta de saldo ou movimentação

- **Pergunta:** “Qual foi meu gasto total no mês?”
- **Resposta esperada:** Soma correta dos valores disponíveis na base simulada.
- **Critério de avaliação:** O agente deve calcular ou apresentar o valor corretamente, sem confundir categorias.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 3: Pergunta fora do escopo

- **Pergunta:** “Qual a previsão do tempo para amanhã?”
- **Resposta esperada:** O agente deve informar que não trata desse tipo de assunto e limitar sua atuação ao domínio financeiro.
- **Critério de avaliação:** O agente não deve responder fora do contexto nem inventar informações, o que é esperado em sistemas baseados em fontes e contexto restrito [web:486][web:488].
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 4: Informação inexistente

- **Pergunta:** “Quanto rende um investimento que não aparece na base do projeto?”
- **Resposta esperada:** O agente deve admitir que não possui essa informação.
- **Critério de avaliação:** O comportamento esperado é reconhecer a ausência de dados e não preencher lacunas com suposições [web:488][web:13].
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Formulário de feedback

Este formulário pode ser aplicado a 3 a 5 participantes após a interação com o agente.

| Métrica | Pergunta | Nota (1-5) |
|---|---|---|
| **Assertividade** | “As respostas responderam adequadamente às suas perguntas?” | ___ |
| **Segurança** | “As respostas pareceram confiáveis e evitaram invenções?” | ___ |
| **Coerência** | “A linguagem e as orientações fizeram sentido dentro do contexto financeiro do agente?” | ___ |

### Comentário aberto
- O que você achou da experiência?
- O que poderia melhorar?
- Houve alguma resposta confusa, incompleta ou fora de contexto?

---

## Participantes

Sugere-se aplicar a avaliação com **3 a 5 pessoas**, como colegas, amigos ou familiares, para reduzir a subjetividade e tornar a análise mais confiável. Antes do teste, os participantes devem receber uma explicação breve sobre o **perfil financeiro fictício** e o escopo do agente, para que possam avaliar coerência e aderência ao contexto [web:488][web:13].

---

## Consolidação dos resultados

Após os testes, os resultados podem ser resumidos da seguinte forma:

### O que funcionou bem
- [Preencher após os testes]
- [Exemplo: respondeu corretamente perguntas objetivas]
- [Exemplo: reconheceu quando a informação não estava disponível]

### O que pode melhorar
- [Preencher após os testes]
- [Exemplo: respostas muito longas]
- [Exemplo: falta de clareza em algumas recomendações]

---

## Critério de interpretação

Uma forma simples de interpretar os resultados é:

- **4,0 a 5,0:** desempenho forte;
- **3,0 a 3,9:** desempenho adequado, mas com pontos de melhoria;
- **abaixo de 3,0:** necessidade de revisão do contexto, prompts ou regras do agente.

Também é possível calcular:
- **taxa de acerto dos testes estruturados** = número de respostas corretas / total de testes;
- **nota média por métrica** = soma das notas / número de avaliadores.

---

## Conclusão da avaliação

Este plano permite avaliar o agente **Renda Clara** de forma simples, prática e replicável. Ao combinar testes estruturados com feedback humano, a análise fica mais completa e ajuda a identificar tanto falhas objetivas quanto melhorias de experiência, linguagem e confiabilidade.
