from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Memória temporária
comando = {"comando": None}
localizacao = {"latitude": None, "longitude": None, "timestamp": None}

# 📥 Rota para enviar localização
@app.route("/enviar", methods=["POST"])
def receber_localizacao():
    data = request.get_json()
    localizacao["latitude"] = data.get("latitude")
    localizacao["longitude"] = data.get("longitude")
    localizacao["timestamp"] = data.get("timestamp")
    return jsonify({"status": "ok", "mensagem": "Localização recebida com sucesso!"})

# 📤 Rota para pegar localização (se quiser usar)
@app.route("/localizacao", methods=["GET"])
def enviar_localizacao():
    return jsonify(localizacao)

# 🔁 Rota para comando
@app.route("/comando", methods=["GET", "POST"])
def gerenciar_comando():
    global comando
    if request.method == "POST":
        data = request.get_json()
        comando["comando"] = data.get("comando")
        return jsonify({"status": "ok", "mensagem": "Comando atualizado"})
    elif request.method == "GET":
        return jsonify(comando)

# 📁 Rota para upload de arquivos (foto ou áudio)
@app.route("/upload", methods=["POST"])
def upload_arquivo():
    if "arquivo" not in request.files:
        return jsonify({"status": "erro", "mensagem": "Nenhum arquivo enviado"}), 400
    
    file = request.files["arquivo"]
    if file.filename == "":
        return jsonify({"status": "erro", "mensagem": "Arquivo sem nome"}), 400

    pasta = "uploads"
    os.makedirs(pasta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho = os.path.join(pasta, f"{timestamp}_{file.filename}")
    file.save(caminho)
    return jsonify({"status": "ok", "mensagem": f"Arquivo salvo como {caminho}"})


if __name__ == "__main__":
    app.run(debug=True)
