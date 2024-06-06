from conexao import Conexao


class Sistema:
    def filtro(self, filtro):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT * from tb_produtos where categoria = '{filtro}'"

        mycursor.execute(sql)
        resultado = mycursor.fetchall()
       
        lista_filtro = []

        for filtro in resultado:
            lista_filtro.append({
                'nome_produto': filtro[1],
                'preco': filtro[2],
                'imagem_produto': filtro[3],
                'descricao': filtro[5]            
        })
        mydb.close()
        if lista_filtro:
            return lista_filtro
        else:
            return []
        
    

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
                'imagem_produto': categoria[3],
                'categoria': categoria[4],
                'descricao': categoria[5]
            })
        mydb.close()
        if lista_categorias:
            return lista_categorias
        else:
            return []
    

    def inserir_carrinho(self):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"select id_produto from tb_produto"
        
        resultado = mycursor.fetchall()
        lista_categorias = []

        lista_categorias.append(resultado)

        

        mycursor.execute(sql)

        mydb.close()
