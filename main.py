from flask import Flask, render_template, request, redirect, session
from usuario import Usuario
from sistema import Sistema





app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

@app.route("/")
def index():
    return render_template("index.html")
    

# Define cadastro route 
@app.route("/cadastro", methods = ["GET", "POST"])
def cadastro():
    if request.method == 'GET':
        return render_template("cadastro.html")
    else:
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = Usuario()

        if usuario.cadastrar(nome, telefone, cpf, endereco, email,senha):
            return redirect("/")
        else:
            return redirect("/cadastro")
     
           
@app.route('/logar', methods = ['GET','POST'])
def logar():
    if request.method =='GET':
        return render_template('login.html')
    else:
        senha = request.form['senha']
        email = request.form['email']
        usuario = Usuario()
        usuario.logar(email, senha)
        if  usuario.logado == True:
            session['usuario_logado'] = {"nome": usuario.nome,
                                    "email": usuario.email,
                                    "cpf": usuario.cpf}
            return redirect("/")
            
        else:
            session.clear()
            return redirect("/logar")
    
    #  ------------------------------------------ VERIFICAR ---------------------------------------------------------------

""" @app.route("/verificar", methods = ['GET', 'POST'])
def verificar_vendedor():
    mensagem_erro = ""
    senhaVendedor =  'EuPossoInserirProdutos'
    if senhaVendedor == 'EuPossoInserirProdutos':
        session
        return render_template("venda.html", mensagem_erro = mensagem_erro)
    else:
        mensagem_erro = "você não tem permissão para acessar esta página"
        session.clear()
        return redirect("/verificar", mensagem_erro = mensagem_erro) """
    
    
    
    # -------------------------------------------------- PRODUTOS ---------------------------------------------------------
    
    
@app.route("/inserir_produtos", methods=['GET','POST'])
def inserir_produtos():
    if request.method == 'GET':
        return render_template("venda.html")
    else:
        imagem_url = request.form["img"]
        nome_produto = request.form["nome"]
        preco_produto = request.form["preco"]
        categoria = request.form["categoria"]
        descricao = request.form["descricao"]

        usuario = Usuario()

        if usuario.inserir_produto(imagem_url, nome_produto, preco_produto, categoria, descricao):
            return redirect("/")
        else: 
            return "ERRO AO INSERIR PRODUTO"
        
@app.route("/produtos")
def compras():
   
    # filtro = request.args.get['text']

    # if filtro == None   :

        sistema = Sistema()
        lista_categoria = sistema.exibir_produtos()
        return   render_template("produtos.html", lista_categoria = lista_categoria)
    # else:
    #     sistema = Sistema()
    #     lista_filtro = sistema.filtro(filtro)
    #     return render_template("produtos.html",  lista_filtro = lista_filtro)

    
    
    # ---------------------------------------- CATEGORIA --------------------------------------------------------
    
@app.route("/categoria/<categoria>")
def catgoria(categoria):

    sistema = Sistema()
    lista_filtro = sistema.filtro(categoria)
    return render_template("produtos-categoria.html",  lista_filtro = lista_filtro)


#  ----------------------------------------- CARRINHO --------------------------------------------------------


    
@app.route("/inserir_carrinho", methods=['GET', 'POST'])
def inserir_carrinho():
    if request.method == 'GET':
        return render_template("carrinho.html")
    else:
        id_produto = request.form['btn-carrinho']
        cpf_cliente = session.get('usuario_logado')['cpf']

        sistema=Sistema()
        if sistema.inserir_produto_carrinho(id_produto, cpf_cliente):
            return render_template("carrinho.html")
        else:
            return "ERRO AO INSERIR PRODUTO AO CARRINHO"
@app.route("/carrinho")
def carrinho():

    sistema = Sistema()
    lista_carrinho = sistema.filtro(id)
    return render_template("carrinho.html",  lista_carrinho = lista_carrinho)

@app.route("/exibir_carrinho")
def exibir_carrinho():
    if request.methods == 'GET':
        return render_template("carrinho.html")
    else:
        id_produto = request.form['btn-carrinho'] 
        
        sistema = Sistema()
        lista_produtos_c = sistema.exibir_carrinho(id)
        return render_template("carrinho.hmtl", lista_produtos_c = lista_produtos_c)

    
    # ----------------------------- PAGINA DE COMPRA -----------------------------------------------
    
@app.route("/compra", methods=['GET', 'POST'])
def comprar():
    if request.method == 'GET':
        return render_template("produto-unico.html")
    else:
        btn_produto = request.form['btn-produto']
        sistema = Sistema()
        id_prd = sistema.exibir_carrinho(btn_produto)
        return render_template("produto-unico.html", id_prds = id_prd)
    
    
    
    # --------------------------- COMENTARIO ---------------------------------------------
    
@app.route("/inserir_comentario", methods=['GET', 'POST'])
def comentario():
    if request.method == 'GET':
        render_template("produto-unico.html")
    else:
        comentario = request.form['comentario']
        nome_cliente = session.get('usuario_logado')['nome']
        sistema = Sistema()
        if sistema.inserir_comentario(comentario, nome_cliente):
            return render_template("produto-unico.html")
        else: 
            return "ERRO AO INSERIR COMENTARIO"

@app.route("/exibir_comentario", methods=['GET', 'POST'])
def exibir_comentario():
    if request.method == 'GET':
        render_template("produto-unico.html")
    else:
        sistema = Sistema()
        nome_cliente = session.get('usuario_logado')['nome']
        lista_comentario = sistema.lista_comentario(nome_cliente)
        return render_template("produto-unico.html", lista_comentario = lista_comentario)
        
    
    


app.run(debug=True)