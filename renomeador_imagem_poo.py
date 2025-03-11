from pathlib import Path
from itertools import chain
import time

def coletar_arquivos_imagem(diretorio, extensoes_imagens):
    """Coleta arquivos de imagem na pasta."""
    arquivos_imagem = [list(diretorio.glob(extensao)) for extensao in extensoes_imagens]
    return list(chain(*arquivos_imagem))

def filtrar_arquivos_renomeados(arquivos_nao_renomeados):
    """Filtra arquivos já renomeados e retorna os não renomeados."""
    ordenacao_arquivos_renomeados = []
    arquivos_nao_renomeados_base = arquivos_nao_renomeados.copy()

    for arquivo in arquivos_nao_renomeados_base:
        if arquivo.stem.startswith("IMG-"):
            _, numero = arquivo.stem.split("-")
            numero = int(numero)
            ordenacao_arquivos_renomeados.append(numero)
            arquivos_nao_renomeados.remove(arquivo)

    return arquivos_nao_renomeados, ordenacao_arquivos_renomeados

def renomear_arquivos(arquivos_nao_renomeados, ordenacao_arquivos_renomeados):
    """Renomeia os arquivos não renomeados."""
    arquivos_nao_renomeados = sorted(arquivos_nao_renomeados, key=lambda x: x.stat().st_mtime)
    ordenacao_arquivos_renomeados.sort()

    if ordenacao_arquivos_renomeados:
        ultimo_valor = ordenacao_arquivos_renomeados[-1] + 1
    else:
        ultimo_valor = 1

    for arquivo in arquivos_nao_renomeados:
        arquivo.rename(f"IMG-{ultimo_valor}{arquivo.suffix}")
        ultimo_valor += 1

def main():
    print("Coletando informações da pasta...")
    diretorio = Path(__file__).cwd()
    print("Localizando somente as imagens da pasta...")

    extensoes_imagens = ('*.PNG', '*.JPG', '*.JPEG', "*.HEIC")
    arquivos_imagem = coletar_arquivos_imagem(diretorio, extensoes_imagens)

    if arquivos_imagem:
        print("Filtrando arquivos já renomeados...")
        arquivos_nao_renomeados, ordenacao_arquivos_renomeados = filtrar_arquivos_renomeados(arquivos_imagem)

        print("Renomeando arquivos...")
        renomear_arquivos(arquivos_nao_renomeados, ordenacao_arquivos_renomeados)
        print("Arquivos renomeados com sucesso...")
    else:
        print("Não há arquivos de imagens para serem renomeados, verifique se a pasta está correta...")

    print("Encerrando aplicação...")
    time.sleep(5)

if __name__ == "__main__":
    main()
