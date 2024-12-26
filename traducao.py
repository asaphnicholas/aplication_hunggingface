from transformers import pipeline 

modelo = "facebook/mbart-large-50-many-to-many-mmt"


menssagem = [
    'Olá eustou aprendendo a programar em python, e a usar modelo de inteligencia artificial',
    'Faça a pessoa que você gosta se sentir especial ao invés de só mais uma.',
    'não deveríamos temer a morte, mais sim a vida.',
    'Teu abraço eras confortante⁠.',
]

linguas = ['en_XX', 'es_XX', 'fr_XX']

tradutor = pipeline(task= 'translation', model=modelo)

for lingua in linguas:
    print(f'Traduzinfo para {lingua}...')
    trad = tradutor(menssagem, src_lang='pt_XX', tgt_lang=lingua)
    for mensagem, traducao in zip(menssagem, trad):
        print(f'Frase original:', mensagem)
        frase_traduzida = traducao['translation_text']
        print(f'Frase em {lingua}: "{frase_traduzida}"')



