import httpx
import asyncio
from utils import functions as adops

# ===== AsyncClient e Semaforo - global =====
client: httpx.AsyncClient | None = None
semaforo = asyncio.Semaphore(10)

# ===== Cliente (app.py inicia|fecha) =====
async def init_client():
    global client
    client = httpx.AsyncClient(follow_redirects=True, timeout=15.0)

async def close_client():
    global client
    if client:
        await client.aclose()
        client = None

async def get_response_async(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/115.0 Safari/537.36"
    }
    global client
    async with semaforo:
        try:
            response = await client.get(url, headers=headers)
            return response
        except httpx.RequestError as e:
            return e

async def process_urls_async(urls, params):
    tarefas = []
    resultados = []
    urls_validas = []

    # ===== TAREFAS (coroutines) =====
    for url in urls:
        if adops.valid_url(url):
            tarefas.append(get_response_async(url)) # Não é executado, apenas criou a coroutine
            urls_validas.append(url)
        else:
            resultados.append({
                "position": len(resultados) +1,
                "url": url,
                "params": "",
                "status": "Erro: URL inválida"
            })

    responses = await asyncio.gather(*tarefas) # Executa as tarefas em paralelo

    # ===== Trabalhar com cada URL =====
    for i, resp in enumerate(responses, start=len(resultados) +1):
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
                "url": urls_validas[i - len(resultados) -1],
                "params": "",
                "status": f"Erro: {resp}"
            })
    return resultados
