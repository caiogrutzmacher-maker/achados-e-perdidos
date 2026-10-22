# SISTEMA DE ACHADOS E PERDIDOS DA ESCOLA
# Permite cadastrar, listar e excluir objetos pelo terminal.

# csv: permite ler e gravar informações em arquivos CSV (tipo de planilha simples).
# os: permite trabalhar com caminhos e verificar se arquivos existem.
import csv
import os

# Define os arquivos que guardarão os objetos cadastrados e excluídos.
# __file__ indica o arquivo Python atual; dirname encontra a pasta onde ele está.
ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "achados_perdidos.csv")
ARQUIVO_EXCLUIDOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "objetos_excluidos.csv")
# Nomes das colunas usadas no arquivo de objetos cadastrados.
CAMPOS = ["nome", "descricao", "local", "data"]


# Salva a lista de objetos no CSV. O modo "w" grava o conteúdo do zero.
def salvar_itens(itens):
    # with fecha o arquivo automaticamente; utf-8 permite acentos.
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()  # Escreve os nomes das colunas.
        escritor.writerows(itens)  # Escreve todos os objetos cadastrados.


# Carrega os objetos salvos quando o programa é iniciado.
def carregar_itens():
    itens = []  # Lista que armazenará os objetos em memória.
    if os.path.exists(ARQUIVO):  # Só tenta ler se o CSV existir.
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)  # Lê cada linha como um dicionário.
            for linha in leitor:  # Percorre todas as linhas do arquivo.
                itens.append(linha)  # Adiciona cada objeto à lista.
    return itens  # Devolve a lista para o restante do sistema.


# Registra o objeto excluído em outro CSV, junto com o motivo da exclusão.
def salvar_item_excluido(item, motivo):
    # Verifica se o arquivo já existe e possui conteúdo.
    arquivo_existe = os.path.exists(ARQUIVO_EXCLUIDOS) and os.path.getsize(ARQUIVO_EXCLUIDOS) > 0
    # O modo "a" acrescenta registros sem apagar os anteriores.
    with open(ARQUIVO_EXCLUIDOS, "a", newline="", encoding="utf-8") as arquivo:
        campos = CAMPOS + ["motivo_exclusao"]  # Acrescenta uma coluna.
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        if not arquivo_existe:
            escritor.writeheader()  # Cria o cabeçalho apenas quando necessário.
        # **item copia os dados do objeto e adiciona o motivo da exclusão.
        escritor.writerow({**item, "motivo_exclusao": motivo})


# Mostra na tela todos os objetos que ainda estão cadastrados.
def listar_itens(itens):
    print("\n--- OBJETOS CADASTRADOS ---")
    if len(itens) == 0:  # len informa quantos objetos existem na lista.
        print("Nenhum objeto cadastrado.")
        return  # Encerra esta função se a lista estiver vazia.
    # enumerate numera os objetos começando em 1.
    for numero, item in enumerate(itens, start=1):
        print(f"\nObjeto {numero}")
        # item['nome'] acessa o campo nome do objeto (dicionário).
        print(f"Nome: {item['nome']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Local: {item['local']}")
        print(f"Data: {item['data']}")
        print("-" * 30)


# Solicita os dados de um novo objeto e realiza seu cadastro.
def cadastrar_item(itens):
    print("\n--- CADASTRO DE OBJETO ---")
    # input recebe as informações digitadas pelo usuário.
    nome = input("Nome do objeto: ")
    descricao = input("Descrição: ")
    local = input("Local encontrado: ")
    data = input("Data (dd/mm/aaaa): ")
    # strip remove espaços nas pontas para impedir campos apenas com espaços.
    # return interrompe o cadastro se algum campo estiver vazio.
    if nome.strip() == "":
        print("Nome obrigatório.")
        return
    if descricao.strip() == "":
        print("Descrição obrigatória.")
        return
    if local.strip() == "":
        print("Local obrigatório.")
        return
    if data.strip() == "":
        print("Data obrigatória.")
        return
    # Dicionário: organiza os dados com os nomes de cada campo.
    item = {"nome": nome, "descricao": descricao, "local": local, "data": data}
    itens.append(item)  # Adiciona o novo objeto à lista.
    salvar_itens(itens)  # Atualiza o arquivo CSV com o novo cadastro.
    print("Objeto cadastrado com sucesso!")


# Exclui um objeto após solicitar motivo e confirmação.
def excluir_item(itens):
    print("\n--- EXCLUSÃO DE OBJETO ---")
    if len(itens) == 0:
        print("Nenhum objeto cadastrado.")
        return
    listar_itens(itens)  # Mostra os objetos para escolher qual excluir.
    try:  # Tenta executar uma conversão que pode gerar erro.
        numero = int(input("\nNúmero do objeto: "))  # int converte texto em número inteiro.
        # Impede escolher uma posição que não existe na lista.
        if numero < 1 or numero > len(itens):
            print("Número inválido.")
            return
        # Listas Python começam no índice 0; por isso usamos numero - 1.
        item_escolhido = itens[numero - 1]
        print(f"Objeto: {item_escolhido['nome']}")
        motivo = input("Motivo da exclusão: ")
        if motivo.strip() == "":
            print("Motivo obrigatório.")
            return
        confirmacao = input("Confirmar exclusão? (S/N): ")
        # upper transforma a resposta em maiúscula, aceitando 's' ou 'S'.
        if confirmacao.upper() == "S":
            salvar_item_excluido(item_escolhido, motivo)  # Guarda o histórico.
            itens.pop(numero - 1)  # Remove o objeto da lista de cadastrados.
            salvar_itens(itens)  # Atualiza o CSV principal sem esse objeto.
            print("Objeto excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    except ValueError:
        # Evita que o programa pare se o usuário digitar letras no número.
        print("Digite somente números.")


# Exibe as opções disponíveis para o usuário.
def mostrar_menu():
    print("\n================================")
    print(" ACHADOS E PERDIDOS DA ESCOLA")
    print("================================")
    print("1 - Cadastrar objeto")
    print("2 - Listar objetos")
    print("3 - Excluir objeto")
    print("4 - Sair")


# Função principal: controla o menu e chama as demais funções.
def main():
    itens = carregar_itens()  # Recupera os cadastros salvos anteriormente.
    while True:  # Repete o menu até o usuário escolher sair.
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")
        # if e elif verificam qual opção foi digitada.
        if opcao == "1":
            cadastrar_item(itens)
        elif opcao == "2":
            listar_itens(itens)
        elif opcao == "3":
            excluir_item(itens)
        elif opcao == "4":
            print("\nPrograma encerrado.")
            break  # Interrompe o while e encerra o programa.
        else:
            print("\nOpção inválida. Digite 1, 2, 3 ou 4.")


# Executa main apenas quando este arquivo é iniciado diretamente.
if __name__ == "__main__":
    main()
