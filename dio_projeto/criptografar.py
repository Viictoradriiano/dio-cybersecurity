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
    destino = pasta("criptografados")
    chave = BASE / "chave.key"
    if chave.is_symlink():
        raise RuntimeError("Chave nao pode ser um link simbolico.")
    if chave.exists():
        segredo = chave.read_bytes()
    else:
        if any(destino.iterdir()):
            raise RuntimeError("Existem arquivos criptografados sem chave. Nao sera gerada outra chave.")
        segredo = Fernet.generate_key()
        with chave.open("xb") as f:
            f.write(segredo)
    cifra = Fernet(segredo)
    for nome in NOMES:
        entrada = origem / nome
        saida = destino / (nome + ".enc")
        if entrada.is_symlink() or not entrada.is_file():
            print("Ignorado; origem ausente ou link:", nome)
            continue
        if saida.exists() or saida.is_symlink():
            print("Preservado; ja existe:", saida.name)
            continue
        with saida.open("xb") as f:
            f.write(cifra.encrypt(entrada.read_bytes()))
        print("Copia criptografada:", saida.name)
    aviso = BASE / "mensagem_resgate.txt"
    if not aviso.exists() and not aviso.is_symlink():
        with aviso.open("x", encoding="utf-8") as f:
            f.write("SIMULACAO EDUCACIONAL. Nenhum original foi removido. Nenhum pagamento e necessario. Execute descriptografar.py para recuperar copias.")
    print("Originais preservados. Laboratorio:", BASE)

if __name__ == "__main__":
    main()
