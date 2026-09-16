from models.phoneme_inventory import PhonemeInventory
from models.transliteration_model import Transliteration
from models.app_config import AppConfig
from models.syllable_model import Syllable

class Transliterator:
    def __init__(self, phoneme_inventory : PhonemeInventory, transliterations : list, app_config : AppConfig = None):
        self.app_config = app_config or AppConfig()
        self.phoneme_inventory = phoneme_inventory or PhonemeInventory([], [], [], [])

        translits = dict()
        for i, t in enumerate(transliterations or []):
            tr_name = t.get("name", "transliteration_" + str(i))
            tr_initials = dict(t.get("initials", []))
            tr_medials = dict(t.get("medials", []))
            tr_nuclei = dict(t.get("nuclei", []))
            tr_codas = dict(t.get("codas", []))
            translit = Transliteration(tr_initials, tr_medials, tr_nuclei, tr_codas, tr_name)
            translits[tr_name] = translit

        self.transliterations : dict[str, Transliteration] = translits

    def transliterate(self, syl, translit_name):
        translit = self.transliterations.get(translit_name)
        if translit is None:
            raise ValueError(f"transliterator.transliterate(...): Transliteration {translit_name!r} not found")

        result = Syllable(syl.initial, syl.medial, syl.nucleus, syl.coda)
        result.initial = translit.initials.get(syl.initial, syl.initial)
        result.medial = translit.medials.get(syl.medial, syl.medial)
        result.nucleus = translit.nuclei.get(syl.nucleus, syl.nucleus)
        result.coda = translit.codas.get(syl.coda, syl.coda)

        return result

    def dump(self):
        return f"Transliterator ( phoneme_inventory={self.phoneme_inventory!r}, transliterations={self.transliterations!r}, app_config={self.app_config} )"

    def __repr__(self):
        return f"Transliterator(app_config={self.app_config!r})"