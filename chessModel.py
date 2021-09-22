serialized_player = {}
serialized_tournament = {}


class Player:
    def __init__(self, name=None):
        self.name = name

    def enter_infos(self):
        pass

    def modify_infos(self):

        p = input("Which Player?")

        for player in tournament.players:
            for key, value in vars(player).items():

                while p == value:
                    print('You can change these informations; ', key, "\n")
                    ask = input("Which info do you want to change?")

                    if key == ask:

                        setattr(player, f'{ask}', input(f'What is the new {ask} value?'))
                        print(f'The {ask} has been successfully changed ')
                        return
                else:
                    print("Can't find this player")
                    break
            break

class Tournament:
    def __init__(self, name=None):
        self.name = name

    def add_player(self):
        players = []

        num_players = int(input("Enter the number of tournament participants: "))

        for i in range(num_players):
            player = Player()
            player.name = input("Enter the player's name :\n")

            players.append(player)

        self.players = players


# ------------------------------------------------------------------- #
# ------------------- WILL BE IN THE VIEW PART ---------------------- #
# ------------------------------------------------------------------- #

tournament = Tournament()
tournament.add_player()

player = Player()
player.modify_infos()
