import sqlite3 as conector

caminhodb = "db\\geve.db"

def cadastrarUsuario(nome,username,password,email,data,cpf):
        conexao = conector.connect(caminhodb)
        cursor = conexao.cursor()
        comando = '''INSERT INTO usuario (name,username,password,email,aniversario,cpf)
                      VALUES (:name,:username,:password,:email,:aniversario,:cpf);'''
        cursor.execute(comando, {
            "name":nome,
            "username":username,
            "password":password,
            "email":email,
            "aniversario":data,
            "cpf":cpf
        })
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Usuario cadastrado")
def verificarUsuario(username,password):
        conexao = conector.connect(caminhodb)
        cursor = conexao.cursor()
        cursor.execute('''SELECT username,password FROM usuario''')
        conexao.commit()
        for linha in cursor.fetchall():
            aux1 = linha[0]
            aux2 = linha[1]
            if aux1 == username:
                if aux2 == password: 
                    cursor.close()
                    conexao.close()
                    return 1
        cursor.close()
        conexao.close()
        return 0
        