from models.phoneme_inventory import PhonemeInventory
from models.transliteration_model import Transliteration
from models.app_config import AppConfig

class Transliterator:
    def __init__(self, phoneme_inventory : PhonemeInventory, transliterations : list, app_config : AppConfig = None):
        self.app_config = app_config or AppConfig()
        self.phoneme_inventory = phoneme_inventory or PhonemeInventory([], [], [], [])

        translits = []
        for i, t in enumerate(transliterations or []):
            tr_name = t.get("name", "transliteration_" + str(i))
            tr_initials = dict(t.get("initials", []))
            tr_medials = dict(t.get("medials", []))
            tr_nuclei = dict(t.get("nuclei", []))
            tr_codas = dict(t.get("codas", []))
            translit = Transliteration(tr_initials, tr_medials, tr_nuclei, tr_codas, tr_name)
            translits.append(translit)

        self.transliterations = translits

    def transliterate(self, syl):
        pass

    def dump(self):
        return f"Transliterator {{ phoneme_inventory:{self.phoneme_inventory}, transliterations:{self.transliterations}, app_config:{self.app_config} }}"

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return f"Transliterator(app_config={self.app_config!r})"