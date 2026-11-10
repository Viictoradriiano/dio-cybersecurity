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
    origem = pasta("originais")
    for nome in NOMES:
        p = origem / nome
        if p.exists() or p.is_symlink():
            print("Preservado:", nome)
            continue
        with p.open("xb") as f:
            f.write(("Arquivo ficticio de laboratorio: " + nome + "\n").encode())
        print("Criado:", nome)

if __name__ == "__main__":
    main()
