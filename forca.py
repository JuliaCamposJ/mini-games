import random

def jogar_forca():
    # Lista de palavras com o tema "Qualidade de Software"
    palavras = ['BUG', 'TESTE', 'AUTOMACAO', 'CYPRESS', 'DOCKER', 'QUALIDADE', 'REQUERIMENTO']
    # Escolhe uma palavra aleatoriamente
    palavra = random.choice(palavras).upper()
    palavra_escondida = ['_' for _ in palavra]
    tentativas = 6
    letras_chutadas = []

    print("=== BEM-VINDO AO JOGO DA FORCA DO QA! ===")
    print(f"Tema: Ferramentas e Conceitos de Qualidade")

    while tentativas > 0 and '_' in palavra_escondida:
        print(f"\nPalavra: {' '.join(palavra_escondida)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras tentadas: {', '.join(letras_chutadas)}")

        chute = input("Digite uma letra: ").upper()

        if not chute.isalpha() or len(chute) != 1:
            print("Por favor, digite apenas uma letra válida.")
            continue

        if chute in letras_chutadas:
            print("Você já tentou essa letra. Tente outra!")
            continue

        letras_chutadas.append(chute)

        if chute in palavra:
            print(f"Boa! A letra {chute} está na palavra.")
            for i in range(len(palavra)):
                if palavra[i] == chute:
                    palavra_escondida[i] = chute
        else:
            print(f"Ops! A letra {chute} não está na palavra.")
            tentativas -= 1

    if '_' not in palavra_escondida:
        print(f"\n🎉 PARABÉNS! Você descobriu a palavra: {' '.join(palavra_escondida)}")
    else:
        print(f"\n💥 GAME OVER! Você perdeu. A palavra era: {palavra}")

if __name__ == "__main__":
    jogar_forca()
