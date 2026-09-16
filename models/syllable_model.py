class Syllable:
    def __init__(self, initial="", medial="", nucleus="", coda=""):
        self.initial = initial
        self.medial = medial
        self.nucleus = nucleus
        self.coda = coda
    
    def dump(self):
        # TODO: hiding special character in coda
        # coda = self.coda
        # if self.coda and self.coda[0] == "\\":
        #     coda = ""
        return f"Syllable ( initial={self.initial!r}, medial={self.medial!r}, nucleus={self.nucleus!r}, coda={self.coda!r} )"

    def __eq__(self, other):
        if not isinstance(other, Syllable):
            return NotImplemented
        return (
            (self.initial, self.medial, self.nucleus, self.coda)
            == (other.initial, other.medial, other.nucleus, other.coda)
        )

    # instance of class is mutable, do not put in dict as key
    def __hash__(self):
        return hash((self.initial, self.medial, self.nucleus, self.coda))

    def __str__(self):
        return f"{self.initial}{self.medial}{self.nucleus}{self.coda}"

    def __repr__(self):
        return self.dump()