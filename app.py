from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_muy_segura_y_larga_1234567890'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pokemon_name = request.form.get('pokemon_name', '').strip().lower()
    if not pokemon_name:
        flash('Por favor, ingresa un nombre de Pokémon.', 'error')
        return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)