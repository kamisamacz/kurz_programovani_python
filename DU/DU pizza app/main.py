import subprocess
import sys

def run_app(module_name):
    """Spustí jednotlivou aplikaci."""
    subprocess.Popen([sys.executable, module_name])

if __name__ == "__main__":
    # Spuštění jednotlivých aplikací jako samostatné procesy
    run_app("admin_app.py")
    run_app("user_app.py")
    run_app("worker_app.py")