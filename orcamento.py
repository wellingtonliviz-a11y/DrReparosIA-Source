
def calcular_total(mao_de_obra, material):
    total = mao_de_obra + material
    return total

def classificar_orcamento(total):
 if total >= 200:
    classificacao = "Orçamento de maior valor"
 else:
    classificacao = "Orçamento de menor valor"
 return classificacao

servicos = [
    "Troca de torneira",
    "Troca de sifão",
    "Instalação de chuveiro",
    "Instalação de suporte de TV"
]
precos = {
    "Troca de torneira": 80.00,
    "Troca de sifão": 70.00,
    "Instalação de chuveiro": 120.00,
    "Instalação de suporte de TV": 150.00
}

print(precos["Troca de sifão"])

for numero, servico in enumerate(servicos, start=1):
    print(numero, "-", servico)

print("DR Reparos IA")

opcao = int(input("Digite o número do serviço desejado: "))
servico = servicos[opcao - 1]

preco_padrao = precos[servico]

print("Serviço escolhido:", servico)
print("Preço padrão:", preco_padrao)

mao_de_obra = preco_padrao
alterar = input("Deseja alterar o preço da mão de obra? (s/n): ") .lower()

if alterar == "s":
    mao_de_obra = float(input("Digite o novo valor: R$ ").replace(",", "."))

material = float(input("Digite o valor do material: R$ ").replace(",", "."))

total = calcular_total(mao_de_obra, material)
classificacao = classificar_orcamento(total)




    
print()
print("==============================")
print("        DR REPAROS IA")
print("==============================")
print(f"Serviço: {servico}")
print(f"Mão de obra: R$ {mao_de_obra:.2f}".replace(".", ","))
print(f"Material: R$ {material:.2f}".replace(".", ","))
print("------------------------------")
print(f"TOTAL: R$ {total:.2f}".replace(".", ","))
print(f"Classificação: {classificacao}")
print("==============================")