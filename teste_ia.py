import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

chave = os.getenv("OPENAI_API_KEY")

if not chave:
    print("ERRO: chave da API não encontrada no arquivo .env")
else:
    print("Chave encontrada com segurança.")

    client = OpenAI(api_key=chave)

    try:
        resposta = client.responses.create(
            model="gpt-5.6-luna",
            input="Responda somente: Dr Reparos IA conectado com sucesso."
        )

        print("\nResposta da IA:")
        print(resposta.output_text)

    except Exception as erro:
        print("\nOcorreu um erro:")
        print(erro)