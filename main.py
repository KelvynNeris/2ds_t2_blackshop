from flask import Flask, render_template, session, redirect, request
from usuario import Usuario
import sqlite3




app = Flask(__name__)
conexao = sqlite3.connect("shopbck.sqlite")
cursor = conexao.cursor()
cursor.execute()
conexao.commit()
conexao.close()

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
        cpf = request.form["cpf"]

        usuario = Usuario()

        if usuario.cadastrar(nome, cpf, telefone, endereco, email, cpf):
            return render_template("logar.html"), 200
        else:
            return ("/cadastro"), 400
     
       
    
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
            return redirect("/index")
            
        else:
            session.clear()
            return redirect("/logar")
        