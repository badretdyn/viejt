from models.language_model import *

if __name__ == "__main__":
    lang : Language = Language.from_json_file("data\\zh.json")

    # for i in range(0, 20):
    #     print(lang.valid_random_syllable())

    lang.debug_mode = False

    # print(sorted(list(lang.unique_graphemes)))

    syls = [
        Syllable("w", "u", "a", "n"),
        Syllable("w", "u", "u", "n"),
        Syllable("", "u", "u", ""),
        Syllable("", "", "", ""),
        Syllable("", "", "u", ""),
        Syllable("", "u", "", ""),
        Syllable("x", "i", "", ""),
        Syllable("x", "u", "", ""),
        Syllable("x", "", "u", ""),
        Syllable("x", "i", "a", ""),
        Syllable("x", "", "i", ""),
        Syllable("x", "u", "i", ""),
        Syllable("x", "", "a", ""),
        Syllable("x", "", "u", ""),
        Syllable("x", "", "ü", ""),
        Syllable("q", "a", "u", ""),
        Syllable("q", "u", "a", ""),
        Syllable("q", "", "a", ""),
        Syllable("q", "i", "a", ""),
        Syllable("", "", "", "r"),
        Syllable("", "", "a", "r"),
        Syllable("", "", "e", "r"),
        Syllable("", "u", "e", "r"),
        Syllable("n", "u", "e", "r"),
        Syllable("n", "", "e", "r"),
        Syllable("v", "", "e", "r"),
        Syllable("s", "ü", "è", "i"),
        Syllable("s", "ü", "è", "ng"),
        Syllable("s", "ü", "o", "i")
    ]

    for i in syls:
        print(f"{i}\t{lang.is_valid_syllable(i)}")