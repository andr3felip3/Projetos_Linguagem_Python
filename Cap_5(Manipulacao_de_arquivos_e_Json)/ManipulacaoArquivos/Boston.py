# Trabalhando com arquivo csv

with open("economic-indicators.csv","r") as boston: #abre arquivo com inteção de leitura
    total=0  #variavel para armazenar total de voos
    for linha in boston.readlines()[1:-1]:  # posiciona na 1 até a ultima
        total=total+float(linha.split(",")[3]) #soma cada linha
    print("O total de voos é: ", total)