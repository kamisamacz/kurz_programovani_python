import json
import os

# Cesta k souboru s objednávkami
STORAGE_FILE = "orders.json"

def load_orders():
    """Načte objednávky ze souboru."""
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_order(order):
    """Přidá objednávku do souboru."""
    orders = load_orders()
    orders.append(order)
    with open(STORAGE_FILE, "w", encoding="utf-8") as file:
        json.dump(orders, file, ensure_ascii=False, indent=4)
