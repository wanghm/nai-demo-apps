from flask import Flask, request, jsonify, render_template
import requests
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

# 環境変数を読み込む
load_dotenv()
endpoint = os.getenv("NAI_ENDPOINT")
api_key = os.getenv("NAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        data = {
            "model": "qwen25-3b",
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "max_tokens": 256,
            "stream": False
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, headers=headers, data=json.dumps(data), verify=False)
        if response.status_code == 200:
            response_data = response.json()
            bot_response = response_data['choices'][0]['message']['content']
            return jsonify({"response": bot_response})
        else:
            return jsonify({"error": response.status_code, "message": response.text}), 500
    return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
