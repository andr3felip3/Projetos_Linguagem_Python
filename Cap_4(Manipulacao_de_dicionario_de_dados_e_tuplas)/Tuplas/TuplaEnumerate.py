usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower()) #lower():tranforma minusculo
    resp=input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1]) # usa o indice(chave) na tupla apenas para percorrer ela, o 1 é para exibir a segunda parte dela.
    usuarios[tupla[chave]]=[input("Digite o nome: "), input("Digite o nível: ")]

print(usuarios)