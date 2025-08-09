import requests 

url = "https://google.com"

try:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"URL final: {response.url}")
    print(f"Redirecionamentos: {response.history}")
except requests.exceptions.RequestException as e:
    print(f"Erro: {e}")
