from transformers import AutoTokenizer, AutoModel

nome_modelo = 'FacebookAI/xlm-roberta-base'

modelo = AutoModel.from_pretrained(nome_modelo)
tokenizador = AutoTokenizer.from_pretrained(nome_modelo)

tokens = tokenizador('A linguagem <mask> é uma ferramenta inovadora.')
print(tokens)

