"""Base view."""
#from dateutil.parser import parse

gender_list = ['M', 'F']


class PlayerView:
    """Player view."""

    def prompt_for_player(self):
        """Prompt for a chess player information"""
        lastname = input("Chess player last name: ")
        if not lastname:
            return None
        firstname = input("Chess player first name: ")
        if not firstname:
            return None
        birthdate = input("Chess player birth date: ")
        if not birthdate:
            return None
        gender = input("Chess player gender (M or F): ")
        if not gender or gender not in gender_list:
            print('M or F')
            return None
        rank = input("Chess player rank: ")
        if not rank or not rank.isdigit():
            print('Not a number')
            return None

        player_info = {
            "LastName": lastname,
            "FirstName": firstname,
            "BirthDate": birthdate,
            "Gender": gender,
            "Rank": rank
        }

        return player_info

    def show_list_all_players(self, players, sort_order="Alphabetical"):
        """List all the chess players"""
        if sort_order == 'Rank':
            players.sort(key=lambda players: players.rank)
        else:
            players.sort(key=lambda players: (players.lastname, players.firstname))
        print("List all the players in " + sort_order + " order:")
        i = 1
        for player in players:
            print(f"Chess Player #{i}: " + player.firstname + " " + player.lastname + " - rank #" + str(player.rank))

    def prompt_for_flip_cards(self):
        """Request to return the cards."""
        print()
        input("Prêt à retourner les cartes ?")
        return True

    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire une partie ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True
