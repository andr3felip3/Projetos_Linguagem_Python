ips = {}
resp = "S"

while resp == "S":
    ips[(input("\nDigite os \"dois pimeiros\" octetos: "),
         input(("\nDigite os \"dois ultimos\" octetos: ")))] = {
        input("\nInfome o \"nome\" da maquina: ")} # a chave será uma tupla
    resp = input("\nDigite \"S\" para continuar: ").upper()

# print("Exibindo ips's: ")
# for ip in ips.keys():
#     print(ip[0]+"."+ip[1])

# print("\nExibindo máquinas com o mesmo endereço: \n")
# pesquisa=input("Digite os dois últimos octetos: ")
# for ip,nome in ips.items():
#     print("\nMáquinas no mesmo endereço (redes diferentes:")
#     if(ip[1]==pesquisa):
#         print(nome)


print("Exibindo as máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)