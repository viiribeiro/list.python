produtos = [[1, "maquina de lavar", 1500.00],
[2, "geladeira", 2000.00],
[3, "fogão", 1200.00]]

print (produtos)
id_procurado = 3
for produto in produtos:
    if produto [0] == id_procurado:
        print("Registro encontrado:", produto)

id_procurado = 2
for indice, produto in enumerate(produtos):
    if produto[0] == id_procurado:
        removido = produtos.pop(indice)
        print("Registro removido:", removido)
        break

print (produtos)
produtos.append([4, "microondas", 800.00])
print (produtos)
