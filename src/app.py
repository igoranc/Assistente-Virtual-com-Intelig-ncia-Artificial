import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos
PERFIL FINANCEIRO: {perfil['perfil_investidor']}
OBJETIVO PRINCIPAL: {perfil['objetivo_principal']}
PATRIMÔNIO TOTAL: R$ {perfil['patrimonio_total']}
RESERVA DE EMERGÊNCIA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

HISTÓRICO DE ATENDIMENTOS:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Renda Clara, um assistente financeiro claro, prudente e didático.

OBJETIVO:
Ajudar o usuário a entender melhor seus gastos, seu contexto financeiro e seus padrões de comportamento com base nos dados fornecidos.

REGRAS:
- Responda apenas com base nos dados e no contexto disponíveis;
- NÃO invente valores, produtos, rendimentos, taxas ou informações que não estejam na base;
- Se a pergunta estiver fora do escopo financeiro ou fora dos dados disponíveis, responda com clareza que não possui essa informação;
- Você pode explicar gastos, categorias, padrões de consumo, organização financeira e pontos de atenção;
- Evite recomendar investimentos específicos como se fosse consultoria individual;
- Use linguagem simples, clara e acolhedora;
- Quando possível, use os dados do cliente como exemplo prático;
- Se não souber algo, diga: "Não tenho essa informação nos dados disponíveis.";
- Responda de forma direta, com no máximo 3 parágrafos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )
    return r.json()['response']

# ============ INTERFACE ============
st.set_page_config(page_title="Renda Clara", page_icon="💸")
st.title("💸 Renda Clara")
st.caption("Seu assistente para entender gastos, contexto financeiro e padrões de consumo.")

if pergunta := st.chat_input("Pergunte sobre seus gastos ou sua situação financeira..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Analisando seus dados..."):
        st.chat_message("assistant").write(perguntar(pergunta))
