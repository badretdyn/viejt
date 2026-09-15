from models.syllable_model import Syllable
from models.app_config import AppConfig

class SyllableGenerator:
    def __init__(self, validator, app_config):
        self.validator = validator
        self._app_config = app_config or AppConfig()

    def random_syllable(self) -> Syllable:
        from random import choice
        initial = choice(list(self.validator.phoneme_inventory.initials)) if self.validator.phoneme_inventory.initials else ""
        medial = choice(list(self.validator.phoneme_inventory.medials)) if self.validator.phoneme_inventory.medials else ""
        nucleus = choice(list(self.validator.phoneme_inventory.nuclei)) if self.validator.phoneme_inventory.nuclei else ""
        coda = choice(list(self.validator.phoneme_inventory.codas)) if self.validator.phoneme_inventory.codas else ""
        return Syllable(initial, medial, nucleus, coda)

    def random_valid_syllable(self) -> Syllable:
        syl = self.random_syllable()
        while not self.validator.is_valid(syl):
            syl = self.random_syllable()
        return syl

    @property
    def app_config(self):
        return self._app_config

    @app_config.setter
    def app_config(self, value: AppConfig):
        self._app_config = value
        self.validator.app_config = value

    def dump(self):
        return f"SyllableGenerator {{ validator:{self.validator}, app_config: {self.app_config} }}"

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return f"SyllableGenerator(validator={self.validator!r}, app_config={self.app_config!r})"