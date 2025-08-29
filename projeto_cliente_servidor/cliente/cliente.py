import requests

API_URL = "http://127.0.0.1:5000"

def listar_funcionarios():
    resposta = requests.get(f"{API_URL}/funcionarios")
    print(resposta.json())

def buscar_funcionario(id):
    resposta = requests.get(f"{API_URL}/funcionarios/{id}")
    print(resposta.json())

def adicionar_funcionario(nome, cargo, salario):
    novo = {"nome": nome, "cargo": cargo, "salario": salario}
    resposta = requests.post(f"{API_URL}/funcionarios", json=novo)
    print(resposta.json())

def atualizar_funcionario(id, nome=None, cargo=None, salario=None):
    dados = {}
    if nome: dados["nome"] = nome
    if cargo: dados["cargo"] = cargo
    if salario: dados["salario"] = salario
    resposta = requests.put(f"{API_URL}/funcionarios/{id}", json=dados)
    print(resposta.json())

def deletar_funcionario(id):
    resposta = requests.delete(f"{API_URL}/funcionarios/{id}")
    print(resposta.json())

def menu():
    while True:
        print("\n===== CLIENTE API FUNCIONÁRIOS =====")
        print("1 - Listar funcionários")
        print("2 - Buscar funcionário por ID")
        print("3 - Adicionar funcionário")
        print("4 - Atualizar funcionário")
        print("5 - Deletar funcionário")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            listar_funcionarios()
        elif opcao == "2":
            id = int(input("ID: "))
            buscar_funcionario(id)
        elif opcao == "3":
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            adicionar_funcionario(nome, cargo, salario)
        elif opcao == "4":
            id = int(input("ID: "))
            nome = input("Novo nome (enter para manter): ") or None
            cargo = input("Novo cargo (enter para manter): ") or None
            salario = input("Novo salário (enter para manter): ")
            salario = float(salario) if salario else None
            atualizar_funcionario(id, nome, cargo, salario)
        elif opcao == "5":
            id = int(input("ID: "))
            deletar_funcionario(id)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
