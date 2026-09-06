# Importa todas as funções explicitamente do arquivo funcoes.py
from funcoes import (limpar_tela,cadastrar_alunos,listar_alunos,buscar_alunos,atualizar_notas,excluir_alunos)

def menu():
    """Exibe o menu do sistema e retorna a opção digitada pelo usuário."""
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTÃO DE ALUNOS".center(50))
    print("=" * 50)
    print("[1] Cadastrar Aluno")
    print("[2] Listar Alunos")
    print("[3] Buscar Aluno")
    print("[4] Atualizar Notas")
    print("[5] Remover Aluno")
    print("[0] Sair do Sistema")
    print("=" * 50)
    return input("Escolha uma opção: ").strip()

def main():
    # Dicionário de alunos mantido em memória
    alunos_dict = {}

    while True:
        limpar_tela()
        # O menu é chamado A CADA CICLO dentro do laço
        opcao = menu()

        if opcao == "1":
            cadastrar_alunos(alunos_dict)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "2":
            listar_alunos(alunos_dict)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "3":
            buscar_alunos(alunos_dict)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "4":
            atualizar_notas(alunos_dict)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "5":
            excluir_alunos(alunos_dict)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "0":
            limpar_tela()
            print("\nSaindo do sistema... Até logo! 👋\n")
            break
        else:
            print("\n⚠️ Opção inválida! Digite um número de 0 a 5.")
            input("\nPressione ENTER para tentar novamente...")

    # Garante a execução apenas quando rodado diretamente
if __name__ == "__main__":
    main()