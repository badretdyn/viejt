class Syllable:
    def __init__(self, initial = "", medial = '', nucleus = "", coda = ""):
        self.initial = initial
        self.medial = medial
        self.nucleus = nucleus
        self.coda = coda
    
    def __str__(self):
        return f"Syllable {{ {self.initial}, {self.medial}, {self.nucleus}, {self.coda} }}"

    def __repr__(self):
        return self.__str__()