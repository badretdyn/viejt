class AppConfig:
    def __init__(self, debug_mode = None):
        self.debug_mode = debug_mode or False

    @classmethod
    def from_json_file(cls, path):
        from utils.json_handler import JsonHandler
        js = JsonHandler.from_file(path)
        instance = cls()
        instance.debug_mode = js.get("debug mode", False)
        return instance

    def dump(self):
        return f"AppConfig {{ debug_mode:{self.debug_mode} }}"

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return f"AppConfig(debug_mode={self.debug_mode!r})"