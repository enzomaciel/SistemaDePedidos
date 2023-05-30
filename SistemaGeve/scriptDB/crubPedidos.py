import sqlite3 as conector

caminhodb = "db\\geve.db"

def cadastrarPedido(name_cliente,prazo,emissao,subtotal):
        conexao = conector.connect(caminhodb)
        cursor = conexao.cursor()
        comando = '''INSERT INTO pedido (name_cliente,prazo,emissao,subtotal)
                      VALUES (:name_cliente,:prazo,:emissao,:subtotal);'''
        cursor.execute(comando, {
            "name_cliente":name_cliente,
            "prazo":prazo,
            "emissao":emissao,
            "subtotal":subtotal
        })
        conexao.commit()
        cursor.close()
        conexao.close()

def selecionarUltimoPedido():
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''SELECT id_pedido FROM pedido ORDER BY id_pedido DESC LIMIT 1''')
    conexao.commit()
    ultimo_valor = cursor.fetchall()[0]
    cursor.close()
    conexao.close()
    return ultimo_valor
def ver_num_pedidos(i):
    conexao = conector.connect(caminhodb)
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM pedido''')
    conexao.commit()
    linha = cursor.fetchall()[i]
    cursor.close()
    conexao.close()
    return linha
        