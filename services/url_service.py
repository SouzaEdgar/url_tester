import httpx
import asyncio
from utils import functions as adops

async def get_response_async(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/115.0 Safari/537.36"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, follow_redirects=True, timeout=15.0)
            return response
        except httpx.RequestError as e:
            return str(e)

async def process_urls_async(urls, params):
    # ===== TAREFAS (coroutines) =====
    tarefas = []
    for url in urls:
        tarefas.append(get_response_async(url)) # Não é executado, apenas criou a coroutine

    responses = await asyncio.gather(*tarefas) # Executa as tarefas em paralelo

    # ===== Trabalhar com cada URL =====
    resultados = []
    for i, resp in enumerate(responses, start=1):
        if isinstance(resp, httpx.Response): # Se for valido 
            parametros = adops.parameters_search(str(resp.url), params)
            parametros_str = f"<ul>{"".join([f"<li><b>{k}:</b> {v}</li>" for k, v in parametros])}</ul>"
            resultados.append({
                "position": i,
                "url": resp.url,
                "params": parametros_str,
                "status": resp.status_code
            })
        else:
            resultados.append({
                "position": i,
                "url": urls[i -1],
                "params": "",
                "status": "Erro"
            })
    return resultados
