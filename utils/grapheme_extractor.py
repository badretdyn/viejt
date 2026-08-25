from data.viet_syl import *

class GraphemeExtractor:

    @staticmethod
    def _get_viet_grapheme(text):
        trigraph = ""
        digraph = ""
        
        try:
            trigraph = text[0] + text[1] + text[2]
            if trigraph in VIETNAMESE_INITIALS:
                return trigraph
        except Exception as e:
            e

        try:    
            digraph = text[0] + text[1]
            if digraph in VIETNAMESE_INITIALS or digraph in VIETNAMESE_CORES:
                return digraph
        except Exception as e:
            e

        if text[0] in VIETNAMESE_INITIALS or text[0] in VIETNAMESE_CORES:
            return text[0]

        return ""

    @staticmethod
    def get_graphemes(text, index_from = 0):
        graphemes = []

        i = index_from
        while i < len(text):

            raw = text[i:i+3]
            grapheme = GraphemeExtractor._get_viet_grapheme(raw)
            if grapheme == "":
                 grapheme = text[i]
            
            graphemes.append(grapheme)

            match len(grapheme):
                case 3:
                    i += 2
                case 2:
                    i += 1
            i += 1
        
        return graphemes
