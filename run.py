import os, re, time

print("Coletando informações da pasta...")
diretorio_atual = os.listdir()
diretorio_atual = [arqv.upper() for arqv in diretorio_atual]
print("Localizando somente as imagens da pasta...")
extensoes = ('.PNG', '.JPG', '.JPEG')
arquivos_filtrados = list(
    filter(
        lambda x: True if x.endswith(extensoes) else False, diretorio_atual
        )
    )
if arquivos_filtrados:
    print("Filtrando arquivos já renomeados...")
    contagem = [1]
    numero_nomes = re.compile('^(\d*)\.\D{0,}$')
    for arqv in arquivos_filtrados:
        numero = re.search(numero_nomes, arqv)
        if numero:
            numero = numero.group(1)
            numero = int(numero)
            contagem.append(numero)
            arquivos_filtrados.remove(arqv)
    if contagem:
        contagem.sort()
        contagem = contagem[-1]
    print("Renomeando arquivos...")
    for arqv in arquivos_filtrados:
        _, extensao = arqv.rsplit('.', 1)
        os.rename(arqv, f'{contagem}.{extensao}')
        contagem += 1
    print("Arquivos renomeados com sucesso...")
else:
    print("Não há arquivos de imagens para serem renomeados, verifique se a pasta está correta...")
print("Encerrando aplicação...")
time.sleep(5)
