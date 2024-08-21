import requests
import json
BASE_URL = "https://jsonplaceholder.typicode.com/users"

def listar_usuarios():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
    else:
        print(f"Falha ao recuperar usuários. Código de status: {response.status_code}")

def listar_tarefas_usuario(user_id):
    url = f"{BASE_URL}/{user_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        tarefas = response.json()
        for tarefa in tarefas:
            status = "Concluída" if tarefa['completed'] else "Não Concluída"
            print(f"ID: {tarefa['id']}, Título: {tarefa['title']}, Status: {status}")
    else:
        print(f"Falha ao recuperar tarefas. Código de status: {response.status_code}")

def criar_usuario():
    nome = input("Digite o nome: ")
    nome_usuario = input("Digite o nome de usuário: ")
    email = input("Digite o email: ")

    dados_usuario = {
        "name": nome,
        "username": nome_usuario,
        "email": email
    }

    response = requests.post(BASE_URL, json=dados_usuario)
    if response.status_code == 201:
        print("Usuário criado com sucesso:", response.json())
    else:
        print(f"Falha ao criar usuário. Código de status: {response.status_code}")

def ler_usuario(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        usuario = response.json()
        print(json.dumps(usuario, indent=4))
    else:
        print(f"Falha ao recuperar usuário. Código de status: {response.status_code}")

def atualizar_usuario(user_id):
    print("Deixe os campos em branco se não quiser modificar.")
    nome = input("Digite o novo nome: ")
    nome_usuario = input("Digite o novo nome de usuário: ")
    email = input("Digite o novo email: ")

    dados_usuario = {}
    if nome:
        dados_usuario['name'] = nome
    if nome_usuario:
        dados_usuario['username'] = nome_usuario
    if email:
        dados_usuario['email'] = email

    if dados_usuario:
        url = f"{BASE_URL}/{user_id}"
        response = requests.patch(url, json=dados_usuario)
        if response.status_code == 200:
            print("Usuário atualizado com sucesso:", response.json())
        else:
            print(f"Falha ao atualizar usuário. Código de status: {response.status_code}")
    else:
        print("Nenhuma atualização fornecida.")

def deletar_usuario(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Usuário com ID {user_id} deletado com sucesso.")
    else:
        print(f"Falha ao deletar usuário. Código de Status: {response.status_code}")

def main():
    while True:
        print("\nCLI da JSONPlaceholder - Gerenciamento de Usuários")
        print("1. Listar todos os usuários")
        print("2. Listar as tarefas de um usuário específico")
        print("3. criar um novo usuário")
        print("4. Ler detalhes de um usuário")
        print("5. Atualizar um usuário")
        print("6. Deletar um usuário")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            user_id = input("Digite o ID do usuário: ")
            listar_tarefas_usuario(user_id)
        elif opcao == '3':
            criar_usuario()
        elif opcao == '4':
            user_id = input("Digite o ID do usuário: ")
            ler_usuario(user_id)
        elif opcao == '5':
            user_id = input("Digite o ID do usuário: ")
            atualizar_usuario(user_id)
        elif opcao == '6':
            user_id = input("Digite o ID do usuário: ")
            deletar_usuario(user_id)
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
