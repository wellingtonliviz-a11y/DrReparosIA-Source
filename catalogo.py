"""Catálogo central de produtos/links de afiliado do Dr Reparos IA.

Os links ficam aqui para que possam ser trocados sem editar os templates.
A plataforma só exibe o produto quando ele faz sentido para o diagnóstico.
"""

PRODUTOS = {
    "salva_registro": {
        "nome": "Kit salva registro para registro de pressão",
        "url_compra": "https://meli.la/1QLDNgm",
    },
    "caixa_acoplada": {
        "nome": "Kit universal para caixa acoplada",
        "url_compra": "https://meli.la/1sNFuAi",
    },
    "sifao": {
        "nome": "Sifão padrão",
        "url_compra": "https://meli.la/1vRK7Ru",
    },
    "hydra_max_2550": {
        "nome": "Reparo Hydra Max 2550",
        "url_compra": "https://meli.la/2igPGqa",
    },
    "hydra_luxo": {
        "nome": "Reparo Hydra Luxo com acionador",
        "url_compra": "https://meli.la/1Sfrjjv",
    },
    "docol_1_1_2": {
        "nome": "Reparo Docol 1 1/2",
        "url_compra": "https://meli.la/2Bdk4co",
    },
    "docol_1_1_4_ri484": {
        "nome": "Reparo Docol 1 1/4 RI484",
        "url_compra": "https://meli.la/1D1aDQJ",
    },
    "lorenzetti_p21": {
        "nome": "Reparo descarga Lorenzetti P21",
        "url_compra": "https://meli.la/1aRkZTW",
    },
    "lorenzetti_p41": {
        "nome": "Reparo descarga Lorenzetti P41",
        "url_compra": "https://meli.la/2mkFLPg",
    },
    "lorenshower_220_6800": {
        "nome": "Chuveiro Lorenshower 220 V 6.800 W",
        "url_compra": "https://meli.la/2zAFi5P",
    },
    "wago": {
        "nome": "Conector Wago",
        "url_compra": "https://meli.la/1zZpRvp",
    },
    "flexivel_aco_60": {
        "nome": "Engate flexível trama de aço 60 cm",
        "url_compra": "https://meli.la/273gP6C",
    },
}

# Compatibilidade específica das válvulas de parede.
VALVULAS_PAREDE = {
    "hydra-max-2550": {"marca": "Hydra", "modelo": "Max 2550", "produto": "hydra_max_2550"},
    "hydra-luxo": {"marca": "Hydra", "modelo": "Luxo com acionador", "produto": "hydra_luxo"},
    "docol-1-1-2": {"marca": "Docol", "modelo": "1 1/2", "produto": "docol_1_1_2"},
    "docol-1-1-4-ri484": {"marca": "Docol", "modelo": "1 1/4 RI484", "produto": "docol_1_1_4_ri484"},
    "lorenzetti-p21": {"marca": "Lorenzetti", "modelo": "P21", "produto": "lorenzetti_p21"},
    "lorenzetti-p41": {"marca": "Lorenzetti", "modelo": "P41", "produto": "lorenzetti_p41"},
}
