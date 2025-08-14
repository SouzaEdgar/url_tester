import requests
import re

#url = "http://google.com" # redirect -> "https://google.com" (HTTP -> HTTPS)

# Ler multiplas URLs
with open("url.txt", "r") as u:
    urls = []
    for line in u:
        line = line.strip()
        if line != "":
            urls.append(line)

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

def status_code(response):
    if isinstance(response, requests.Response):
        status = []
        for resp in response.history:
            status.append(resp.status_code) # add o status de cada URL
        status.append(response.status_code) # add o status da ultima URL
        return status
    else:
        return response

def redirects_history(response):
    if isinstance(response, requests.Response):
        redirect_chain = []

        for i, resp in enumerate(response.history, 1):
            redirect_chain.append(f"{i}. {resp.url}") # add cada URL da corrente
        redirect_chain.append(f"{len(response.history) +1}. {response.url}") # add a URL final

        return "\n".join(redirect_chain)
    else:
        return response

for url in urls:
    resposta = get_response(url)
    #print(resposta)
    print(status_code(resposta))
    #print(redirects_history(resposta))
    print()
