print("=" * 40)
print("          DR REPAROS IA")
print("=" * 40)

print("\nOlá! 👋")
print("Vou ajudar você a resolver um problema na sua casa.")

print("\nComo você gostaria de começar?")
print("1 - Resolver meu problema com a IA")
print("2 - Falar com um especialista por videochamada")
print("3 - Solicitar atendimento presencial")

opcao = input("\nEscolha uma opção: ")

if opcao == "1":
    print("\nVamos começar o diagnóstico.")

    print("\nQual problema você está enfrentando?")
    print("1 - Descarga vazando")
    print("2 - Torneira vazando")
    print("3 - Sifão vazando")
    print("4 - Chuveiro com problema")

    problema = input("\nEscolha uma opção: ")

    if problema == "1":
        print("\nVocê escolheu: Descarga vazando")

        print("\nQual tipo de descarga você possui?")
        print("1 - Caixa acoplada")
        print("2 - Válvula na parede")
        print("3 - Não sei identificar")

        tipo_descarga = input("\nEscolha uma opção: ")

        print("\nTipo de descarga selecionado:", tipo_descarga)
        

if tipo_descarga == "1":
    print("\nVamos identificar o problema da sua caixa acoplada.")

    print("\nO que está acontecendo?")
    print("1 - A água não para de cair dentro do vaso")
    print("2 - A caixa não enche")
    print("3 - A caixa demora muito para encher")
    print("4 - A descarga está fraca")
    print("5 - Está vazando água por fora da caixa")
    print("6 - Outro problema")

    sintoma = input("\nEscolha uma opção: ")

    if sintoma == "1":
        print("\nEntendi. A água está passando continuamente para dentro do vaso.")
        print("Vamos descobrir a possível causa antes de mexer em qualquer peça.")

        if sintoma == "1":
         print("\nEntendi. A água está passando continuamente para dentro do vaso.")
         print("Vamos descobrir a possível causa antes de mexer em qualquer peça.")

         print("\nObserve a água dentro da caixa acoplada.")

        print("\nO nível da água sobe até o tubo ladrão/extravasor?")
        print("1 - Sim")
        print("2 - Não")
        print("3 - Não sei identificar")

    nivel_agua = input("\nEscolha uma opção: ")

    if nivel_agua == "1":
        print("\nPossível problema no mecanismo de entrada ou na regulagem da boia.")
        print("Vamos fazer mais um teste.")

    elif nivel_agua == "2":
        print("\nA água não está transbordando pelo extravasor.")
        print("A possível causa pode estar na vedação do mecanismo de saída.")

    elif nivel_agua == "3":
        print("\nSem problema. Futuramente poderemos analisar uma foto ou vídeo.")

    else:
        print("\nOpção inválida.")

elif opcao == "2":
    print("\nEm breve você poderá agendar uma videochamada com um especialista.")

elif opcao == "3":
    print("\nVamos iniciar a solicitação de atendimento presencial.")

else:
    print("\nOpção inválida.")