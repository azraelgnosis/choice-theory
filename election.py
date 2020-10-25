import pandas as pd
from models import Voter, Candidate

candidates = [Candidate() for _ in range(2)]
voters = [Voter().to_dict() for idx in range(10000)]
# voter_df = pd.DataFrame.from_dict(voters, orient='index', columns=["left_right"])
# voter_df = pd.DataFrame(columns=Voter.__slots__)
voter_df = pd.DataFrame(voters)


voter_df['vote'] = voter_df['left_right'].apply(Voter.vote, args=[candidates])

winner = voter_df['vote'].mode().iloc[0]
mean = voter_df['left_right'].mean()
mean_winner = Voter.vote(mean, candidates)
median = voter_df['left_right'].median()
median_winner = Voter.vote(median, candidates)

assert winner == mean_winner == median_winner

print("done")