from models.syllable_model import Syllable

class SyllableGenerator:
    def __init__(self, validator):
        self.validator = validator
        self.debug_mode = False

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

    def __str__(self):
        return f"SyllableGenerator {{ validator:{self.validator!r} }}"

    def __repr__(self):
        return self.__str__()