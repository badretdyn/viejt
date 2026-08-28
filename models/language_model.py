from utils.json_handler import JsonHandler
from models.syllable_model import Syllable

class Language:
    def __init__(self, initials : list[str], medials: list[str], nuclei: list[str], codas: list[str]):
        self.initials = initials
        self.medials = medials
        self.nuclei = nuclei
        self.codas = codas

    @classmethod
    def empty(cls):
        return cls([], [], [], [])

    @classmethod
    def from_json_file(cls, path : str):
        js = JsonHandler.from_file(path)
        return cls(js["initials"], js["medials"], js["nuclei"], js["codas"])

    def random_syl(self) -> Syllable:
        import random

        random_initial = random.randint(0, len(self.initials))
        random_medial = random.randint(0, len(self.medials))
        random_nucleus = random.randint(0, len(self.nuclei) - 1)
        random_coda = random.randint(0, len(self.codas))

        initial = (self.initials + [""])[random_initial]
        medial = (self.medials + [""])[random_medial]
        nucleus = self.nuclei[random_nucleus]
        coda = (self.codas + [""])[random_coda]

        return Syllable(initial, medial, nucleus, coda)

    def __str__(self):
        return f"Language {{ {self.initials!r}, {self.medials!r}, {self.nuclei!r}, {self.codas!r} }}"

    def __repr__(self):
        return self.__str__()