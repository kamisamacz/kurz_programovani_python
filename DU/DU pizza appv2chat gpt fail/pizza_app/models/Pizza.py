class Pizza:
    def __init__(self, name, base, extras=None):
        self.name = name
        self.base = base
        self.extras = extras if extras else []

    def to_dict(self):
        return {
            "name": self.name,
            "base": self.base,
            "extras": self.extras
        }
