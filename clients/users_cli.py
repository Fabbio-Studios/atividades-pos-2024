import users_wrapper as users
import requests

def listar_usuarios():
    try:
        usuarios = users.list_users()
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao listar usuários: {e}")

def criar_usuario():
    nome = input("Digite o nome: ")
    nome_usuario = input("Digite o nome de usuário: ")
    email = input("Digite o email: ")

    try:
        usuario = users.create_user(nome, nome_usuario, email)
        print("Usuário criado com sucesso:", usuario)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao criar usuário: {e}")

def ler_usuario():
    user_id = input("Digite o ID do usuário: ")
    try:
        usuario = users.read_user(user_id)
        print(usuario)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao ler usuário: {e}")

def atualizar_usuario():
    user_id = input("Digite o ID do usuário: ")
    print("Deixe os campos em branco se não quiser modificar.")
    nome = input("Digite o novo nome: ")
    nome_usuario = input("Digite o novo nome de usuário: ")
    email = input("Digite o novo email: ")

    try:
        usuario = users.update_user(user_id, nome, nome_usuario, email)
        print("Usuário atualizado com sucesso:", usuario)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao atualizar usuário: {e}")

def deletar_usuario():
    user_id = input("Digite o ID do usuário: ")
    try:
        resultado = users.delete_user(user_id)
        print(resultado["message"])
    except requests.exceptions.RequestException as e:
        print(f"Erro ao deletar usuário: {e}")

def main():
    while True:
        print("\nCLI para JSONPlaceholder - Gerenciamento de Usuários")
        print("1. Listar todos os usuários")
        print("2. Criar um novo usuário")
        print("3. Ler detalhes de um usuário")
        print("4. Atualizar um usuário")
        print("5. Deletar um usuário")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            criar_usuario()
        elif opcao == '3':
            ler_usuario()
        elif opcao == '4':
            atualizar_usuario()
        elif opcao == '5':
            deletar_usuario()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
