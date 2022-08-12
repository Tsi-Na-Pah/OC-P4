"""Define a Round of a chess tournament."""

from typing import Optional
import random

from .match import Match
from typing import List

class Round:
    """Round of a chess tournament."""

    def __init__(self,round_name, start_datetime, end_datetime):
        """Init Round attributes
        Round matches will be automatically generated when the tournament starts"""
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.round_over = False

        self.matchs: List[Match] = []

    def __str__(self):
        """Used in print."""
        return f"{self.round_name} started at {self.start_datetime} : {self.matchs}"

    def __repr__(self):
        """Used in print."""
        return str(self)

