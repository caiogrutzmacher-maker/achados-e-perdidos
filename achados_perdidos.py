
def mostrar_menu():
print("\n================================")
print(" ACHADOS E PERDIDOS DA ESCOLA")
print("================================")
print("1 - Cadastrar objeto")
print("2 - Listar objetos")
print("3 - Excluir objeto")
print("4 - Sair")

mostrar_menu()

def main():
mostrar_menu()
opcao = input("\nEscolha uma opção: ")
print("Você escolheu a opção:", opcao)

main()
