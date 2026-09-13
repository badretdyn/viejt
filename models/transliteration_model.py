class Transliteration:
    def __init__(self, initials, medials, nuclei, codas, name : str):
        self.initials = initials
        self.medials = medials
        self.nuclei = nuclei
        self.codas = codas
        self.name = name

    def __str__(self):
        return f"Transliteration {{ name: {self.name}, initials: {self.initials}, initials: {self.medials}, initials: {self.nuclei}, initials: {self.codas} }}"

    def __repr__(self):
        return self.__str__()