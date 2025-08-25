import httpx
import re

    
def verify_response(response: httpx.Response):
    return isinstance(response, httpx.Response) # Retorna booleano

def status_code(response: httpx.Response):
    return [resp.status_code for resp in response.history] + [response.status_code] # Retorna a lista status code dos redirects + o status_code da url final

def redirects_history(response: httpx.Response):
    return [resp.url for resp in response.history] + [response.url] # Retorna a lista dos redirects + a url final

def parameters_search(url, parameters: list):
    found_params = [] # Criar uma lista de tuplas (findall retorna tupla)
    for x in parameters:
        match = re.findall(rf"(?:[?&])([^=&#]*{re.escape(x)}[^=&#]*)=([^&#]*)", url)
        found_params.extend(match)
    return found_params

def valid_url(url):
    regex = re.compile(r"^(https?://)([\w.-]+)(\.[a-zA-Z]{2,})(:[0-9]+)?(/.*)?$")
    return bool(regex.match(url))
