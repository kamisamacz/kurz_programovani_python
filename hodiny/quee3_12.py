class Queue:
    def __init__(self):
        # Inicializace prázdné fronty
        self.items = []

    def add_last(self, item):
        # Přidání prvku na konec fronty
        self.items.append(item)

    def delete_first(self):
        # Odstranění prvního prvku z fronty
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def get_peek(self):
        # Získání prvního prvku bez odstranění
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        # Kontrola, zda je fronta prázdná
        return len(self.items) == 0

    def size(self):
        # Získání velikosti fronty
        return len(self.items)
