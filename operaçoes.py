from http import HTTPStatus
import json

#parte 1
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2 and HTTPStatus == 200

def dividir(num1, num2):
    if num2 <= 0:
        print("Não é possível dividir nenhum número por zero")
        return HTTPStatus == 406
    else:
        return num1 / num2 and HTTPStatus == 200

somar(num1, num2)
subtrair(num1, num2)
multiplicar(num1, num2)
dividir(num1, num2)
# ---------------------------------------
#parte 2
usuarios = {
    'nome': 'pedro', "idade": 20
}

novoUsuario = {'nome': 'lucas', 'idade': 32}
jsonNovoUsuario = json.dumps(novoUsuario)

def criarUsuario(nome, idade):
    usuarios.append(novoUsuario)
    return usuarios

def deleteUsuario():
    del novoUsuario['nome']
    print("Usuario deletado")
    return usuarios

def listarUsuario():
    for usuario in usuarios:
        return usuarios.get(usuario)
# -----------------------------------------
#parte 3
class Produtos:
    def __init__(self, nome, valor, categoria):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria


produtos = []
