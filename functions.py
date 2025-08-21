import requests
import re

#url = "http://google.com" # redirect -> "https://google.com" (HTTP -> HTTPS)

# Ler multiplas URLs
# with open("url.txt", "r") as u:
#     urls = []
#     for line in u:
#         line = line.strip()
#         if line != "":
#             urls.append(line)

def get_response(url):
    headers = {
        "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                        "AppleWebKit/537.36 (KHTML, like Gecko)"
                        "Chrome/115.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        return response
    except requests.exceptions.RequestException as e:
        # tratar a mensagem de erro
        return str(e)
    
def verify_response(response: requests.Response):
    if isinstance(response, requests.Response):
        return 1
    return 0

def status_code(response: requests.Response):
    status = []
    for resp in response.history:
        status.append(resp.status_code) # add o status de cada URL
    status.append(response.status_code) # add o status da ultima URL
    return status

def redirects_history(response: requests.Response):
    redirect_chain = []

    for resp in response.history:
        redirect_chain.append(resp.url) # add cada URL da corrente
    redirect_chain.append(response.url) # add a URL final
    return redirect_chain

def parameters_search(response: requests.Response, parameters: list):
    url = response.url
    found_params = [] # Criar uma lista de tuplas (findall retorna tupla)

    for x in parameters:
        match = re.findall(rf"(?:[?&])([^=&#]*{re.escape(x)}[^=&#]*)=([^&#]*)", url)
        if match:
            found_params.extend(match)
    return found_params

# for url in urls:
#     resposta = get_response(url)
#     if isinstance(resposta, requests.Response):
#         print(status_code(resposta))
#         print(redirects_history(resposta))
#         parametro = ["aaaa", "bbb", "gws", "utm_source", "utm_ad", "teste"]
#         print(parameters_search(resposta, parametro))
#         print()
#     else:
#         print(resposta) # Mensagem de erro
#         print()
