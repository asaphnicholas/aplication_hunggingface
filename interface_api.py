import requests
from transformers import AutoTokenizer

# Substitua pelo seu token de acesso válido
HF_TOKEN = "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"

# Modelo
model = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

# Inicializa o chat e o tokenizer
chat = []
tokenizer = AutoTokenizer.from_pretrained(model)

# URL da API
url = f'https://api-inference.huggingface.co/models/{model}'

# Headers para autenticação
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

while True:
    mensagem = input('Faça sua pergunta: ')
    if mensagem == 'q':
        break
    
    # Adiciona a mensagem ao histórico
    chat.append({'role': 'user', 'content': mensagem})
    
    # Aplica o template no tokenizer
    template = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    
    # JSON da requisição
    json = {
        'inputs': template,
        'parameters': {'max_new_token': 1000},
        'options': {'use_cache': False, 'wait_for_model': True},
    }
    
    # Faz a requisição para a API com os headers
    response = requests.post(url, headers=headers, json=json)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        response_json = response.json()
        
        # Verifica se a resposta contém o índice 0
        if isinstance(response_json, list) and len(response_json) > 0:
            mensagem_chatbot = response_json[0].get('generated_text', '').split('[/INST]')[-1]
            print('Resposta do bot:', mensagem_chatbot)
            chat.append({'role': 'assistant', 'content': mensagem_chatbot})
        else:
            print("Erro: A resposta da API não contém texto gerado.")
    else:
        print(f"Erro na API: {response.status_code} - {response.text}")

# Imprime o histórico do chat
print(chat)
