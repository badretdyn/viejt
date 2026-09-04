from models.syllable_model import Syllable
from models.language_facade import Language
from models.grapheme_extractor import GraphemeExtractor
from models.phoneme_inventory import PhonemeInventory
from models.app_config import AppConfig

if __name__ == "__main__":
    appcon = AppConfig.from_json_file("app_config.json")
    lang : Language = Language.from_json_file("data\\nihongo.json")

    conf = AppConfig()
    conf.debug_mode = False
    lang.app_config = conf
    print(lang._app_config)
    print(lang.validator.app_config)
    print(lang.generator.app_config)
    
    usinp = int(input("test = "))
    match usinp:
        case 0:
            pass
        case 1:
            for i in range(0, 20):
                print(repr(lang.random_valid_syllable()))
        case 2:
            syls = [
                Syllable("", "", "a", ""),
                Syllable("k", "", "", ""),
                Syllable("k", "", "a", ""),
                Syllable("k", "i", "", ""),
                Syllable("k", "", "", "i"),
                Syllable("n", "", "a", ""),
                Syllable("n", "", "", ""),
            ]

            for i in syls:
                print(f"{i}\t{lang.is_valid_syllable(i)}")
        case 3:
            graex = GraphemeExtractor(PhonemeInventory(["p", "t", "k", "ch"], [], ["a", "o"], []))
            print(graex)
            print(graex.phoneme_inventory.max_grapheme_length)
            print(graex.phoneme_inventory.unique_graphemes)