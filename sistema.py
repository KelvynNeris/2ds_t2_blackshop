from conexao import Conexao


class Sistema:
    def filtro(filtro):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT * from tb_produtos where categoria = '{filtro}'"

        mycursor.execute(sql)
        mydb.commit()
        mydb.close()
        return True
    

    def exibir_produtos(self):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT * from tb_produtos"
        mycursor.execute(sql)
        
        resultado = mycursor.fetchall()
       
        lista_categorias = []

        for categoria in resultado:
            lista_categorias.append({
                'nome_produto': categoria[1],
                'preco': categoria[2],
                'imagem_produto': categoria[3]
            })
        mydb.close()
        if lista_categorias:
            return lista_categorias
        else:
            return []
