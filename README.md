# Pre-Entrega 1

Cliente LLM con streaming para OpenAI y Anthropic, usando un factory (`chain.py`).

## Requisitos

- Python 3.10+
- API keys de OpenAI y Anthropic

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración

Copia `.env.example` a `.env` y completa tus claves:

```bash
cp .env.example .env
```

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

Ambas variables tienen que estar definidas: `main.py` las lee con `os.environ[...]` y falla con `KeyError` si falta alguna.

## Uso

```bash
python main.py
```

Envía el prompt `"¿Qué es la entropía?"` a Anthropic (`claude-haiku-5-5`) y muestra la respuesta en streaming.

Para usar OpenAI, cambia el proveedor en `main.py`:

```python
client = LLMFactory.create_client(Provider.OPENAI, config)
```

Para usar ANTHROPIC, cambia el proveedor en `main.py`:

```python
client = LLMFactory.create_client(Provider.ANTHROPIC, config)
```

