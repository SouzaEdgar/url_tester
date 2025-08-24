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

            