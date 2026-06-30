import json
from pathlib import Path
import pandas as pd
import requests
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
PERFIL_PATH = BASE_DIR / "perfil_cliente.json"
TRANSACOES_PATH = BASE_DIR / "transacoes.csv"
HISTORICO_PATH = BASE_DIR / "historico_atendimento.csv"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

perfil = json.load(open(PERFIL_PATH, encoding="utf-8"))
transacoes = pd.read_csv(TRANSACOES_PATH)
historico = pd.read_csv(HISTORICO_PATH)

metas_txt = "\n".join(
    [f"- {m['meta']} | valor necessário: R$ {m['valor_necessario']:.2f} | prazo: {m['prazo']}" for m in perfil.get("metas", [])]
) or "- Sem metas cadastradas."

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos
PROFISSÃO: {perfil.get('profissao', 'Não informada')}
RENDA MENSAL: R$ {perfil.get('renda_mensal', 0):.2f}
PERFIL INVESTIDOR: {perfil.get('perfil_investidor', 'Não informado')}
ACEITA RISCO: {'Sim' if perfil.get('aceita_risco') else 'Não'}
OBJETIVO PRINCIPAL: {perfil['objetivo_principal']}
PATRIMÔNIO TOTAL: R$ {perfil['patrimonio_total']:.2f}
RESERVA DE EMERGÊNCIA: R$ {perfil['reserva_emergencia_atual']:.2f}

METAS:
{metas_txt}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

HISTÓRICO DE ATENDIMENTOS:
{historico.to_string(index=False)}
"""

SYSTEM_PROMPT = """Você é o Renda Clara, um assistente financeiro claro, prudente e didático.

OBJETIVO:
Ajudar o usuário a entender melhor seus gastos, seu contexto financeiro e seus padrões de comportamento com base nos dados fornecidos.

REGRAS:
- Responda apenas com base nos dados e no contexto disponíveis;
- NÃO invente valores, produtos, rendimentos, taxas ou informações que não estejam na base;
- Se a pergunta estiver fora do escopo financeiro ou fora dos dados disponíveis, responda com clareza que não possui essa informação;
- Você pode explicar gastos, categorias, padrões de consumo, organização financeira, metas e pontos de atenção;
- Evite recomendar investimentos específicos como se fosse consultoria individual;
- Use linguagem simples, clara e acolhedora;
- Quando possível, use os dados do cliente como exemplo prático;
- Se não souber algo, diga: "Não tenho essa informação nos dados disponíveis.";
- Responda de forma direta, com no máximo 3 parágrafos.
"""

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()["response"]

st.set_page_config(page_title="Renda Clara", page_icon="💸")
st.title("💸 Renda Clara")
st.caption("Seu assistente para entender gastos, contexto financeiro e padrões de consumo.")

if pergunta := st.chat_input("Pergunte sobre seus gastos ou sua situação financeira..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Analisando seus dados..."):
        st.chat_message("assistant").write(perguntar(pergunta))
