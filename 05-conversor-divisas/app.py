from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# Ruta para la página principal
@app.route('/', methods=['GET', 'POST'])
def index():
    # Si se envía el formulario
    if request.method == 'POST':
        # Obtener los datos del formulario
        source_currency = request.form['source_currency']
        target_currency = request.form['target_currency']
        amount = float(request.form['amount'])

        # Hacer la solicitud HTTP a la API de APILayer.com
        url = f'https://api.apilayer.com/exchangerates_data/convert?from={source_currency}&to={target_currency}&amount={amount}'
        headers = {'apikey': 'TU-CLAVE-API-AQUI'}
        response = requests.get(url, headers=headers)

        # Obtener el resultado de la conversión
        result = response.json()['result']

        # Devolver los datos a la plantilla index.html
        return render_template('index.html', result=result)

    # Si se carga la página por primera vez
    else:
        # Monedas disponibles
        currencies = ['EUR', 'USD', 'CNY', 'JPY']

        # Renderizar la plantilla index.html con las monedas disponibles
        return render_template('index.html', currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)
