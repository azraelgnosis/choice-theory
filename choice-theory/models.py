from lorekeeper import Model
from math import sqrt
import random

class Voter(Model):
    __slots__ = ['name', 'ethos']

    def __init__(self, name:str=None, ethos:dict=dict()):
        self.name = name or self._generate_name()
        self.ethos = ethos or self._generate_ethos()

    def vote(self, candidates):
        opinions = {candidate.name: self.accord(candidate) for candidate in candidates}
        ranked_choice = sorted(opinions.keys(), key=lambda x: opinions[x])

        return ranked_choice

    def accord(self, candidate):
        keys = self.ethos.keys() & candidate.ethos.keys()
        voter_vals = [self.ethos[key] for key in keys]
        candidate_vals = [candidate.ethos[key] for key in keys]

        accord = self.euclidean_distance(voter_vals, candidate_vals)
        return accord

    @staticmethod
    def euclidean_distance(valsA:list, valsB:list) -> float:
        assert len(valsA) == len(valsB)

        dims = len(valsA)

        return sqrt(sum([pow(valsA[dim] - valsB[dim], 2) for dim in range(dims)]))

    @staticmethod
    def _generate_name():
        """Returns a randomly generated name composed of 2 or 3 CV syllables."""

        letters = [chr(idx) for idx in range(97, 97+26)]
        vowels = ('a', 'e', 'i', 'o', 'u')
        consonants = [char for char in letters if char not in vowels] # set(letters) - set(vowels)

        name = "".join([random.choice(consonants) + random.choice(vowels) for _ in range(random.randint(2, 4))])

        return name

    @staticmethod
    def _generate_ethos(dims=1):
        """Returns a dict of whose keys are randomly generated values between -10 and 10"""

        ethos = {idx: random.uniform(-10, 10) for idx in range(dims)}

        return ethos

    def __repr__(self): return f"{self.name} " + ", ".join([f"{key}: {round(val, 2)}" for key, val in self.ethos.items()])
