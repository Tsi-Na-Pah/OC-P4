"""Define the tournament system : swiss..."""

from .base import TOURNAMENT_PLAYER_NUMBER
from models.match import Match

class TournamentSystem:
    """Define the chess matches between chess players for the different tournament rounds
    according to different systems like the swiss system"""

    def swiss_system(self, players_score, round_number):
        """Defines the chess matches for one round using the Swiss system """
        players_score.sort(key=lambda players_score: players_score[0].rank)
        players_score.sort(key=lambda players_score: players_score[1], reverse=True)
        matchs = []

        if round_number == 1:
            matchs.append(Match(players_score[0], 0, players_score[4], 0))
            matchs.append(Match(players_score[1], 0, players_score[5], 0))
            matchs.append(Match(players_score[2], 0, players_score[6], 0))
            matchs.append(Match(players_score[3], 0, players_score[7], 0))
        else:
            matchs.append(Match(players_score[0], 0, players_score[1], 0))
            matchs.append(Match(players_score[2], 0, players_score[3], 0))
            matchs.append(Match(players_score[4], 0, players_score[5], 0))
            matchs.append(Match(players_score[6], 0, players_score[7], 0))

        return matchs
