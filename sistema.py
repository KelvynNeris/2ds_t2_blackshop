from conexao import Conexao


class Sistema:
    def __init__(self):
        self.cpf = None
        self.id_produto = None

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
                'descricao': filtro[5],
                'id_produto': filtro[0]       
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
                'descricao': categoria[5],
                'id_produto': categoria[0] 
            })
        mydb.close()
        if lista_categorias:
            return lista_categorias
        else:
            return []
    
   
    def inserir_carrinho(self, cpf, id_produto):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"INSERT INTO tb_carrinho (cpf_cliente, id_produto) VALUES ('{cpf}', '{id_produto}')"
        
        mycursor.commit()
        mydb.close()
    
    def exibir_carrinho(self, id):
        mydb =  Conexao.conectar()
        mycursor = mydb.cursor()

        sql = f"SELECT * from tb_produtos where categoria = '{id}'"

        mycursor.execute(sql)
        resultado = mycursor.fetchall()
       
        lista_carrinho = []

        for id_produto in resultado:
            lista_carrinho.append({
                'nome_produto': id_produto[1],
                'preco': id_produto[2],
                'imagem_produto': id_produto[3],
                'descricao': id_produto[5]            
        })

        mycursor.execute(sql)
        mydb.close()
    def exibir_produto1(self, id):
            mydb =  Conexao.conectar()
            mycursor = mydb.cursor()

            sql = f"SELECT * FROM tb_produtos INNER JOIN tb_produtos WHERE id_produto = '{id}'"

            mycursor.execute(sql)
            resultado = mycursor.fetchall()
        
            lista_produto1 = []

            for id_produto in resultado:
                lista_produto1.append({
                    'nome_produto': id_produto[1],
                    'preco': id_produto[2],
                    'imagem_produto': id_produto[3],
                    'descricao': id_produto[5]            
            })

            mycursor.execute(sql)
            mydb.close()