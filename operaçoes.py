from flask import Flask, request, jsonify
 
app = Flask(__name__)
# PARTE 1 - CALCULADORA
 
@app.route('/calculadora', methods=['POST'])
def calculadora():
    data = request.json
 
    # Verifica se o corpo da requisição foi enviado
    if not data:
        return jsonify(erro="Corpo da requisição ausente"), 400
 
    a        = data.get('a')
    b        = data.get('b')
    operacao = data.get('operacao')
 
    # Verifica se os números foram enviados e são válidos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify(erro="Os campos 'a' e 'b' devem ser números"), 400
 
    if operacao == 'soma':
        return jsonify(operacao=operacao, resultado=a + b), 200
 
    elif operacao == 'subtracao':
        return jsonify(operacao=operacao, resultado=a - b), 200
 
    elif operacao == 'multiplicacao':
        return jsonify(operacao=operacao, resultado=a * b), 200
 
    elif operacao == 'divisao':
        if b == 0:
            return jsonify(erro="Divisão por zero não é permitida"), 400
        return jsonify(operacao=operacao, resultado=a / b), 200
 
    return jsonify(erro=f"Operação '{operacao}' inválida. Use: soma, subtracao, multiplicacao, divisao"), 400

# PARTE 2 - USUÁRIOS
 
usuarios = []
 
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
 
    if not data:
        return jsonify(erro="Corpo da requisição ausente"), 400
 
    nome  = data.get('nome')
    idade = data.get('idade')
 
    # Valida tipos: nome deve ser string, idade deve ser inteiro positivo
    if not isinstance(nome, str) or not nome.strip():
        return jsonify(erro="Campo 'nome' inválido: deve ser uma string não vazia"), 400
 
    if not isinstance(idade, int) or idade < 0:
        return jsonify(erro="Campo 'idade' inválido: deve ser um inteiro positivo"), 400
 
    usuario = {"nome": nome.strip(), "idade": idade}
    usuarios.append(usuario)
    return jsonify(msg="Usuário criado com sucesso", usuario=usuario, total=len(usuarios)), 201
 
 
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios=usuarios, total=len(usuarios)), 200
 
 
@app.route('/usuarios', methods=['DELETE'])
def deletar_usuario():
    # DELETE não é suportado nesta rota — retorna 405 Method Not Allowed
    return jsonify(erro="Método DELETE não é permitido nesta rota"), 405
 
# PARTE 3 - PRODUTOS
 
produtos = [
    {"nome": "Camiseta", "valor": 50,   "categoria": "vestuario"},
    {"nome": "Calça",    "valor": 100,  "categoria": "vestuario"},
    {"nome": "Notebook", "valor": 3000, "categoria": "eletronico"},
]
 
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    categoria = request.args.get('categoria')  # ex: /produtos?categoria=vestuario
 
    if categoria:
        filtrados = [p for p in produtos if p['categoria'] == categoria]
        if not filtrados:
            return jsonify(erro=f"Nenhum produto encontrado para a categoria '{categoria}'"), 404
        return jsonify(categoria=categoria, produtos=filtrados, total=len(filtrados)), 200
 
    return jsonify(produtos=produtos, total=len(produtos)), 200
 
# PARTE 4 - STATUS

@app.route('/status', methods=['GET'])
def status():
    return jsonify(status="ok", servico="API de Testes", versao="1.0"), 200

if __name__ == '__main__':            
    app.run(debug=True)


produtos = []
