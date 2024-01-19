from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        valor1 = float(request.form['valor1'])
        valor2 = float(request.form['valor2'])
        valor3 = float(request.form['valor3'])
        resultado = (valor3 * valor2) / valor1
        return render_template('index.html', resultado=resultado)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
