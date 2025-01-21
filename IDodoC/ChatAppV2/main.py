import subprocess
import os

# Funkce pro spuštění souboru v novém procesu s pozicí
def run_file_async(file_name, x, y):
    try:
        # Ověří, zda soubor existuje
        if not os.path.exists(file_name):
            print(f"Soubor '{file_name}' nebyl nalezen.")
            return

        # Spustí soubor v novém procesu na pozadí s parametry pro pozici
        subprocess.Popen(["python", file_name, str(x), str(y)])
    except Exception as e:
        print(f"Chyba při spuštění souboru: {e}")

# Hlavní část programu
if __name__ == "__main__":
    print("Spouštím zadané soubory...")

    # Seznam souborů k automatickému spuštění
    files_to_run = ["server.py", "chat 1 v2.py", "chat 3 v2.py", "chat 2 v2.py"]

    # Výchozí pozice oken
    start_x = 0
    start_y = 0
    offset = 300  # Posun mezi okny

    for index, file_name in enumerate(files_to_run):
        x = start_x + index * offset
        y = start_y + index * offset
        print(f"Spouštím: {file_name} na pozici ({x}, {y})")
        run_file_async(file_name, x, y)
