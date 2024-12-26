import requests

modelo= 'csebuetnlp/mT5_multilingual_XLSum'
url= f'https://api-inference.huggingface.co/models/{modelo}'

with open('brasil.txt', encoding='utf8') as f:
    texto = f.read()

json = {
    'inputs': texto,
    'parameters': {'min_length': 200},
    'options': {'use_cache': False, 'wait_for_model': True},
}

response = requests.post(url, json=json)
print(response.json())