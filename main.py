from models.language_model import *

if __name__ == "__main__":
    lang : Language = Language.from_json_file("data\\nihongo.json")
    usinp = int(input("test = "))
    lang.debug_mode = False #True

    match usinp:
        case 0:
            pass
        case 1:
            for i in range(0, 20):
                print(repr(lang.valid_random_syllable()))
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