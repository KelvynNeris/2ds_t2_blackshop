from conexao import Conexao


class Sistema:
    def filtro(filtro):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT * from tb_produtos nome_produto"
        