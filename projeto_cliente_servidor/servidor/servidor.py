from flask import Flask, jsonify, request

app = Flask(__name__)

funcionarios = [
    {"id": 1, "nome": "Ana Silva", "cargo": "Desenvolvedora", "salario": 5000},
    {"id": 2, "nome": "Carlos Souza", "cargo": "Analista de Sistemas", "salario": 4500}
]

@app.route("/")
def home():
    return jsonify({"mensagem": "API de Cadastro de Funcionários está no ar!"})

@app.route("/funcionarios", methods=["GET"])
def listar_funcionarios():
    return jsonify(funcionarios)

@app.route("/funcionarios/<int:id>", methods=["GET"])
def buscar_funcionario(id):
    funcionario = next((f for f in funcionarios if f["id"] == id), None)
    if funcionario:
        return jsonify(funcionario)
    return jsonify({"erro": "Funcionário não encontrado"}), 404

@app.route("/funcionarios", methods=["POST"])
def adicionar_funcionario():
    novo = request.get_json()
    novo["id"] = len(funcionarios) + 1
    funcionarios.append(novo)
    return jsonify(novo), 201

@app.route("/funcionarios/<int:id>", methods=["PUT"])
def atualizar_funcionario(id):
    funcionario = next((f for f in funcionarios if f["id"] == id), None)
    if funcionario:
        dados = request.get_json()
        funcionario.update(dados)
        return jsonify(funcionario)
    return jsonify({"erro": "Funcionário não encontrado"}), 404

@app.route("/funcionarios/<int:id>", methods=["DELETE"])
def deletar_funcionario(id):
    global funcionarios
    funcionarios = [f for f in funcionarios if f["id"] != id]
    return jsonify({"mensagem": "Funcionário removido com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
