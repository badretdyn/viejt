class Syllable:
    def __init__(self, initial = "", medial = '', core = "", coda = "", tone = 0):
        self.initial = initial
        self.medial = medial
        self.core = core
        self.coda = coda
        self.tone = tone
    
    def __str__(self):
        return f"Syllable {{ {self.initial}, {self.medial}, {self.core}, {self.coda}, {self.tone} }}"

    def __repr__(self):
        return self.__str__()