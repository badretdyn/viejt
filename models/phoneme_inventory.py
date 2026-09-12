from models.app_config import AppConfig

class PhonemeInventory:
    def __init__(self, initials, medials, nuclei, codas, app_config = None):
        self.initials = set(initials or [])
        self.medials = set(medials or [])
        self.nuclei = set(nuclei or [])
        self.codas = set(codas or [])
        self._unique_graphemes = None
        self._max_grapheme_length = None
        self.app_config = app_config or AppConfig()

    @property
    def unique_graphemes(self) -> set[str]:
        if self._unique_graphemes is None:
            all_components = self.initials | self.medials | self.nuclei | self.codas
            self._unique_graphemes = { comp for comp in all_components if comp != "" }
        return self._unique_graphemes

    @property
    def max_grapheme_length(self) -> int:
        self.unique_graphemes # to avoid eternal 1 length while unique_graphemes isn't called
        #print(f"pi\tug = {self._unique_graphemes},\n\t\tformula:max({[comp for comp in self._unique_graphemes if not "\\" in comp]})") if self.app_config.debug_mode else False
        if self._max_grapheme_length is None:
            if not self._unique_graphemes:
                self._max_grapheme_length = 1
            else:
                self._max_grapheme_length = max(len(comp) for comp in self._unique_graphemes if not "\\" in comp)
        return self._max_grapheme_length

    def __str__(self, separator = " "):
        return f"PhonemeInventory {{ initials:{self.initials!r},{separator}medials:{self.medials!r},{separator}nuclei:{self.nuclei!r},{separator}codas:{self.codas!r} }}"

    def __repr__(self):
        return self.__str__()