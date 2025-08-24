import requests
import re

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
        return str(e)
    
def verify_response(response: requests.Response):
    return isinstance(response, requests.Response) # Retorna booleano

def status_code(response: requests.Response):
    return [resp.status_code for resp in response.history] + [response.status_code] # Retorna a lista status code dos redirects + o status_code da url final

def redirects_history(response: requests.Response):
    return [resp.url for resp in response.history] + [response.url] # Retorna a lista dos redirects + a url final

def parameters_search(url, parameters: list):
    found_params = [] # Criar uma lista de tuplas (findall retorna tupla)
    for x in parameters:
        match = re.findall(rf"(?:[?&])([^=&#]*{re.escape(x)}[^=&#]*)=([^&#]*)", url)
        found_params.extend(match)
    return found_params
