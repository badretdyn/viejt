from models.phoneme_inventory import PhonemeInventory
from models.transliteration_model import Transliteration
from models.app_config import AppConfig

class Transliterator:
    def __init__(self, phoneme_inventory : PhonemeInventory, transliterations : list[Transliteration], app_config : AppConfig = None):
        self.app_config = app_config or AppConfig()
        self.phoneme_inventory = phoneme_inventory or PhonemeInventory([], [], [], [])
        self.transliterations = transliterations or []
        if self.app_config: print("ttor")
        
    def __str__(self):
        return f"Transliterator {{ phoneme_inventory: {self.phoneme_inventory}, transliterations: {self.transliterations}, app_config: {self.app_config} }}"