#from models.language_model import *
from models.syllable_model import Syllable
from models.language_facade import LanguageFacade

if __name__ == "__main__":
    lang : LanguageFacade = LanguageFacade.from_json_file("data\\nihongo.json")
    # lang.validator.debug_mode = True # need global congif
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