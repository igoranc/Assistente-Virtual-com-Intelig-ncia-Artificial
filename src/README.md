# Renda Clara 💸

## Passo a passo de execução

### Setup do Ollama

1. Instalar o Ollama em [ollama.com](https://ollama.com).
2. Baixar um modelo leve:

```bash
ollama pull gpt-oss
```

3. Testar se está funcionando:

```bash
ollama run gpt-oss "Olá!"
```

## Código completo

Todo o código-fonte está no arquivo `app.py`.

## Como rodar

1. Instalar as dependências:

```bash
pip install streamlit pandas requests
```

2. Garantir que o Ollama esteja em execução:

```bash
ollama serve
```

3. Rodar o app:

```bash
streamlit run .\src\app.py
```
