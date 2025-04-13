from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Localização armazenada em memória (simples)
localizacao = {"latitude": None, "longitude": None, "timestamp": None}

@app.route("/enviar", methods=["POST"])
def receber_localizacao():
    data = request.get_json()
    localizacao["latitude"] = data.get("latitude")
    localizacao["longitude"] = data.get("longitude")
    localizacao["timestamp"] = data.get("timestamp")
    return jsonify({"status": "ok", "mensagem": "Localização recebida com sucesso!"})

@app.route("/localizacao", methods=["GET"])
def enviar_localizacao():
    return jsonify(localizacao)

if __name__ == "__main__":
    app.run()
