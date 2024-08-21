import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def list_users():
    response = requests.get(BASE_URL)
    response.raise_for_status()  
    return response.json()

def create_user(name, username, email):
    user_data = {
        "name": name,
        "username": username,
        "email": email
    }
    response = requests.post(BASE_URL, json=user_data)
    response.raise_for_status()
    return response.json()

def read_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def update_user(user_id, name=None, username=None, email=None):
    user_data = {}
    if name:
        user_data['name'] = name
    if username:
        user_data['username'] = username
    if email:
        user_data['email'] = email

    url = f"{BASE_URL}/{user_id}"
    response = requests.patch(url, json=user_data)
    response.raise_for_status()
    return response.json()

def delete_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url)
    response.raise_for_status()
    return {"message": f"Usuário com ID {user_id} deletado com sucesso."}
