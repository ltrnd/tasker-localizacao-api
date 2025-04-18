from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

localizacao = {"latitude": None, "longitude": None, "timestamp": None}
comando = {"acao": None}  # Novo: comando enviado

@app.route("/enviar", methods=["POST"])
def receber_localizacao():
    data = request.get_json()
    localizacao["latitude"] = data.get("latitude")
    localizacao["longitude"] = data.get("longitude")
    localizacao["timestamp"] = data.get("timestamp")
    return jsonify({"status": "ok", "mensagem": "Localização recebida com sucesso!"})

@app.route("/comando", methods=["GET"])
def obter_comando():
    return jsonify(comando)

@app.route("/comando", methods=["POST"])
def definir_comando():
    data = request.get_json()
    comando["acao"] = data.get("acao")
    return jsonify({"status": "ok", "mensagem": f"Comando '{comando['acao']}' recebido"})

@app.route("/localizacao", methods=["GET"])
def enviar_localizacao():
    return jsonify(localizacao)

if __name__ == "__main__":
    app.run()
