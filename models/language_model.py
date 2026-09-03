from utils.json_handler import JsonHandler
from models.syllable_model import Syllable

class Language:
    def __init__(self, initials = None, medials = None, nuclei = None, codas = None, restrictions : dict = None, name = "", desc = ""):
        # if initials is None:
        #     initials = []
        # if medials is None:
        #     medials = []
        # if nuclei is None:
        #     nuclei = []
        # if codas is None:
        #     codas = []

        if restrictions is None:
            restrictions = []

        for restriction in restrictions:
            if restriction.get("mode") not in ("and", "or"):
                restriction["mode"] = "and"
        
        self.initials = set(initials or [])
        self.medials = set(medials or [])
        self.nuclei = set(nuclei or [])
        self.codas = set(codas or [])
        self.restrictions = restrictions
        self.name = name
        self.desc = desc
        self.debug_mode = False

        self._unique_graphemes = None
        self._max_grapheme_length = None

    @property
    def unique_graphemes(self) -> set[str]:
        if self._unique_graphemes is None:
            all_components = self.initials | self.medials | self.nuclei | self.codas
            self._unique_graphemes = { comp for comp in all_components if comp != "" }
        return self._unique_graphemes

    @property
    def max_grapheme_length(self) -> int:
        if self._max_grapheme_length is None:
            if not self._unique_graphemes:
                self._max_grapheme_length = 1
            else:
                self._max_grapheme_length = max(len(comp) for comp in self._unique_graphemes)
        return self._max_grapheme_length

    # def _find_longest_match(self, text : str, start_pos : int) -> tuple[str, int]:
    #     return "", 0

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
            js.get("desc", "")
        )

    # def random_syl(self) -> Syllable:
    #     import random

    #     random_initial = random.randint(0, len(self.initials))
    #     random_medial = random.randint(0, len(self.medials))
    #     random_nucleus = random.randint(0, len(self.nuclei) - 1)
    #     random_coda = random.randint(0, len(self.codas))

    #     initial = (self.initials + [""])[random_initial]
    #     medial = (self.medials + [""])[random_medial]
    #     nucleus = self.nuclei[random_nucleus]
    #     coda = (self.codas + [""])[random_coda]

    #     return Syllable(initial, medial, nucleus, coda)

    def is_valid_syllable(self, syl : Syllable):
        
        print(f"syl\t{syl}") if self.debug_mode else False

        if syl.initial and syl.initial not in self.initials:
            print(f"\texit fl\t\tinitial does not exist") if self.debug_mode else False
            return False
        if syl.medial and syl.medial not in self.medials:
            print(f"\texit fl\t\tmedial does not exist") if self.debug_mode else False
            return False
        if syl.nucleus and syl.nucleus not in self.nuclei:
            print(f"\texit fl\t\tnucleus does not exist") if self.debug_mode else False
            return False
        if syl.coda and syl.coda not in self.codas:
            print(f"\texit fl\t\tcoda does not exist") if self.debug_mode else False
            return False

        if self.restrictions == []:
            print("\texit tr\t\tthere are no restrictons") if self.debug_mode else False
            return True

        for restriction in self.restrictions:

            print(f"\trestr\t\t{restriction}\n\tmode\t{restriction.get("mode")}") if self.debug_mode else False
            
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

            print(f"\tcmpnts\t\t{inInitials} {inMedials} {inNuclei} {inCodas}")  if self.debug_mode else False
            
            mode = restriction.get("mode")

            match mode:
                case "and":
                    print("\trestriction is and") if self.debug_mode else False
                    if true_count == specified_parts and specified_parts > 0:
                        print("\texit fl") if self.debug_mode else False
                        return False
                case "or": # need to think about this mode
                    print("\trestriction is or") if self.debug_mode else False
                    if true_count > 0:
                        print("\texit fl") if self.debug_mode else False
                        return False
            
        return True

    def random_syllable(self) -> Syllable:
        from random import choice
        initial = choice(list(self.initials)) if self.initials else ""
        medial = choice(list(self.medials)) if self.medials else ""
        nucleus = choice(list(self.nuclei)) if self.nuclei else ""
        coda = choice(list(self.codas)) if self.codas else ""
        return Syllable(initial, medial, nucleus, coda)

    def valid_random_syllable(self) -> Syllable:
        syl = self.random_syllable()
        while not self.is_valid_syllable(syl):
            syl = self.random_syllable()
        return syl

    def __str__(self, separator = " "):
        return f"Language {{ name:{self.name},{separator}desc:{self.desc},{separator}initials:{self.initials!r},{separator}medials:{self.medials!r},{separator}nuclei:{self.nuclei!r},{separator}codas:{self.codas!r} }}"

    def __repr__(self):
        return self.__str__()

# class Restriction:
#     def __init__(self, initial, medials, nuclei, finals):
#         self.initial = initial
#         self.medials = medials
#         self.nuclei = nuclei
#         self.finals = finals

        # why good is true