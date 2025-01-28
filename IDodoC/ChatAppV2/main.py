import subprocess
import os
import time

# Funkce pro spuštění souboru v novém procesu bez určení pozice
def run_file_async(file_name):
    try:
        # Ověří, zda soubor existuje
        if not os.path.exists(file_name):
            print(f"Soubor '{file_name}' nebyl nalezen.")
            return

        # Spustí soubor v novém procesu na pozadí
        subprocess.Popen(["python", file_name])
    except Exception as e:
        print(f"Chyba při spuštění souboru: {e}")

# Hlavní část programu
if __name__ == "__main__":
    print("Spouštím zadané soubory...")

    # Seznam souborů k automatickému spuštění
    files_to_run = ["server.py", "last_stat_app.py", "alltime.py", "chat2.py", "chat1.py", "chat3.py"]

    for file_name in files_to_run:
        print(f"Spouštím: {file_name}")
        time.sleep(1)
        run_file_async(file_name)
