from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = 'TU_CLAVE_AQUI'
OPENAI_API_URL = 'https://api.openai.com/v1/engines/text-davinci-003/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    prompt = f"User: {user_message}\nAI:"
    data = {
        'prompt': prompt,
        'max_tokens': 150,
        'n': 1,
        'stop': None,
        'temperature': 0.8,
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    ai_message = response.json()['choices'][0]['text'].strip()

    return jsonify({'message': ai_message})


if __name__ == '__main__':
    app.run(debug=True)
