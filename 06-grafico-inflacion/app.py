# app.py
from flask import Flask, render_template, send_file, url_for
import matplotlib.pyplot as plt
import pandas as pd
import io

app = Flask(__name__)

# Datos ficticios de la inflación media en España, Francia, Alemania e Italia en los últimos 20 años
data = {
    'Año': list(range(2003, 2023)),
    'Inflación_media_ES': [3.0, 2.8, 2.9, 3.1, 2.6, 1.8, 1.0, 0.9, 2.3, 2.1, 1.5, 1.3, 0.6, 1.2, 1.5, 1.9, 2.2, 2.0,
                           1.7, 1.8],
    'Inflación_media_FR': [2.1, 2.2, 2.0, 1.9, 1.7, 1.5, 1.4, 1.3, 1.8, 1.6, 1.0, 1.1, 0.7, 1.4, 1.3, 1.7, 2.0, 1.8,
                           1.6, 1.4],
    'Inflación_media_DE': [1.6, 1.7, 1.8, 1.9, 1.5, 1.3, 0.8, 0.7, 1.5, 1.3, 0.9, 0.8, 0.5, 1.1, 1.0, 1.4, 1.7, 1.5,
                           1.3, 1.2],
    'Inflación_media_IT': [2.5, 2.4, 2.6, 2.8, 2.2, 2.0, 1.5, 1.4, 2.0, 1.8, 1.2, 1.0, 0.8, 1.6, 1.7, 2.1, 2.3, 2.1,
                           1.9, 1.7]
}

df = pd.DataFrame(data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inflacion.png')
def inflacion():
    plt.figure(figsize=(12, 6))
    plt.plot(df['Año'], df['Inflación_media_ES'], marker='o', linestyle='-', linewidth=2, label='España')
    plt.plot(df['Año'], df['Inflación_media_FR'], marker='o', linestyle='-', linewidth=2, label='Francia')
    plt.plot(df['Año'], df['Inflación_media_DE'], marker='o', linestyle='-', linewidth=2, label='Alemania')
    plt.plot(df['Año'], df['Inflación_media_IT'], marker='o', linestyle='-', linewidth=2, label='Italia')

    plt.xlabel('Año')
    plt.ylabel('Inflación media (%)')
    plt.title('Inflación media en España, Francia, Alemania e Italia (2003-2022)')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
