from crypt import methods
from __init__ import app
from flask import render_template,flash,redirect,session,request
from models import revista

@app.route('/show/revista/<int:revista_id>')
def show_revista(revista_id):
    data = {
        "id": revista_id
    }
    return render_template('show_revista.html',revista_info = revista.Revista.show_revista_by_id(data)[0],usuarios_suscritos = revista.Revista.usuarios_suscritos(data))

@app.route('/agregar_revista')
def agregar_revista():
    return render_template('agregar_revista.html')

@app.route('/agregar_revista_process',methods=['POST'])
def agregar_revista_process():
    if not revista.Revista.validacion(request.form):
        return redirect('/agregar_revista')
    data = {
        "nombre": request.form['nombre'],
        "descripcion": request.form['descripcion']
    }
    revista.Revista.save(data)
    flash('Revista agregada exitosamente','success')
    return redirect('/inicio_sesion')

@app.route('/agregar/suscripcion/<int:revista_id>')
def agregar_suscripcion(revista_id):
    data = {
        "usuario_id": session['user_id'],
        "revista_id": revista_id
    }
    revista.Revista.agregar_suscripcion(data)
    flash('Suscripcion agregada','success')
    return redirect('/inicio_sesion')