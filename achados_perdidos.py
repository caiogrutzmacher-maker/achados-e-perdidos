# ==========================================================
# FUNÇÃO PARA CADASTRAR UM OBJETO
# ==========================================================
def cadastrar_item(itens):
    # Mostra o título da tela de cadastro.
    print("\n--- CADASTRO DE OBJETO ---")
   
    # Solicita os dados do objeto.
    nome = input("Nome do objeto: ")
    descricao = input("Descrição do objeto: ")
    local = input("Local onde foi encontrado: ")
    data = input("Data do registro (dd/mm/aaaa): ")

    # Validação dos campos obrigatórios.
    if nome.strip() == "":
        print("\nO nome do objeto não pode ficar vazio.")
        return
    if descricao.strip() == "":
        print("\nA descrição não pode ficar vazia.")
        return
    if local.strip() == "":
        print("\nO local não pode ficar vazio.")
        return
    if data.strip() == "":
        print("\nA data não pode ficar vazia.")
        return

    # Cria o dicionário com os dados do objeto.
    item = {
        "nome": nome,
        "descricao": descricao,
        "local": local,
        "data": data
    }

    # Adiciona o dicionário à lista de objetos.
    itens.append(item)
    print("\nObjeto cadastrado com sucesso!")


# ==========================================================
# FUNÇÃO PARA MOSTRAR O MENU
# ==========================================================
def mostrar_menu():
    print("\n================================")
    print(" ACHADOS E PERDIDOS DA ESCOLA")
    print("================================")
    print("1 - Cadastrar objeto")
    print("2 - Listar objetos")
    print("3 - Excluir objeto")
    print("4 - Sair")


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================
def main():
    # Cria uma lista vazia para armazenar os objetos.
    itens = []

    # Mantém o sistema funcionando continuamente.
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_item(itens)
        elif opcao == "2":
            print(itens)
        elif opcao == "3":
            print("\nA exclusão será criada em outra aula.")
        elif opcao == "4":
            print("\nPrograma encerrado.")
            break
        else:
            print("\nOpção inválida. Digite 1, 2, 3 ou 4.")


# ==========================================================
# INÍCIO DO PROGRAMA
# ==========================================================
main()
