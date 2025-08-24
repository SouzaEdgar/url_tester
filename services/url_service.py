import re
from utils import functions as adops

def process_urls(urls_raw: list, params_raw: str):
    resultados = []

    # ===== Tratar - URL ===== 
    urls = []
    for u in urls_raw:
        if u.strip():
            urls.append(u.strip())

    # ===== Trata - Parametros ===== 
    user_params = re.split(r"[;\n,]+", params_raw)
    params = []
    for p in user_params:
        if p.strip():
            params.append(p.strip())

    # ===== Trabalhar com cada URL =====
    for i, url in enumerate(urls, start=1):
        resposta = adops.get_response(url)

        if adops.verify_response(resposta):
            url_final = resposta.url
            parametros = adops.parameters_search(url_final, params)
            parametros_str = f"<ul>{"".join([f"<li><b>{k}:</b> {v}</li>" for k, v in parametros])}</ul>"

            resultados.append({
                "position": i,
                "url": url_final,
                "params": parametros_str,
                "status": resposta.status_code
            })

    return resultados
