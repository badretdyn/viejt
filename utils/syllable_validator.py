from data.viet_syl import *
from models.syllable_model import *
from utils.grapheme_extractor import GraphemeExtractor
from utils.latin_finder import LatinFinder
from utils.case_mask import CaseMask

class SyllableValidator:
    @staticmethod
    def define_syllable(graphems : list):

        initial = ""
        medial = ""
        nucleus = ""
        coda = ""
        
        if len(graphems) == 4:
            initial = graphems[0] if graphems[0] in VIETNAMESE_INITIALS else ""
            medial = graphems[1] if graphems[1] in VIETNAMESE_MEDIALS else ""
            nucleus = graphems[2] if graphems[2] in VIETNAMESE_CORES else ""
            coda = graphems[3] if graphems[3] in VIETNAMESE_CODAS else ""
        elif len(graphems) == 3:
            if graphems[0] in VIETNAMESE_INITIALS and graphems[2] in VIETNAMESE_CODAS:
                initial = graphems[0]
                nucleus = graphems[1] if graphems[1] in VIETNAMESE_CORES else ""
                coda = graphems[2]
            elif graphems[0] in VIETNAMESE_INITIALS and graphems[2] in VIETNAMESE_CORES:
                initial = graphems[0]
                medial = graphems[1] if graphems[1] in VIETNAMESE_MEDIALS else ""
                nucleus = graphems[2]
            elif graphems[0] in VIETNAMESE_MEDIALS and graphems[2] in VIETNAMESE_CODAS:
                medial = graphems[0]
                nucleus = graphems[1] if graphems[1] in VIETNAMESE_CORES else ""
                coda = graphems[2]
        elif len(graphems) == 2:
            if graphems[0] in VIETNAMESE_INITIALS:
                initial = graphems[0] if graphems[0] in VIETNAMESE_INITIALS else ""
                nucleus = graphems[1] if graphems[1] in VIETNAMESE_CORES else ""
            elif graphems[0] in VIETNAMESE_MEDIALS and graphems[1] in VIETNAMESE_CORES:
                medial = graphems[0]
                nucleus = graphems[1]
            elif graphems[0] in VIETNAMESE_CORES and graphems[1] in VIETNAMESE_CODAS:
                nucleus = graphems[0]
                coda = graphems[1]
        elif len(graphems) == 1:
            nucleus = graphems[0]

        syl = Syllable(initial, medial, nucleus, coda)

        return syl

    @staticmethod
    def extract_syllables(text : str):
        syls = []
        #mask = CaseMask.get_uppercase_mask(text)
        text_lowered = str.lower(text)
        graphemes = GraphemeExtractor.get_graphemes(text_lowered, 0)
        latin_indexes = LatinFinder.get_latin_indexes(graphemes)
        #words = []
        for i in latin_indexes:
            word = LatinFinder.get_word(graphemes, i)
            #words.append(word)
            syl = SyllableValidator.define_syllable(word)
            if syl.core != "":
                syls.append(syl)
        return syls