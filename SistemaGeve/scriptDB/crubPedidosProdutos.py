import sqlite3 as conector
caminhodb = "db\\geve.db"

def cadastrarProdutoPedido(num_pedido,produto,emissao,quantidade,valor,total):
        conexao = conector.connect(caminhodb)
        cursor = conexao.cursor()
        comando = '''INSERT INTO produtopedido (num_pedido,produto,emissao,quantidade,valor,total)
                      VALUES (:num_pedido,:produto,:emissao,:quantidade,:valor,:total);'''
        cursor.execute(comando, {
            "num_pedido":num_pedido,
            "produto":produto,
            "emissao":emissao,
            "quantidade":quantidade,
            "valor":valor,
            "total":total
        })
        conexao.commit()
        cursor.close()
        conexao.close()
        
def ver_num_prodPedido(i,num_pedido):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM produtopedido  WHERE num_pedido = ?''',num_pedido)
    conexao.commit()
    print(i)
    print(num_pedido)
    linha = cursor.fetchall()
    cursor.close()
    conexao.close()
    return linha

def selecionarUltimoProduto():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''SELECT id FROM produtopedido ORDER BY id DESC LIMIT 1''')
    conexao.commit()
    ultimo_valor = cursor.fetchall()[0]
    cursor.close()
    conexao.close()
    return ultimo_valor

