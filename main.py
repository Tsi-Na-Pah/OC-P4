"""Entry point."""

from controllers.base import Controller
from controllers.tournamentsystem import TournamentSystem

from views.playerview import PlayerView

"""

from controllers.evaluate import CheckerRankAndSuitIndex

from views.base import Views
from views.player import PlayerView
from views.broadcast import BroadcastView
from views.internet import InternetStreamingView
"""


def main():

    active_view = PlayerView()
    """passive_views = (active_view, BroadcastView(), InternetStreamingView())
    views = Views(active_view, passive_views)
    """
    tournament_system = TournamentSystem()

    game = Controller(active_view, tournament_system)
    game.run()


if __name__ == "__main__":
    main()
