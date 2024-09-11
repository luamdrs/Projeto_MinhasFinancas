from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []


def cadastrar_categoria(nome):              # Chama a função passando 'nome' como parâmetro
    nova_categoria = Categoria(nome=nome)   # Instancia/Inicializa a categoria

    LISTA_CATEGORIAS.append(nova_categoria) # Cadastra na lista

    return nova_categoria                   # Retorna o valor de nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(
        descricao=descricao,
        valor=valor,
        categoria=categoria
    )
    
    LISTA_TRANSACOES.append(nova_transacao)

    return nova_transacao


def saldo_total():
    total = 0

    for t in LISTA_TRANSACOES:
        total += t.valor

    return total
