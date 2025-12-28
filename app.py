from flask import Flask, render_template, request, redirect, url_for
import requests
from db_connection import get_db_connection

app = Flask(__name__)

# CONFIGURACIÓN BANXICO 
TOKEN_BANXICO = "aqui tu token" 
SERIE_DOLAR = "SF43718"

@app.route('/')
def index():
    # Conectarse a SQL
    conn = get_db_connection()
    articulos = []
    
    if conn:
        cursor = conn.cursor()
        # Traemos los datos para la tabla principal
        cursor.execute("SELECT IdArticulo, DescripcionCorta, Costo, Precio, PrecioDolares FROM Articulos")
        # lista manejable
        columns = [column[0] for column in cursor.description]
        articulos = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        
    return render_template('index.html', articulos=articulos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        #  Recibir datos del formulario HTML
        desc_corta = request.form['desc_corta']
        desc_larga = request.form['desc_larga']
        unidad = request.form['unidad']
        costo = float(request.form['costo'])
        precio = float(request.form['precio'])
        
        #  Consultar Banxico 
        
        tipo_cambio = 20.00 # Valor por defecto por si falla la API
        try:
            url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{SERIE_DOLAR}/datos/oportuno"
            headers = {"Bmx-Token": TOKEN_BANXICO}
            response = requests.get(url, headers=headers)
            data = response.json()
            # Navegar el JSON de Banxico para sacar el dato
            tipo_cambio = float(data['bmx']['series'][0]['datos'][0]['dato'])
        except Exception as e:
            print(f"Error consultando Banxico: {e}")

        # Calcular precio 
        precio_dolares = precio / tipo_cambio
        
        #  Guardar en SQL 
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Articulos 
            (DescripcionCorta, DescripcionLarga, UnidadMedida, Costo, Precio, TipoCambio, PrecioDolares)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (desc_corta, desc_larga, unidad, costo, precio, tipo_cambio, precio_dolares))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)