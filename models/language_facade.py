from models.syllable_validator import SyllableValidator
from models.phoneme_inventory import PhonemeInventory
from models.syllable_generator import SyllableGenerator
from utils.json_handler import JsonHandler
from models.syllable_model import Syllable
from models.grapheme_extractor import GraphemeExtractor

class Language:
    def __init__(self, initials, medials, nuclei, codas, restrictions, name = None, desc = None,\
                 debug_mode = None):
        self.phoneme_inventory = PhonemeInventory(initials, medials, nuclei, codas)
        self.validator = SyllableValidator(self.phoneme_inventory, restrictions)
        self.generator = SyllableGenerator(self.validator)
        self.name = name or "lang_" + str(hash(self.phoneme_inventory)) #  for random string
        self.desc = desc or self.name + "_desc"

        self._debug_mode = debug_mode or False # config

        self.grapheme_extractor = GraphemeExtractor(self.phoneme_inventory)

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

    @property
    def debug_mode(self):
        # at least one of these must have debug enabled for True
        return self._debug_mode or self.validator.debug_mode or self.generator.debug_mode

    @debug_mode.setter
    def debug_mode(self, value: bool):
        self._debug_mode = value
        self.validator.debug_mode = value
        self.generator.debug_mode = value