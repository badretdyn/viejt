class Transliteration:
    def __init__(self, initials : tuple[str, str], medials : tuple[str, str], nuclei : tuple[str, str], codas : tuple[str, str], name : str):
        self.initials = initials
        self.medials = medials
        self.nuclei = nuclei
        self.codas = codas
        self.name = name