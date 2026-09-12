from models.syllable_validator import SyllableValidator
from models.phoneme_inventory import PhonemeInventory
from models.syllable_generator import SyllableGenerator
from utils.json_handler import JsonHandler
from models.syllable_model import Syllable
from models.grapheme_extractor import GraphemeExtractor
from models.app_config import AppConfig
from models.transliterator_model import Transliterator

class Language:
    def __init__(self, initials, medials, nuclei, codas, restrictions, transliterations = None,\
                 name = None, desc = None, app_config = None):
        
        self._app_config = app_config or AppConfig()

        self.phoneme_inventory = PhonemeInventory(initials, medials, nuclei, codas, self._app_config)
        self.validator = SyllableValidator(self.phoneme_inventory, restrictions, self._app_config)
        self.generator = SyllableGenerator(self.validator, self._app_config)
        self.grapheme_extractor = GraphemeExtractor(self.phoneme_inventory, self._app_config)
        self.transliterator = Transliterator(self.phoneme_inventory, transliterations)

        self.name = name or "lang_" + str(hash(self.phoneme_inventory)) #  for random string
        self.desc = desc or self.name + "_desc"

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
    def app_config(self):
        return self._app_config

    @app_config.setter
    def app_config(self, value: AppConfig):
        self._app_config = value
        self.phoneme_inventory.app_config = value
        self.validator.app_config = value
        self.generator.app_config = value
        self.grapheme_extractor.app_config = value

    def __str__(self, separator = " "):
        return f"Language {{ " + \
            f"phoneme_inventory:{self.phoneme_inventory},{separator}" + \
            f"validator:{self.validator},{separator}" + \
            f"generator:{self.generator},{separator}" + \
            f"grapheme_extractor:{self.grapheme_extractor},{separator}" + \
            f"app_config:{self._app_config} }}"
    
    def __repr__(self):
        return self.__str__()