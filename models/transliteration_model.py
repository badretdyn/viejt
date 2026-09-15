class Transliteration:
    def __init__(self, initials, medials, nuclei, codas, name : str):
        self.initials = initials
        self.medials = medials
        self.nuclei = nuclei
        self.codas = codas
        self.name = name

    def dump(self):
        return f"Transliteration(name={self.name!r}, initials={self.initials!r}, medials={self.medials!r}, nuclei={self.nuclei!r}, codas={self.codas!r})"

    def __repr__(self):
        return f"Transliteration(name={self.name!r})"