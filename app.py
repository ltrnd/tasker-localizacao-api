from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Localização armazenada em memória
localizacao = {"latitude": None, "longitude": None, "timestamp": None}
comando_pendente = {"executar": False}

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

@app.route("/comando", methods=["GET", "POST"])
def comando():
    global comando_pendente
    if request.method == 'POST':
        comando_pendente["executar"] = True
        return jsonify({"status": "comando recebido"})
    elif request.method == 'GET':
        if comando_pendente["executar"]:
            comando_pendente["executar"] = False
            return jsonify({"executar": True})
        else:
            return jsonify({"executar": False})

if __name__ == "__main__":
    app.run()
