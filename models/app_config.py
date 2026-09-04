class AppConfig:
    def __init__(self):
        self.debug_mode = False

    @classmethod
    def from_json_file(cls, path):
        from utils.json_handler import JsonHandler
        js = JsonHandler.from_file(path)
        instance = cls()
        instance.debug_mode = js.get("debug mode", False)
        return instance

    def __str__(self):
        return f"AppConfig {{ debug_mode:{self.debug_mode} }}"

    def __repr__(self):
        return self.__repr__()