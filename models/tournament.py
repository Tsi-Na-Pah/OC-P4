"""Chess Tournament"""
from typing import List
from .chessplayer import ChessPlayer
from .round import Round


class ChessTournament:
    """Chess Tournament"""

    def __init__(self, tournament_name, tournament_location, tournament_date, tournament_round_number, tournament_description, time_controller):
        """Init Chess Player attributes"""
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_date = tournament_date
        self.tournament_round_number = tournament_round_number
        self.tournament_description = tournament_description
        self.time_controller = time_controller

        self.tournament_players: List[ChessPlayer] = []
        self.tournament_rounds: List[Round] = []

    def __str__(self):
        """Used in print."""
        return f"{self.tournament_name} at {self.tournament_location} with {self.tournament_players}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def update_player_score(self, round):
        for match in round.matchs:
            for player in self.tournament_players:
                if player[0] == match.player1[0]:
                    player[1] += match.score1
                if player[0] == match.player2[0]:
                    player[1] += match.score2
