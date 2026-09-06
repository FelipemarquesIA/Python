import os
def limpar_tela():
    # Detecta o sistema operacional e limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_alunos(alunos_dict):
        # Menu de exibição
    print("\n" + "=" * 50)
    print("CADASTRO DE ALUNO".center(50))
    print("=" * 50)

    # Recebendo dados
    nome = input("Digite o nome do aluno..: ").strip().upper()
    nota1 = float(input("Digite a 1ª nota..: "))
    nota2 = float(input("Digite a 2ª nota..: "))

    # Calculando e arredondando a média
    media = round((nota1 + nota2) / 2, 2)

    # Verificando a situação
    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"

    # Exibindo a situação e a média formatada
    print(f"\nSituação: {situacao} (Média: {media})")

    # Armazenando no dicionário que foi passado como parâmetro
    alunos_dict[nome] = {
        "notas": [nota1, nota2],
        "media": media,
        "situacao": situacao,
    }
    print("\n--- DEBUG: CONTEÚDO ATUAL DO DICIONÁRIO ---")
    print(alunos_dict)
    print("------------------------------------------"  )
    print(f"✅ Aluno {nome} cadastrado com sucesso!")

def listar_alunos(alunos_dict):
    """Percorre o dicionário e exibe todos os alunos cadastrados de forma formatada."""
    print("\n" + "=" * 50)
    print("RELATÓRIO DE ALUNOS CADASTRADOS".center(50))
    print("=" * 50)

    # Verificação de segurança: se o dicionário estiver vazio, encerra a função
    if not alunos_dict:
        print("⚠️ Nenhum aluno cadastrado no sistema.")
        # return

    # Iteração principal sobre cada aluno cadastrado
    for nome, dados in alunos_dict.items():
        print(f"Nome     : {nome}")

        # Exibindo as notas com o laço for dinâmico
        print("Notas    : ", end="")
        for nota in dados["notas"]: 
            print(f"{nota}", end=" | ")
        print()  # Quebra de linha após imprimir todas as notas

        print(f"Média    : {dados['media']}")
        print(f"Situação : {dados['situacao']}")
        print("-" * 50)

def buscar_alunos(alunos_dict):
    """Percorre o dicionário e busca 1 aluno cadastradode forma formatada."""
    print("\n" + "=" *   50)
    print("CONSULTA DE ALUNO".center(50))
    print("=" * 50)

    nome = input("Digite o nome do aluno que deseja procurar: ").strip().upper()

    # 1. Verifica se a chave existe no dicionário
    if nome in alunos_dict:
        # 2. Resgata o dicionário interno do aluno direto pela chave
        dados = alunos_dict[nome]

        print(f"\nNome     : {nome}")

        # Exibindo as notas com o seu laço for dinâmico
        print("Notas    : ", end="")
        for nota in dados["notas"]:
            print(f"{nota}", end=" | ")
        print()  # Quebra de linha

        print(f"Média    : {dados['media']}")
        print(f"Situação : {dados['situacao']}")
        print("-" * 50)

    # 3. Trata o caso em que o aluno não está cadastrado
    else:
        print(f"\n⚠️ Aluno '{nome}' não encontrado no sistema.")
        

def excluir_alunos(alunos_dict):
    """Solicita o nome do aluno, pede confirmação e remove a chave do dicionário."""
    print("\n" + "=" * 50)
    print("REMOVER ALUNO".center(50))
    print("=" * 50)

    nome = input("Digite o nome do aluno que deseja excluir: ").strip().upper()

    # 1. Verifica se o aluno existe no dicionário
    if nome in alunos_dict:
    # 2. Pergunta de confirmação de segurança
        confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (S/N): ").strip().upper()

        if confirmacao == "S":
            del alunos_dict[nome]
            print(f"\n✅ Aluno '{nome}' removido com sucesso!")
        else:
            print("\n❌ Operação cancelada. O aluno não foi removido.")

    # 3. Caso o aluno não exista
    else:
        print(f"\n⚠️ Aluno '{nome}' não encontrado no sistema.")

    print("-" * 50)

def atualizar_notas(alunos_dict):
    """Permite atualizar as notas, recalcula a média e a situação do aluno."""
    print("\n" + "=" * 50)
    print("ATUALIZAR NOTAS".center(50))
    print("=" * 50)

    nome = input("Digite o nome do aluno: ").strip().upper()

    if nome in alunos_dict:
        confirmacao = (input(f"Confirma a alteração das notas de '{nome}'? (S/N): ").strip().upper())

        if confirmacao == "S":
            print(f"\n--- Digite as novas notas para {nome} ---")
            nota1 = float(input("Digite a nota 1: "))
            nota2 = float(input("Digite a nota 2: "))

            media = (nota1 + nota2) / 2

            if media >= 7:
                situacao = "APROVADO"
            elif media >= 5:
                situacao = "RECUPERAÇÃO"
            else:
                situacao = "REPROVADO"

            # ATUALIZAÇÃO DOS DADOS NO DICIONÁRIO
            alunos_dict[nome]["notas"] = [nota1, nota2]
            alunos_dict[nome]["media"] = media
            alunos_dict[nome]["situacao"] = situacao

            print(f"\n✅ Notas de '{nome}' atualizadas com sucesso!")
            print(f"Nova Média: {media:.1f} | Nova Situação: {situacao}")
        else:
            print("\n❌ Atualização cancelada pelo usuário.")
    else:
        print(f"\n⚠️ Aluno '{nome}' não encontrado no sistema.")

    print("-" * 50)