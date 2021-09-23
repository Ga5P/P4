serialized_player = {}
serialized_tournament = {}

def get_num_player(val, dic):
    for key, value in dic.items():
        for k, v in value.items():
            if val == v:
                return key

'''def save_seri(dic):
    dic[get_num_player(p, dic)] = info
    pass'''


class Player:
    def __init__(self, name=None):
        self.name = name

    def enter_infos(self, info):
        valid_infos = ['age', 'last name', 'birth date', 'gender', 'rank', 'position in tournament']

        num_player = input("Enter the player's name :\n")
        if len(tournament.players) >= num_player:
            pass
        else:
            return 'Please enter an number smaller than or equal to the number of challengers '

        # For how many players ?
        # For how many infos ?

        serialized_player[get_num_player(p, serialized_player)] = info
        pass

    def modify_info(self):

        p = input("Which Player?")

        for play in tournament.players:
            for key, value in vars(play).items():

                if p == value:
                    while False: continue

                    if True:
                        print('You can change these informations; ', "\n", key)
                        ask = input("Which info do you want to change?")

                    if key == ask:
                        new = input(f'What is the new {ask} value?')
                        serialized_player[get_num_player(p, serialized_player)] = {ask: new}
                        setattr(play, f'{ask}', new)

                        return f'The {ask} has been successfully changed'

                    else:
                        return "can't find this info"
        else:
            return "Can't find this player"


class Tournament:
    def __init__(self, name=None):
        self.name = name

    def add_players(self):
        players = []

        num_players = int(input("Enter the number of tournament participants: "))

        for i in range(num_players):
            player = Player()
            player.name = input("Enter the player's name :\n")
            players.append(player)
            serialized_player[f'player{i + 1}'] = {'name': player.name}

        self.players = players


# ------------------------------------------------------------------- #
# ------------------- WILL BE IN THE VIEW PART ---------------------- #
# ------------------------------------------------------------------- #

tournament = Tournament()
tournament.add_players()

player = Player()
player.modify_info()