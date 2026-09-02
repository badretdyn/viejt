class Syllable:
    def __init__(self, initial = "", medial = '', nucleus = "", coda = ""):
        self.initial = initial
        self.medial = medial
        self.nucleus = nucleus
        self.coda = coda
    
    def __str__(self):
        # coda = self.coda
        # if self.coda and self.coda[0] == "\\":
        #     coda = ""
        return f"Syllable {{ {self.initial}, {self.medial}, {self.nucleus}, {self.coda if not (self.coda and self.coda[0] == "\\") else ""} }}"

    def __repr__(self):
        return f"Syllable {{ {self.initial}, {self.medial}, {self.nucleus}, {self.coda} }}"