"""Define the main controller."""
from models.chessplayer import ChessPlayer
from models.match import Match
from models.round import Round
from models.tournament import ChessTournament

from typing import List
import random
import datetime

TOURNAMENT_ROUND_NUMBER = 4
TOURNAMENT_PLAYER_NUMBER = 8
TOURNAMENT_TIME_CONTROLLER = ["Blitz", "Bullet", "Quick Shot"]
MATCH_SCORE = [(1, 0), (0.5, 0.5), (0, 1)]

class Controller:
    """Main controller."""

    def __init__(self, view, tournament_system_swiss):
        """Has a deck, a list of players and a view."""
        # models
        self.players: List[ChessPlayer] = []

        # views
        self.view = view

        # check strategy
        self.tournament_system_swiss = tournament_system_swiss

    def get_new_players(self):
        player_info = self.view.prompt_for_player()
        if not player_info:
            return
        chess_player = ChessPlayer(player_info["LastName"],
                                   player_info["FirstName"],
                                   player_info["BirthDate"],
                                   player_info["Gender"],
                                   int(player_info["Rank"]))
        self.players.append(chess_player)

    def initiate_new_tournament(self):
        tournament_info = {
            "TournamentName": "Paris Chess Masters",
            "TournamentLocation":  "Paris Bercy",
            "TournamentDate": "10/08/2022",
            "TournamentRoundNumber": TOURNAMENT_ROUND_NUMBER,
            "TournamentDescription": "Awesome chess tournament in Paris",
            "TournamentTimeController": TOURNAMENT_TIME_CONTROLLER[0]
        }
        chess_tournament = ChessTournament(tournament_info["TournamentName"],
                                           tournament_info["TournamentLocation"],
                                           tournament_info["TournamentDate"],
                                           tournament_info["TournamentRoundNumber"],
                                           tournament_info["TournamentDescription"],
                                           tournament_info["TournamentTimeController"])

        return chess_tournament

    def select_players(self,chess_tournament, players):
        number_selected = 0
        player_score_initial_score = 0
        for player in players:
            if number_selected < TOURNAMENT_PLAYER_NUMBER:
                chess_tournament.tournament_players.append([player, player_score_initial_score])
                number_selected += 1
            else:
                return
        print("Number of selected players:" + str(len(chess_tournament.tournament_players)))
        return

    def get_match_results(self, round):
        for match in round.matchs:
                random.shuffle(MATCH_SCORE)
                match.score1 = float(MATCH_SCORE[0][0])
                match.score2 = float(MATCH_SCORE[0][1])
        return

    def evaluate_game(self):
        """Evaluate the game."""
        return self.checker_strategy.check(self.players)

    def rebuild_deck(self):
        """Rebuild the deck."""
        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_face_up = False
                self.deck.append(card)
        self.deck.shuffle()

    def start_game(self):
        """Shuffle the deck and makes the players draw a card."""
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def run(self):

        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(ranks)

        self.players.append(ChessPlayer("Doe1", "John", "01/01/2000", "M", ranks[0]))
        self.players.append(ChessPlayer("Doe2", "John", "01/01/2000", "M", ranks[1]))
        self.players.append(ChessPlayer("Doe3", "John", "01/01/2000", "M", ranks[2]))
        self.players.append(ChessPlayer("Doe4", "John", "01/01/2000", "M", ranks[3]))
        self.players.append(ChessPlayer("Doe1", "Jane", "01/01/2000", "F", ranks[4]))
        self.players.append(ChessPlayer("Doe6", "Jane", "01/01/2000", "F", ranks[5]))
        self.players.append(ChessPlayer("Doe7", "Jane", "01/01/2000", "F", ranks[6]))
        self.players.append(ChessPlayer("Doe8", "Jane", "01/01/2000", "F", ranks[7]))
        #only 7 players, one is missing

        #we need at least 8 players
        """while len(self.players) < TOURNAMENT_PLAYER_NUMBER:
            self.get_new_players()"""

        self.view.show_list_all_players(self.players)
        self.view.show_list_all_players(self.players, "Rank")

        chess_tournament = self.initiate_new_tournament()
        random.shuffle(self.players)
        self.select_players(chess_tournament, self.players)


        for round_number in range(TOURNAMENT_ROUND_NUMBER):
            round = Round("Round" + str(round_number + 1), datetime.datetime.today(), None)
            generated_matchs = self.tournament_system_swiss.swiss_system(chess_tournament.tournament_players,
                                                                         round_number + 1)
            for match in generated_matchs:
                round.matchs.append(match)

            self.get_match_results(round)
            round.end_datetime = datetime.datetime.today()
            round.round_over = True

            chess_tournament.update_player_score(round)
            chess_tournament.tournament_rounds.append(round)

            print(round)

        chess_tournament.tournament_players.sort(key=lambda tournament_players: tournament_players[0].rank)
        chess_tournament.tournament_players.sort(key=lambda tournament_players: tournament_players[1], reverse=True)

        print(chess_tournament.__dict__)

        """running = True
        while running:
            self.start_game()

            for player in self.players:
                self.view.show_player_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()

            for player in self.players:
                for card in player.hand:
                    card.is_face_up = True
                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())

            running = self.view.prompt_for_new_game()
            self.rebuild_deck()"""
