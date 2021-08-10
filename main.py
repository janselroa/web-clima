#import packaches

from flask import Flask,render_template,request,redirect,url_for, flash
from flask_mail import Mail,Message
import os
import requests
import functions


app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=os.environ['SECRET_KEY']
)
#configurando Flask Email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['EMAIL']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['EMAIL']
mail = Mail(app)


@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	elif request.method == 'POST':
		ciudad = functions.limpiar_str(request.form['ciudad'])
		clima = functions.clima(ciudad)
		return render_template('clima.html',clima=clima)
	else:
		return "Error"

@app.route('/contacto',methods=['GET','POST'])
def contacto():
	if request.method == 'GET':
		return render_template('contacto.html')

	elif request.method == 'POST':
		mensaje = [request.form['asunto'],request.form['name'],request.form['mensaje']]
		mensajes = list(map(functions.limpiar_str,mensaje))
		msg = Message(recipients=[os.environ['EMAIL']],
			body=mensaje[2],
			subject=mensaje[0]
		)
		mail.send(msg)
		flash('Gracias email enviado correctamente')
		return redirect(url_for('contacto'))
	else:
		return "Error"

