from conexao import Conexao
from hashlib import sha256

class Usuario:
    def __init__(self):
        self.tel = None
        self.nome = None
        self.senha = None
        self.endereco = None
        self.cpf = None
        self.email = None
        self.logado = False
    def cadastrar(self, telefone, nome, senha, cpf, endereco, email):
        senha = sha256(senha.encode()).hexdigest()
        try:
            mydb = Conexao.conectar()


            mycursor = mydb.cursor()

            
            sql =(f"INSERT INTO tb_cliente VALUES('{nome}', {cpf}, '{telefone}', '{endereco}, '{email}')")
            
            mycursor.execute(sql)
            
            self.tel = telefone
            self.nome = nome
            self.senha = senha
            self.endereco = endereco
            self.cpf = cpf
            self.email = email
            self.logado = True


            mydb.commit()

            print(mycursor.rowcount, "registro inserido")

            mycursor.execute("SELECT email, nome FROM tb_cliente")

            ver = mycursor.fetchall()

            print(ver)

            mydb.close()
            return True
        except:
            return False