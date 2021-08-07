from flask import Flask,render_template,request
import requests
import functions

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	elif request.method == 'POST':
		ciudad = functions.limpiar_str(request.form['ciudad'])
		clima = functions.clima(ciudad)
		return render_template('clima.html',clima=clima)
	else:
		return "error"

@app.route('/contacto',methods=['GET','POST'])
def contacto():
	if request.method == 'GET':
		return render_template('contacto.html')

	elif request.method == 'POST':
		mensaje = [request.form['asunto'],request.form['name'],request.form['mensaje']]
		mensajes = list(filter(functions.limpiar_str,mensaje))
		functions.enviar_email(mensajes)
		return render_template('contacto.html')
	else:
		return "error"

	
app.run()
