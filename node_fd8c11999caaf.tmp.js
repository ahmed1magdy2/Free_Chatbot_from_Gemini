from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyDWv2VB6Bnn0a8lWunuVl_S5HZmcWysIQs"
API_URL = "https://api.gemini.com/v1/chatbot"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    response = requests.post(
        API_URL,
        headers={'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'},
        json={'message': user_message}
    )
    bot_reply = response.json()
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
