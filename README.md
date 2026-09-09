# Dr Reparos IA — V4

Protótipo Flask para diagnóstico guiado e orientação de pequenos reparos residenciais.

## Módulos disponíveis

- Válvulas de parede: Hydra Max 2550, Hydra Luxo com acionador, Docol 1 1/2, Docol 1 1/4 RI484, Lorenzetti P21 e P41.
- Caixa acoplada: diagnóstico por ladrão/boia ou torre central.
- Substituição de sifão, incluindo anéis de vedação e adaptador de lavatório.
- Troca de engate flexível.
- Reparo de registro de pressão do chuveiro.
- Instalação de chuveiro com conector Wago com orientações de segurança.
- Upload de foto preparado para futura análise por IA.
- Videochamada e atendimento presencial como rotas de apoio.

## Produtos

Os links de afiliado ficam centralizados em `catalogo.py`. Para alterar um produto ou link, edite apenas esse arquivo.

## Como executar

```bash
pip install -r requirements.txt
python app.py
```

Abra `http://127.0.0.1:5000`.

## Segurança

Não inclua seu `.env` em ZIPs ou repositórios. A V4 contém apenas `.env.example`.

O módulo elétrico exige circuito desenergizado e confirmação de ausência de tensão. Em caso de dúvida sobre dimensionamento, aterramento ou ausência de tensão, o fluxo orienta interromper e procurar profissional qualificado.


## Versão 5
A V5 amplia os módulos ativos com passo a passo completo, materiais/ferramentas, links de compra, confirmação de segurança elétrica e finalização do reparo.
