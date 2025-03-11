from pathlib import Path
from itertools import chain
import time

ordenacao_arquivos_renomeados = []

extensoes_imagens = ('*.PNG', '*.JPG', '*.JPEG', "*.HEIC")
print("Coletando informações da pasta...")
diretorio = Path(__file__).cwd()
print("Localizando somente as imagens da pasta...")
arquivos_imagem = [list(diretorio.glob(extensao)) for extensao in extensoes_imagens]
if arquivos_imagem:
    arquivos_nao_renomeados = list(chain(*arquivos_imagem))
    print("Filtrando arquivos já renomeados...")
    arquivos_nao_renomeados_base = arquivos_nao_renomeados.copy()
    for arquivo in arquivos_nao_renomeados_base:
        if arquivo.stem.startswith("IMG-"):
            _, numero = arquivo.stem.split("-")
            numero = int(numero)
            ordenacao_arquivos_renomeados.append(numero)
            arquivos_nao_renomeados.remove(arquivo)
    arquivos_nao_renomeados = sorted(arquivos_nao_renomeados, key=lambda x: x.stat().st_mtime)
    ordenacao_arquivos_renomeados.sort()
    ultimo_valor = ordenacao_arquivos_renomeados[-1] + 1
    print("Renomeando arquivos...")
    for arqv in arquivos_nao_renomeados:
        arqv.rename(f"IMG-{ultimo_valor}{arqv.suffix}")
        ultimo_valor += 1
    print("Arquivos renomeados com sucesso...")
else:
    print("Não há arquivos de imagens para serem renomeados, verifique se a pasta está correta...")
print("Encerrando aplicação...")
time.sleep(5)