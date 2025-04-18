from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Localização armazenada em memória
localizacao = {"latitude": None, "longitude": None, "timestamp": None}

# Comando remoto (para o monitorado buscar)
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

@app.route("/comando", methods=["GET", "POST"])
def gerenciar_comando():
    global comando
    if request.method == "POST":
        data = request.get_json()
        comando["comando"] = data.get("comando")
        return jsonify({"status": "ok", "mensagem": "Comando recebido com sucesso!"})
    elif request.method == "GET":
        return jsonify(comando)
        comando = {"comando": None}  # limpa o comando após entregar
        return resposta

if __name__ == "__main__":
    app.run()
