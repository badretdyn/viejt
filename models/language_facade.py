from models.syllable_validator import SyllableValidator
from models.phoneme_inventory import PhonemeInventory
from models.syllable_generator import SyllableGenerator
from utils.json_handler import JsonHandler
from models.syllable_model import Syllable

class LanguageFacade:
    def __init__(self, initials, medials, nuclei, codas, restrictions, name, desc):
        self.inventory = PhonemeInventory(initials, medials, nuclei, codas)
        self.validator = SyllableValidator(self.inventory, restrictions)
        self.generator = SyllableGenerator(self.validator)
        self.name = name
        self.desc = desc
        self.debug_mode = False

    @classmethod
    def from_json_file(cls, path: str):
        js = JsonHandler.from_file(path)
        return cls(
            js.get("initials", []),
            js.get("medials", []),
            js.get("nuclei", []),
            js.get("codas", []),
            js.get("restrictions", []),
            js.get("name", ""),
            js.get("desc", ""),
        )

    def is_valid_syllable(self, syl) -> bool:
        return self.validator.is_valid(syl)

    def random_syllable(self) -> Syllable:
        return self.generator.random_syllable()

    def random_valid_syllable(self) -> Syllable:
        return self.generator.random_valid_syllable()