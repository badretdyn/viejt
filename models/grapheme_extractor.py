from models.phoneme_inventory import PhonemeInventory
from models.syllable_validator import SyllableValidator
from models.app_config import AppConfig

class GraphemeExtractor:
    def __init__(self, phoneme_inventory : PhonemeInventory, app_config = None):
        self.phoneme_inventory = phoneme_inventory
        self.app_config = app_config or AppConfig()

    def _get_grapheme(self, text : str):
        max_grapheme_length = self.phoneme_inventory.max_grapheme_length
        if self.app_config: print(f"grex\tmxgrlen={max_grapheme_length}")

        char = 0
        grapheme = ""
        while char < len(text):
            if self.app_config: print(f"grex\twh {char} < {len(text)}")

            for graph_len in range(max_grapheme_length, 0, -1):
                if self.app_config: print(f"grex\t\tfr i={graph_len} char:{char}")

                grapheme = ""
                try:
                    grapheme = text[char : char+graph_len]
                    if self.app_config: print(f"grex\t\t\tgr={grapheme}")
                except Exception as e:
                    if self.app_config: print(f"grex\t\t\terror={e}")
                
                if grapheme in self.phoneme_inventory.unique_graphemes:
                    if self.app_config: print(f"grex\t\trt={grapheme}, {char}")
                    return grapheme, char

            char += 1

        if self.app_config: print(f"grex\t={grapheme}, {char}")
        return grapheme, char

    def dump(self):
        return f"GraphemeExtractor {{ phoneme_inventory:{self.phoneme_inventory} }}"

    def __str__(self):
        return self.dump()

    def __repr__(self):
        return f"GraphemeExtractor(app_config={self.app_config!r})"