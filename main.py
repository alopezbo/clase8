#Dependencias
import os
import sqlite3
from flask import Flask, render_template, session, escape
from flask import render_template, request, redirect, url_for, g
from flask_sqlachemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

#Configuracion general del software
app=Flask(__name__)
app.config['DEBUG']=True

#Configuracion del email
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='masterlist.supplier@gmail.com',
    MAIL_PASSWORD='Celeste:801020363'
)
mail=Mail(app)

#Base de datos login de user
dbdir="sqlite:///"+os.path.abspath(os.getcwd())+"/database.db"
DATABASE="data.db"
app.config["SQLALCHEMY_DATABASE_URI"]=dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(80), nullable=False)
    
    
#Gestion de la base de datos proveedores
def get_db():
    db=getattr(g,'_database',None)
    if db is None:
        db=g_database=sqlite3,connect(DATABASE)
        db.row_factory=sqlite3.Row
    return db

def query_db(query,args=(),one=False):
    cur=get_db().execute(query,args)
    rv=cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def change_db(query,args=()):
    cur=get_db().execute(query,args)
    get_db().commit()
    cur.close()
    
@app.teardown_appcontext
def close_connection(exception):
    db=getattr(g,'_database',None)
    if db is not None:
        db.close()


@app.route('/crearempresa',methods=['GET','POST'])  
def crearempresa():
    if request.method=="GET" #GET solicita el formulario para ingresar los datos.
        return render_template("crearempresa.html",contact=None)
    
    if request.method=="POST": #va a la DB para agregar los elementos indicados
        contact=request.form.to_dict()
        values=[contact['entidad'],contact['tel'],contact['email'],contact['representante'],contact['usuario'],contact['emailusuario']]
            change_db("INSERT INTO contact (entidad,tel,email,representante,usuario,emailusuario) VALUES(?,?,?,?,?,?,?,?,?,?,?)",values)
            return redirec(url_for("empresa"))  #tiene que haber igual cantidad de signos de pregunta como elementos que se solicitan
        
        if __name__=="__main__":
            db.create_all()
            app.run(debug=True)