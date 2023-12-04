# Better
class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self._relatives = None

    @property
    def relatives(self):
        if self._relatives is None:
            self._relatives = 'Larissa'  # Get all relatives
        return self._relatives


pessoa = Person('Bruno', 'analista')
print(pessoa.relatives)
