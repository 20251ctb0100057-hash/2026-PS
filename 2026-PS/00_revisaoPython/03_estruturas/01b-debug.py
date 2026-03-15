# Arquivo: 01b-debug.py

catalogo = [
	{"titulo": "Código Limpo", "autor": "Robert C. Martin", "disponivel": True},
	{"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "disponivel": False},
	{"titulo": "Python Fluente", "autor": "Luciano Ramalho", "disponivel": True}
]

print("Primeiro livro:", catalogo[0]["titulo"])

print("\nLivros disponíveis:")
for livro in catalogo:
	if livro["disponivel"]:
		print(f'{livro["titulo"]}')

total = len(catalogo)
print(f"\nTotal de livros: {total}")

for chave, valor in catalogo[0].items():
	print(f"{chave} : {valor}")

primeiro_autor = catalogo[0]["autor"]
print("\nAutor do primeiro livro:", primeiro_autor)