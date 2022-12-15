from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os
from config import config
from database import database
from flask_login import LoginManager, login_user, logout_user, login_required 

# -----------MODELOS-------------

from models.modelsUser import ModelUser

#_---------ENTITIES---------------

from models.entities.User import User

#------------APP Flask-------------------------------------------------------------

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

app=Flask(__name__)

db=MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
	return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method=='POST':

		user = User(0, request.form['username'], request.form['password'])
		logged_user=ModelUser.login(db, user)

		if logged_user != None:
			if logged_user.password:
				login_user(logged_user)
				return redirect(url_for('inicio'))
			else:
				flash("Contraseña no valida")
				return render_template('auth/login.html')
		else:
			flash("Usuario no encontrado...")
			return render_template('auth/login.html')
	else:
		return render_template('auth/login.html')

@app.route('/logout')
def logout():
	return redirect(url_for('login'))

@app.route('/inicio')
def inicio():
	return (render_template('layout.html'))


#--------FORMULARIO---------------------------------

@app.route('/form')
def form():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM objetos")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('formulario.html', data=insertObject)

#-------------GUARDAR DATOS----------------

@app.route('/user', methods=['POST'])
def addUser():
	nombre = request.form['nombre']
	cantidad = request.form['cantidad']
	marca = request.form['marca']

	if nombre and cantidad and marca:
		cursor = database.cursor()
		sql = "INSERT INTO objetos (nombre, cantidad, marca) VALUES (%s, %s, %s)"
		data = (nombre, cantidad, marca)
		cursor.execute(sql, data)
		database.commit()
	return redirect(url_for('form'))

@app.route('/delete/<string:id>')
def delete(id):
	cursor = database.cursor()
	sql = "DELETE FROM objetos WHERE id=%s"
	data = (id,)
	cursor.execute(sql, data)
	database.commit()
	return redirect(url_for('form'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
	nombre = request.form['nombre']
	cantidad = request.form['cantidad']
	marca = request.form['marca']

	if nombre and cantidad and marca:
		cursor = database.cursor()
		sql = "UPDATE objetos SET nombre = %s, cantidad = %s, marca = %s WHERE id = %s"
		data = (nombre, cantidad, marca, id)
		cursor.execute(sql, data)
		database.commit()
	return redirect(url_for('form'))

#--------#FORMULARIO SALA 1-----------------------------------------------------



@app.route('/sala')
def sala():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM sala2")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('formulariosala2.html', data=insertObject)

#-------------GUARDAR DATOS----------------

@app.route('/user2', methods=['POST'])
def addUser1():
	nombre = request.form['nombre']
	cantidad = request.form['cantidad']
	marca = request.form['marca']

	if nombre and cantidad and marca:
		cursor = database.cursor()
		sql = "INSERT INTO sala2 (nombre, cantidad, marca) VALUES (%s, %s, %s)"
		data = (nombre, cantidad, marca)
		cursor.execute(sql, data)
		database.commit()
	return redirect(url_for('sala'))

@app.route('/delete1/<string:id>')
def delete1(id):
	cursor = database.cursor()
	sql = "DELETE FROM sala2 WHERE id=%s"
	data = (id,)
	cursor.execute(sql, data)
	database.commit()
	return redirect(url_for('sala'))

@app.route('/edit1/<string:id>', methods=['POST'])
def edit1(id):
	nombre = request.form['nombre']
	cantidad = request.form['cantidad']
	marca = request.form['marca']

	if nombre and cantidad and marca:
		cursor = database.cursor()
		sql = "UPDATE sala2 SET nombre = %s, cantidad = %s, marca = %s WHERE id = %s"
		data = (nombre, cantidad, marca, id)
		cursor.execute(sql, data)
		database.commit()
	return redirect(url_for('sala'))	

#--------FORMULARIO3---------------------------------

@app.route('/sala3')
def sala3():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM formulario3")
    myresult = cursor.fetchall()

    #Convertir los datos a diccionario

    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('formulario3.html', data=insertObject)

#-------------GUARDAR DATOS----------------

@app.route('/user3', methods=['POST'])
def addUser3():
	nombre = request.form['nombre']
	cantidad = request.form['cantidad']
	marca = request.form['marca']

	if nombre and cantidad and marca:
		cursor = database.cursor()
		sql = "INSERT INTO formulario3 (nombre, cantidad, marca) VALUES (%s, %s, %s)"
		data = (nombre, cantidad, marca)
		cursor.execute(sql, data)
		database.commit()
	return redirect(url_for('sala3'))

@app.route('/delete2/<string:id>')
def delete2(id):
	cursor = database.cursor()
	sql = "DELETE FROM formulario3 WHERE id=%s"
	data = (id,)
	cursor.execute(sql, data)
	database.commit()
	return redirect(url_for('sala3'))

@app.route('/edit2/<string:id>', methods=['POST'])
def edit2(id):
	nombre = request.form['nombre']
	cantidad = request.form['cantidad']
	marca = request.form['marca']

	if nombre and cantidad and marca:
		cursor = database.cursor()
		sql = "UPDATE formulario3 SET nombre = %s, cantidad = %s, marca = %s WHERE id = %s"
		data = (nombre, cantidad, marca, id)
		cursor.execute(sql, data)
		database.commit()
	return redirect(url_for('sala3'))


#--------------REGISTRO---------------------
@app.route('/regis')
def registrar():
	return redirect(url_for('regist'))

@app.route('/regist')
def registro():
	return render_template('registro.html')


if __name__=='__main__':
	app.config.from_object(config['development'])
	app.run(port=5000)