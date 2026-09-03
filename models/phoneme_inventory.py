class PhonemeInventory:
    def __init__(self, initials, medials, nuclei, codas):
        self.initials = set(initials or [])
        self.medials = set(medials or [])
        self.nuclei = set(nuclei or [])
        self.codas = set(codas or [])
        self._unique_graphemes = None
        self._max_grapheme_length = None

    @property
    def unique_graphemes(self) -> set[str]:
        if self._unique_graphemes is None:
            all_components = self.initials | self.medials | self.nuclei | self.codas
            self._unique_graphemes = { comp for comp in all_components if comp != "" }
        return self._unique_graphemes

    @property
    def max_grapheme_length(self) -> int:
        self.unique_graphemes # to avoid eternal 1 length while unique_graphemes isn't called
        if self._max_grapheme_length is None:
            if not self._unique_graphemes:
                self._max_grapheme_length = 1
            else:
                self._max_grapheme_length = max(len(comp) for comp in self._unique_graphemes)
        return self._max_grapheme_length

    def __str__(self, separator = " "):
        return f"PhonemeInventory {{ initials:{self.initials!r},{separator}medials:{self.medials!r},{separator}nuclei:{self.nuclei!r},{separator}codas:{self.codas!r} }}"

    def __repr__(self):
        return self.__str__()