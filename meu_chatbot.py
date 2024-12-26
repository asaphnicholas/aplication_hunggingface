from transformers import pipeline

chatbot = pipeline( 
    task="text-generation",
    model="Felladrin/Llama-68M-Chat-v1",
    max_new_tokens=300,
    penalty_alpha= 0.5,
    top_k= 4,
)


# <|im_start|>system
# {system_message}<|im_end|>
# <|im_start|>user
# {user_message}<|im_end|>
# <|im_start|>assistant

mensagem_siatema = 'You are a helpful artificial intelligence'
prompt_sistema = f'<|im_start|>system\n{mensagem_siatema}<|im_end|>'

pergunta = 'Hi, what is your name?'
print('Sua pergunta:', pergunta)
prompt_usuario = f'<|im_start|>user\n{pergunta}<|im_end|>'

conversa = f'{prompt_sistema}{prompt_usuario}<|im_start|>assistant'


resposta = chatbot(pergunta)
print(resposta)
