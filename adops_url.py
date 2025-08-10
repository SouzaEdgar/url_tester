import requests 

url = "http://google.com" # redirect -> "https://google.com" (HTTP -> HTTPS)


def get_response(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        # tratar a mensagem de erro
        return str(e)

def status_code(response):
    if isinstance(response, requests.Response):
        return response.status_code
    else:
        return response

resposta = get_response(url)
print(resposta)
print(status_code(resposta))
