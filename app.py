from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Estado simples em memória para a primeira versão.
# Depois podemos trocar por SQLite para registrar as quatro estações.
state = {
    "ux_completed": 0,
    "ux_points": 0,
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ux")
def ux():
    return render_template("ux.html")

@app.post("/api/ux/check")
def ux_check():
    data = request.get_json(silent=True) or {}
    score = 0
    feedback = []

    # Missão: interface com contraste, botão principal destacado e menu visível.
    if data.get("contrast") == "high":
        score += 30
        feedback.append("Boa escolha de contraste.")
    else:
        feedback.append("Tente melhorar o contraste.")

    if data.get("primary") == "solid":
        score += 30
        feedback.append("O botão principal ficou claro.")
    else:
        feedback.append("Escolha um botão principal mais evidente.")

    if data.get("menu") == "top":
        score += 20
        feedback.append("O menu ficou fácil de localizar.")
    else:
        feedback.append("Experimente colocar o menu em uma área previsível.")

    if data.get("font") == "large":
        score += 20
        feedback.append("A leitura ficou mais confortável.")
    else:
        feedback.append("Uma fonte maior pode melhorar a leitura.")

    state["ux_completed"] += 1
    state["ux_points"] = score

    return jsonify({
        "score": score,
        "feedback": feedback,
        "completed": score >= 70
    })

@app.get("/api/status")
def status():
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)