from pathlib import Path
from cryptography.fernet import Fernet
BASE = Path(__file__).resolve().parent / "laboratorio_seguro"
NOMES = ("relatorio.txt", "anotacoes.txt", "lista_de_compras.txt")

def pasta(nome):
    if BASE.is_symlink():
        raise RuntimeError("Laboratorio nao pode ser um link simbolico.")
    BASE.mkdir(exist_ok=True)
    p = BASE / nome
    if p.is_symlink():
        raise RuntimeError("Pasta nao pode ser um link simbolico.")
    p.mkdir(exist_ok=True)
    return p

def main():
    origem = pasta("criptografados")
    destino = pasta("recuperados")
    chave = BASE / "chave.key"
    if chave.is_symlink() or not chave.is_file():
        raise RuntimeError("Chave ausente ou invalida. Nao gere outra chave para recuperar dados antigos.")
    cifra = Fernet(chave.read_bytes())
    for nome in NOMES:
        entrada = origem / (nome + ".enc")
        saida = destino / nome
        if entrada.is_symlink() or not entrada.is_file():
            continue
        if saida.exists() or saida.is_symlink():
            print("Preservado; ja existe:", nome)
            continue
        dados = cifra.decrypt(entrada.read_bytes())
        with saida.open("xb") as f:
            f.write(dados)
        print("Copia recuperada:", nome)
    print("Arquivos criptografados e originais preservados.")

if __name__ == "__main__":
    main()
