#enrique

import time
import keyboard
import os
import sys

print("\n>>>ta funcionando<<<\n")

def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def sleep(seconds=2):
    time.sleep(seconds)

def create_sample_input(path):
    sample = [
        "bartolomeu",
        "enrique",
        "joaquim"
    ]
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(sample))
        print(f"criei um arquivo pra vc botar o texto :3 em:\n  {path}\n ")
        sleep(2)
    except Exception as e:
        print(f"n deu input.txt: {e}")
        sleep(2)

def spam():
    base_dir = get_base_dir()
    file_path = os.path.join(base_dir, "input.txt")

    if not os.path.exists(file_path):
        create_sample_input(file_path)
        return

    with open(file_path, encoding='utf-8') as text:
        lines = [ln.rstrip("\n") for ln in text]

    non_empty = [ln for ln in lines if ln.strip() != ""]
    if not non_empty:
        print("acho que vc esqueceu de adcionar texto.")
        return

    print("Muda de tela AGORA e espere alguns segundos.")
    sleep(6)

    for each_line in non_empty:
        try:
            keyboard.write(each_line)
            keyboard.press('enter')
            time.sleep(0.12) 
        except Exception as e:
            print(f"provavalemente seu layout de teclado e cozido: {e}")
            print("corre como adm")
            return

def main():
    spam()

if __name__ == "__main__":
    main()
