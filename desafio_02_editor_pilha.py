pilha = []

print("=" * 40)
print("       EDITOR DE TEXTO")
print("=" * 40)

while True:
    print("\n[1] - Digitar palavra")
    print("[2] - Desfazer ultima palavra")
    print("[3] - Mostrar texto")
    print("[4] - Sair")
    print("-" * 40)

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        palavra = input("Digite uma palavra: ")

        if palavra == "":
            print("  Palavra vazia. Nada foi adicionado.")
        else:
            pilha.append(palavra)
            print("  Palavra adicionada: " + palavra)

    elif opcao == "2":
        if len(pilha) == 0:
            print("  Nada para desfazer. O editor esta vazio.")
        else:
            removida = pilha.pop()
            print("  Palavra removida: " + removida)

    elif opcao == "3":
        if len(pilha) == 0:
            print("  (O editor esta vazio)")
        else:

            texto = ""
            for i in range(len(pilha)):
                if i == 0:
                    texto = pilha[i]
                else:
                    texto = texto + " " + pilha[i]

            print("  Texto atual: " + texto)

    elif opcao == "4":
        print("\nSaindo do editor...")

        if len(pilha) == 0:
            print("Nenhum texto foi digitado.")
        else:
            texto_final = ""
            for i in range(len(pilha)):
                if i == 0:
                    texto_final = pilha[i]
                else:
                    texto_final = texto_final + " " + pilha[i]

            print("Texto salvo: " + texto_final)

        print("=" * 40)
        break

    else:
        print("  Opcao invalida. Digite 1, 2, 3 ou 4.")