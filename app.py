from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Armazena a última localização recebida
localizacao = {"latitude": None, "longitude": None, "timestamp": None}

# Armazena o último comando enviado pelo controlador
comando = {"comando": None}

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

@app.route("/comando", methods=["POST"])
def receber_comando():
    data = request.get_json()
    comando["comando"] = data.get("comando")
    return jsonify({"status": "ok", "mensagem": "Comando recebido com sucesso!"})

@app.route("/comando", methods=["GET"])
def enviar_comando():
    return jsonify(comando)

if __name__ == "__main__":
    app.run()
