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
                                    "email": usuario.email}
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
    
@app.route("/produtos", methods=['GET','POST'])
def inserir_produtos():
    if request.method == 'GET':
        return render_template("venda.html")
    else:
        imagem_url = request.form["img"]
        nome_produto = request.form["nome"]
        preco_produto = request.form["preco"]
        categoria = request.form["categoria"]

        usuario = Usuario()

        if usuario.inserir_produto(imagem_url, nome_produto, preco_produto, categoria):
            return redirect("/")
        else: 
            return "ERRO AO INSERIR PRODUTO"
        
@app.route("/categoria", ['GET', 'POST'])
def categoria():
    if request.method == 'GET':
        return render_template("categoria.html")
    else:
    
        filtrado = request.name['filtro']
        sistema = Sistema()

        if sistema.filtro(filtrado):

@app.route("/teste/<categoria>")
def catgoria(categoria):
    
    return render_template("categoria.html")


   



app.run(debug=True)

        