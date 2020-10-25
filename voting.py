from collections import defaultdict

class Poll:
    def __init__(self, choices=None, mutable=True):
        self.mutable = mutable # determines whether new choices can be added
        self.choices = defaultdict(int)
        self.num_votes = 0 # keeps track of the number of votes submitted

        if choices:
            for choice in self.choices:
                self.choices[choice] = 0

            self.valid_choices = choices
    
    def result(self):
        plurality = max(self.choices.values())

        self.winner = [choice for choice, votes in self.choices.items() if votes == plurality]

        return self.winner

    def __repr__(self):
        return self.choices
        

class FPTP(Poll):
    def vote(self, choice):
        self.choices[choice] += 1

    def __repr__(self):
        return self.choices

class Approval(Poll):
    def vote(self, choices):
        for choice in choices:
            self.choices[choice] += 1

class IRV(Poll):
    '''
    Instant-Runoff Vote, Alternative Vote, Preferential Voting, or Ranked-Choice Vote (RCV)


    '''

    def __init__(self, choices=None, mutable=True):
        super().__init__(choices, mutable)

        self.ballots = []
        self.losers = []

    def vote(self, vote:dict):
        self.num_votes += 1
        self.ballots.append(vote)
    
    def result(self, ballots, losers=[]):
        self.choices = defaultdict(int)

        for ballot in ballots:
            i = 0
            while ballot[i] in losers:
                i += 1
            self.choices[ballot[i]] += 1

        winner = max(self.choices, key=self.choices.get)

        if self.choices.get(winner) / self.num_votes >= 0.5:
            return winner

        loser = min(self.choices, key=self.choices.get)
        losers.append(loser)

        return self.result(ballots, losers)


def elect(poll, election):
    for vote in election:
        poll.vote(vote)

'''
poll = FPTP()

election = {
    'Lion': 3,
    'Koala': 2,
    'Llama': 5,
    'Penguin': 4,
    'Yak': 5,
}

elect(poll, election)

print(poll.result())
'''
# ------------------------------------------------------
'''
poll = FPTP(poll.result())
election = {
    'Llama': 10,
    'Yak': 9
}

elect(poll, election)

print(poll.result())
'''
# ------------------------------------------------------
'''
poll = Approval()

election = {
    'a': ['Steak Shack', 'Burger Barn'],
    'b': ['Steak Shack', 'Burger Barn'],
    'c': ['Burger Barn'],
    'd': ['Burger Barn', 'Veggie Villa'],
    'e': ['Burger Barn', 'Veggie Villa'],
    'f': ['Burger Barn', 'Veggie Villa'],
}

['Steak Shack',]

elect(poll, election)
print(poll.result())
'''
# ------------------------------------------------------

poll = IRV()
election = [
    ['Turtle', 'Owl'],
    ['Owl', 'Leopard'],
    ['Leopard', 'Turtle'],
    ['Owl', 'Turtle', 'Leopard'],
    ['Leopard', 'Owl', 'Turtle']
]

elect(poll, election)
print(poll.result(poll.ballots))