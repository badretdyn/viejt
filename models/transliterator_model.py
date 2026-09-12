from models.phoneme_inventory import PhonemeInventory
from models.transliteration_model import Transliteration

class Transliterator:
    def __init__(self, phoneme_inventory : PhonemeInventory, transliterations : list[Transliteration]):
        self.phoneme_inventory = phoneme_inventory or PhonemeInventory([], [], [], [])
        self.transliterations = transliterations or []