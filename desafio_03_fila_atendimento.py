fila = []

contador_senha = 1

print("=" * 45)
print("        SECRETARIA ACADÊMICA")
print("=" * 45)

while True:
    print("\n[1] - Retirar senha (entrar na fila)")
    print("[2] - Chamar próximo aluno")
    print("[3] - Mostrar fila atual")
    print("[4] - Sair")
    print("-" * 45)

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome do aluno: ").strip()
        if nome == "":
            print("  ✖ Nome inválido. Tente novamente.")
        else:
            aluno = {"nome": nome, "senha": contador_senha}
            fila.append(aluno)
            print(f"  ✔ {nome} entrou na fila de atendimento.")
            print(f"     Senha: {contador_senha:03d}")
            contador_senha += 1

    elif opcao == "2":
        if len(fila) == 0:
            print("  ✖ A fila está vazia. Nenhum aluno aguardando.")
        else:
            proximo = fila.pop(0)
            print(f"  📢 Chamando aluno: {proximo['nome']}")
            print(f"     Senha: {proximo['senha']:03d}")

            restantes = len(fila)
            if restantes == 0:
                print("     (A fila está agora vazia)")
            else:
                print(f"     ({restantes} aluno(s) ainda aguardando)")

    elif opcao == "3":
        if len(fila) == 0:
            print("  A fila está vazia.")
        else:
            print("  Fila atual:")
            for posicao, aluno in enumerate(fila, start=1):
                print(f"    {posicao}º - {aluno['nome']}  (Senha: {aluno['senha']:03d})")

    elif opcao == "4":
        print("\nEncerrando o sistema de atendimento.")
        if len(fila) > 0:
            print(f"Atenção: ainda há {len(fila)} aluno(s) na fila.")
        print("=" * 45)
        break

    else:
        print("  ✖ Opção inválida. Digite 1, 2, 3 ou 4.")
