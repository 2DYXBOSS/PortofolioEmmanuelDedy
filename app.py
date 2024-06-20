from flask import Flask,send_file, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import os
import datetime

data = datetime.date.today()
dataheure = datetime.datetime.now()
formatted_time = dataheure.strftime('%H')
formatted = dataheure.strftime('%M')
print(data)
print(dataheure)
print(formatted_time)
print(formatted)
print(dataheure)

print(2)

from flask import Flask, request, render_template, redirect, url_for,send_file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# import pywhatkit

# Configurations pour le serveur SMTP


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'BONJOUR'


app.config['SECRET_KEY'] = 'sdfgghjklhkj'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '0streamblay@gmail.com'
app.config['MAIL_PASSWORD'] = 'vgux fpjq qyqr nxem'
app.config['MAIL_DEFAULT_SENDER'] = '0streamblay@gmail.com'



SMTP_SERVER = 'smtp.googlemail.com'  # Remplacez par l'adresse de votre serveur SMTP
SMTP_PORT = 587  # Port SMTP (généralement 587 pour TLS)
SMTP_USERNAME = 'pythonanywhere225@gmail.com'
SMTP_PASSWORD = 'tdqn cklm uvjd aonn'
# Clé secrète pour sécuriser l'application
app.secret_key = os.urandom(24)
mail = Mail(app)
# fin
# ghhh
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


db = SQLAlchemy(app)



debug = True



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    # Chemin vers le fichier que vous voulez permettre de télécharger
    filepath = 'static/images/cv.pdf'  # Remplacez par votre chemin de fichier réel

    # Vous pouvez également gérer le nom de fichier de sortie ici
    filename = 'cv.pdf'

    return send_file(filepath, as_attachment=True, attachment_filename=filename)

@app.route('/emmanuelDedy')
def emmanuelDedy():
    return send_file("static/images/cv.pdf")




@app.route('/message', methods=['POST'])
def message():
    
    # sujet = request.form['sujet']
    # tre = Connecter.query.get(1)
    # if 'utilisateur_id' in session:
    #     user = Profil.query.get(session['utilisateur_id'])
    # else:
    #     return redirect('/pre')
    destinataire = "2dyxboss225@gmail.com"
    nom = request.form.get("nom")
    email = request.form.get("email")
    sujet = f"Message de {nom} via son mail {email} "
    contenu = request.form.get("contenu")

    msg = Message(sujet, recipients=[destinataire])
    msg.body = contenu
    
    try:

        mail.send(msg)
        flash("Commande validee avec succes", 'success')

        
    except Exception as e:
        flash("Une erreur s'est produite lors de l'envoi de l'e-mail", 'danger')

    return redirect("/#Contact")
    # return render_template("payement.html")
# FIN COMMANDER

if __name__ == '__main__' :
    app.run(debug=True,port=5005)

