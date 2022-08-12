"""Chess Player"""

class ChessPlayer:
    """Player."""

    def __init__(self, lastname, firstname, birthdate, gender, rank):
        """Init Chess Player attributes"""
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank

    def update_rank(self, new_rank):
        self.rank = new_rank

    def __str__(self):
        """Used in print."""
        return f"{self.firstname} {self.lastname} #{self.rank} "

    def __repr__(self):
        """Used in print."""
        return str(self)