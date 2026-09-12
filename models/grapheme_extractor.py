from models.phoneme_inventory import PhonemeInventory
from models.syllable_validator import SyllableValidator
from models.app_config import AppConfig

class GraphemeExtractor:
    def __init__(self, phoneme_inventory : PhonemeInventory, app_config = None):
        self.phoneme_inventory = phoneme_inventory
        self.app_config = app_config or AppConfig()

    def _get_grapheme(self, text : str):
        max_grapheme_length = self.phoneme_inventory.max_grapheme_length
        print(f"ge\tmgl:{max_grapheme_length}") if self.app_config.debug_mode else False

        char = 0
        grapheme = ""
        while char < len(text):
            print(f"ge\twh {char} < {len(text)}") if self.app_config.debug_mode else False


            for graph_len in range(max_grapheme_length, 0, -1):
                print(f"ge\t\tfr i:{graph_len} char:{char}") if self.app_config.debug_mode else False

                grapheme = ""
                try:
                    grapheme = text[char : char+graph_len]
                    print(f"ge\t\t\tgrapheme: {grapheme}") if self.app_config.debug_mode else False
                except Exception as e:
                    print(f"ge\t\t\terror: {e}") if self.app_config.debug_mode else False
                
                if grapheme in self.phoneme_inventory.unique_graphemes:
                    return grapheme, char

            char += 1

        return grapheme, char

    def __str__(self):
        return f"GraphemeExtractor {{ phoneme_inventory:{self.phoneme_inventory} }}"

    def __repr__(self):
        return self.__str__()