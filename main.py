from models.syllable_model import Syllable
from models.language_facade import Language
from models.grapheme_extractor import GraphemeExtractor
from models.phoneme_inventory import PhonemeInventory
from models.app_config import AppConfig

if __name__ == "__main__":
    appcon = AppConfig.from_json_file("app_config.json")
    lang : Language = Language.from_json_file("data\\viet.json", appcon)
    
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
                Syllable("k", "", "a", "\\tsu"),
            ]

            for i in syls:
                print(f"{i.dump()}\t{lang.is_valid_syllable(i)}")
            
        case 3:
            #phoneme inventory
            from models.syllable_validator import SyllableValidator
            graex = GraphemeExtractor(PhonemeInventory( ["p", "t", "k", "ch"], [], ["a", "o"], []))
            print(graex)
            print(graex.phoneme_inventory.max_grapheme_length)
            print(graex.phoneme_inventory.unique_graphemes)

        case 4:
            #grapheme extractor
            text = input("text = ")
            grapheme = lang.grapheme_extractor._get_grapheme(text)
            print(f"grapheme = {grapheme}")

        case 5:
            #printiqui
            print(repr(lang))
            print(repr(lang.validator))
            print(repr(lang.generator))
            print(repr(lang.grapheme_extractor))
            print(repr(lang.transliterator))

        case 6:
            #transliteration
            print(*lang.transliterator.transliterations)

            syls = [
                Syllable("k", "", "a", ""),
                Syllable("z", "", "a", ""),
                Syllable("ch", "", "i", ""),
                Syllable("sh", "", "a", "")
            ]

            for i in syls:
                print(f"{i.dump()}\t{lang.transliterator.transliterate(i, "cyrillic")}")

        case 7:
            # evals
            syl = Syllable("b", "", "a", "")
            representation = repr(syl)
            print( f"syl={syl}\nrepresentation={representation}\nsyl == eval(representation)={syl == eval(representation)}" )

            tests = [
                Syllable("a'b", "", 'c"d', ""),
                Syllable("a\nb", "", "c\td", ""),
                Syllable("\\", "", "", ""),
                Syllable("日本語", "", "π", ""),
                Syllable("", "", "", ""),
            ]

            for t in tests:
                print(f"{repr(t)} {t == eval(repr(t))}")

        case 8:
            # viejt

            syls = []
            for i in range(0, 20):
                syls.append(lang.random_valid_syllable())

            for i in syls:
                print(f"{i.dump()}\t{lang.transliterator.transliterate(i, "viejt")}")

        case 9:
            # choẩo must not == choooeo but chuooeu
            # TODO: chuoeeru -- no, chuoeeur -- yes
            # is it necessary changing tilde tone as f but not doubling vowel + r as it is now

            syls = [
                Syllable ( initial='ch', medial='o', nucleus='ẩ', coda='o' ),
                Syllable ( initial='ch', medial='o', nucleus='ẫ', coda='o' ),
                Syllable ( initial='gi', medial='i', nucleus='ẫ', coda='y' ),
                Syllable ( initial='m', medial='i', nucleus='ẫ', coda='y' ),
                Syllable ( initial='d', medial='', nucleus='ệ', coda='i' ), # must zeij not zeji
                Syllable ( initial='b', medial='', nucleus='ẵ', coda='t' )
            ]

            for syl in syls:
                print(f"{syl} {lang.transliterator.transliterate(syl, "viejt")}\t{lang.validator.is_valid(syl)}")