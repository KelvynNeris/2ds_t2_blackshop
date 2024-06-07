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

    
@app.route("/categoria/<categoria>")
def catgoria(categoria):

    sistema = Sistema()
    lista_filtro = sistema.filtro(categoria)
    return render_template("produtos-categoria.html",  lista_filtro = lista_filtro)

    
@app.route("/inserir_carrinho", methods=['GET', 'POST'])
def inserir_carrinho():
    if request.method == 'GET':
        return render_template("carrinho.html")
    else:

        btn_carrinho = request.form['btn-carrinho']
        cpf_cliente = session['usuario.logado']['cpf']

        sistema=Sistema()
        if sistema.inserir_carrinho(btn_carrinho, cpf_cliente):
            return render_template("carrinho.html")
        else:
            return "ERRO AO INSERIR PRODUTO AO CARRINHO"
@app.route("/carrinho")
def carrinho():

    sistema = Sistema()
    lista_carrinho = sistema.filtro(id)
    return render_template("carrinho.html",  lista_carrinho = lista_carrinho)

    
@app.route("/compra", methods=['GET', 'POST'])
def comprar():
    if request.method == 'GET':
        return render_template("produto-unico.html")
    else:
        btn_produto = request.form['btn-produto']
        sistema=Sistema()
        id_prd = sistema.exibir_carrinho(btn_produto)
        return render_template("produto-unico.html", id_prd = id_prd)




app.run(debug=True)

        