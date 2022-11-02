
class Consult:

    def __init__(self, *terms):
        self.terms = terms

    def __str__(self) -> str:
        return ", ".join(self.terms)
