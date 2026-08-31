from utils.json_handler import JsonHandler
from models.syllable_model import Syllable

class Language:
    def __init__(self, initials, medials, nuclei, codas, restrictions = None):
        if restrictions is None:
            restrictions = []
        self.initials = initials
        self.medials = medials
        self.nuclei = nuclei
        self.codas = codas
        self.restrictions = restrictions

    # @classmethod
    # def from_json_file(cls, path : str):
    #     js = JsonHandler.from_file(path)
    #     return cls(js["initials"], js["medials"], js["nuclei"], js["codas"], js["restrictions"])

    @classmethod
    def from_json_file(cls, path: str):
        js = JsonHandler.from_file(path)
        return cls(
            js.get("initials", []),
            js.get("medials", []),
            js.get("nuclei", []),
            js.get("codas", []),
            js.get("restrictions", [])
        )

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

    def is_valid_syllable(self, syl : Syllable):

        print(f"syl\t{syl}")

        for restriction in self.restrictions:

            print(f"rst\t\t{restriction}")
            
            inInitials = syl.initial in (restriction.get("initials") or [])
            inMedials = syl.medial in (restriction.get("medials") or [])
            inNuclei = syl.nucleus in (restriction.get("nuclei") or [])
            inCodas = syl.coda in (restriction.get("codas") or [])
            
            true_count = sum([inInitials, inMedials, inNuclei, inCodas])

            specified_parts = 0
            if restriction.get("initials") is not None:
                specified_parts += 1
            if restriction.get("medials") is not None:
                specified_parts += 1
            if restriction.get("nuclei") is not None:
                specified_parts += 1
            if restriction.get("codas") is not None:
                specified_parts += 1

            print(f"\t\t{inInitials} {inMedials} {inNuclei} {inCodas} = {not (true_count == specified_parts and specified_parts > 0)}")

            if true_count == specified_parts and specified_parts > 0:
                return False

        return True

    def random_syllable(self) -> Syllable:
        from random import choice
        initial = choice(self.initials)
        medial = choice(self.medials)
        nucleus = choice(self.nuclei)
        coda = choice(self.codas)
        return Syllable(initial, medial, nucleus, coda)

    def valid_random_syllable(self) -> Syllable:
        syl = self.random_syllable()
        while not self.is_valid_syllable(syl):
            syl = self.random_syllable()
        return syl

    def __str__(self):
        return f"Language {{ {self.initials!r}, {self.medials!r}, {self.nuclei!r}, {self.codas!r} }}"

    def __repr__(self):
        return self.__str__()

# class Restriction:
#     def __init__(self, initial, medials, nuclei, finals):
#         self.initial = initial
#         self.medials = medials
#         self.nuclei = nuclei
#         self.finals = finals

        # why good is true