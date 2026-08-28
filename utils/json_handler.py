import json

class JsonHandler:
    @staticmethod
    def from_file(path : str):
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def to_json(data, indent=2):
        return json.dumps(data, ensure_ascii=False, indent=indent)

    @staticmethod
    def to_file(data, path: str, indent: int = 2) -> None:
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)