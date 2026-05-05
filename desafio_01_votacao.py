votos = []

print("=" * 45)
print("   BEM-VINDO AO SISTEMA DE VOTAÇÃO")
print("=" * 45)
print("Candidatos:")
print("  1. Ana")
print("  2. Bruno")
print("  3. Carlos")
print("-" * 45)

while True:
    voto = input("\nDigite o nome do candidato (fim para encerrar): ")
    voto = voto.lower()

    if voto == "fim":
        break

    if voto == "ana" or voto == "bruno" or voto == "carlos":
        votos.append(voto)
        print("  Voto registrado para " + voto.capitalize() + "!")
    else:
        print("  Voto invalido. Tente novamente.")
        input("  Pressione Enter para continuar...")

print("\n" + "=" * 45)
print("         RESULTADO DA VOTAÇÃO")
print("=" * 45)

if len(votos) == 0:
    print("Nenhum voto foi registrado.")
else:
    votos_ana    = votos.count("ana")
    votos_bruno  = votos.count("bruno")
    votos_carlos = votos.count("carlos")

    print("Ana:    " + str(votos_ana) + " voto(s)")
    print("Bruno:  " + str(votos_bruno) + " voto(s)")
    print("Carlos: " + str(votos_carlos) + " voto(s)")
    print("-" * 45)

    maior = max(votos_ana, votos_bruno, votos_carlos)

    vencedores = []
    if votos_ana == maior:
        vencedores.append("Ana")
    if votos_bruno == maior:
        vencedores.append("Bruno")
    if votos_carlos == maior:
        vencedores.append("Carlos")

    if len(vencedores) > 1:
        print("Houve um empate entre os candidatos.")
    else:
        print("O vencedor e: " + vencedores[0])

print("=" * 45)