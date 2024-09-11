from utilitarios import(
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total
)

# Categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_viagens = cadastrar_categoria('Viagens')
categoria_lazer = cadastrar_categoria('Lazer')

# Transações
t1 = cadastrar_transacao(
    descricao='Salário Jan/2024',
    valor=1400,
    categoria=categoria_receitas
)

t2 = cadastrar_transacao(
    descricao='Mesada',
    valor=200,
    categoria=categoria_receitas
)

t3 = cadastrar_transacao(
    descricao='Ingresso Show',
    valor=-150,
    categoria=categoria_lazer
)

t4 = cadastrar_transacao(
    descricao='Conta de Luz',
    valor=-100,
    categoria=categoria_contas
)

t5 = cadastrar_transacao(
    descricao='Gramado',
    valor=-400,
    categoria=categoria_viagens
)

total = saldo_total()
t1.exibir()
t2.exibir()
t3.exibir()
t4.exibir()
t5.exibir()
print()
print('Saldo Total = ', total)