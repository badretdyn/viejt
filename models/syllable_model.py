class Syllable:
    def __init__(self, initial = "", medial = '', nucleus = "", coda = ""):
        self.initial = initial
        self.medial = medial
        self.nucleus = nucleus
        self.coda = coda
    
    def dump(self):
        # coda = self.coda
        # if self.coda and self.coda[0] == "\\":
        #     coda = ""
        return f"Syllable {{ {self.initial}, {self.medial}, {self.nucleus}, {self.coda} }}"

    def __str__(self):
        return f"{self.initial}{self.medial}{self.nucleus}{self.coda}"
    
    def __repr__(self):
        return f"Syllable(initial={self.initial!r}, medial={self.medial!r}, nucleus={self.nucleus!r}, coda={self.coda!r})"