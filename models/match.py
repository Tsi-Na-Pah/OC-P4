"""Define the chess match results"""

class Match:
    """Match class.
    A match is between 2 chess players
    Match score: 1 player wins (1 point) and A player looses (0 point) or a draw (0.5 point for each player)
    """

    def __init__(self, player1, score1, player2, score2):
        """Init the match"""
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

        self.match_result = ([player1, score1], [player2, score2])

    def __str__(self):
        """Used in print."""
        return f"{self.player1} {self.score1} - {self.score2} {self.player2}"

    def __repr__(self):
        """Used in print."""
        return str(self)
