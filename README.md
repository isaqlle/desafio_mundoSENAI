# Desafio Digital — base Python

## Rodar no computador

1. Instale Python 3.
2. Abra o terminal nesta pasta.
3. Execute:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Depois:

```bash
pip install -r requirements.txt
python app.py
```

Abra no navegador:
http://127.0.0.1:5000

## Estrutura

- `/` = painel das quatro estações
- `/ux` = Mini-App 1
- `/api/ux/check` = validação Python da missão UX
- Mini-Apps 2, 3 e 4 serão acrescentados mantendo a independência entre as estações.
