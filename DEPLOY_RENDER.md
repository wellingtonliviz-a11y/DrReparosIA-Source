# Publicar no Render

1. Envie esta pasta para um repositório GitHub. Não envie `.env`.
2. No Render, crie um Blueprint apontando para o repositório ou um Web Service.
3. Se usar Web Service manual:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: Free
4. Variáveis:
   - `FLASK_SECRET_KEY`: gere um valor aleatório.
   - `OPENAI_API_KEY`: opcional enquanto a IA real estiver desativada.
5. O upload local é temporário no plano Free e pode ser perdido em restart/redeploy.
