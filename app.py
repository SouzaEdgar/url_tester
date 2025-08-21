from flask import Flask, render_template, request
import functions as adops
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultados = []

    if request.method == "POST":
        # ===== URLs ===== 
        user_urls = request.form.get("url", "").splitlines()
        urls = []
        for linha in user_urls:
            linha = linha.strip()
            if linha: # <--- ignorar linhas vazias
                urls.append(linha)

        # ===== Parametros ===== 
        raw_params = request.form.get("parameter", "")
        user_params = re.split(r"[;\n,]+", raw_params)
        params = []
        for param in user_params:
            param = param.strip()
            if param:
                params.append(param)
        
        # ===== Trabalhar com cada URL ===== 
        for url in urls:
            resposta = adops.get_response(url)
            if adops.verify_response(resposta):
                print(f"PASSOU!\n{adops.verify_response(resposta)}")
                url_final = adops.redirects_history(resposta)
                parametros = adops.parameters_search(resposta, params)
                status_final = adops.status_code(resposta)

                resultados.append({
                    "url": url_final[-1],
                    "params": parametros,
                    "status": status_final[-1]
                })

    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
