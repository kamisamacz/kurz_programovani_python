import multiprocessing
import os

def run_app(app_file):
    """Spustí aplikaci jako samostatný proces."""
    os.system(f'python {app_file}')

if __name__ == "__main__":
    # Procesy pro jednotlivé aplikace
    apps = ["admin_app.py", "user_app.py", "worker_app.py"]

    processes = []
    for app in apps:
        p = multiprocessing.Process(target=run_app, args=(app,))
        p.start()
        processes.append(p)

    # Čeká na dokončení všech procesů
    for p in processes:
        p.join()
