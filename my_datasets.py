from datasets import load_dataset

ds = load_dataset("stanfordnlp/imdb", streaming=True)

dataset_treino = ds['train']

print(dataset_treino[9])

# for linha in dataset_treino:
#     print(linha)
#     input()

df = dataset_treino.to_pandas()
print(df)

# input()

# print(dataset_treino['label'])

# input()

# print(dataset_treino[9]['label'])
