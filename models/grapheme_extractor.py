class GraphemeExtractor:
    def __init__(self, phoneme_inventory):
        self.phoneme_inventory = phoneme_inventory

    def _get_grapheme(self, text : str):
        max_grapheme_length = self.phoneme_inventory.max_grapheme_length

        pass

    def __str__(self):
        return f"GraphemeExtractor {{ phoneme_inventory:{self.phoneme_inventory} }}"

    def __repr__(self):
        return self.__str__()