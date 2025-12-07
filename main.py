from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Tester bot server is running!"

@app.route('/callback', methods=['POST'])
def callback():
    data = request.get_json()
    print("Message received:", data)

    if data.get("sender_type") != "bot":
        print("User said:", data.get("text"))

    return "ok", 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
