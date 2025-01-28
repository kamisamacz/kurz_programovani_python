from threading import Lock

class SharedData:
    _data = {}
    _lock = Lock()

    @staticmethod
    def set(key, value):
        with SharedData._lock:
            SharedData._data[key] = value
            print(f"Nastavena hodnota {key}: {value}")

    @staticmethod
    def get(key):
        with SharedData._lock:
            value = SharedData._data.get(key)
            print(f"Získána hodnota {key}: {value}")
            return value
