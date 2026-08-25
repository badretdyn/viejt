class LatinFinder:

    @staticmethod
    def get_latin_indexes(graphemes, index_from = 0):
        positions = []
        start = -1
        end = -1
        i = index_from
        while (i < len(graphemes)):
            if str.isalpha(graphemes[i]):
                start = i
                while i < len(graphemes) and str.isalpha(graphemes[i]):
                    end = i
                    i += 1
                positions.append((start, end))
            i += 1

        return positions

    @staticmethod
    def get_word(graphemes, indexes : tuple[int, int]):
        word = []
        for i in range(indexes[0], indexes[1] + 1):
            word.append(graphemes[i])
        return word