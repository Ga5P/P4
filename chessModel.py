valid_tournament_info = ['name', 'place', 'date', 'players', 'description', 'score historic', 'round duration']
valid_player_info = ['name', 'age', 'last name', 'birth date', 'gender', 'rank', 'position in tournament']


serialized_player = {}
serialized_tournament = {}

def varname(instance):
    try:
        iter(instance)
        if instance == tournament.players:
            name = 'players'
        #elif instance == tournament.score_historic:
            #name = 'score historic'
        return name
    except TypeError:
        for name in globals():
            if eval(name) == instance:
                return name
def get_num_player(val, dic):
    for key, value in dic.items():
        for k, v in value.items():
            if val == v:
                return key
def current_attributes(obj):
    try:
        iter(obj)
        for i in obj:
                return [k for k in vars(i).keys()]
    except TypeError:
        return [i for i in dir(obj) if i in f'valid_{obj}_info']

# ----------------------------------------------------- #
# ------------------- MODEL PART ---------------------- #
# ----------------------------------------------------- #

class Player:
    def __init__(self, name=None):
        self.name = name

    def enter_infos(self, info):


        num_player = input("Enter the player's name :\n")
        if len(tournament.players) >= num_player:
            pass
        else:
            return 'Please enter an number smaller than or equal to the number of challengers '

        # For how many players ?
        # For how many infos ?

        serialized_player[get_num_player(p, serialized_player)] = info
        pass

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

    def modif_infos(self, obj):

        instance = varname(obj)
        modif = int(input(f'How many {instance} would you modify ?'))
        modifs = []

        if obj == tournament.players:
            if modif > 1:
                iter = [i + 1 for i in range(modif)]
                for it in iter:
                    p = input(f"Which {instance} ?")
                    print(f'({iter[-1] - it} remaining)')
                    modifs.append(p)
            elif modif == 1:
                print(f"choose one in the list {[i.name for i in obj]}")
                p = input(f"Which {instance} ?")
                modifs.append(p)
        else:
            if modif == 1:
                print(f"choose one in the list {obj.name}")
                p = input(f"Which {instance} ?")
                modifs.append(p)

        valid = [i for i in current_attributes(obj) if i in valid_player_info or valid_tournament_info]
        print('All the information you can change :', valid)
        ask = input("Which info do you want to change ?")
        for p in modifs:
            if obj == tournament.players:
                for play in tournament.players:
                    for key, value in vars(play).items():

                        while p == value:
                            if ask == key:
                                new = input(f'What is the new {ask} for {p}?')
                                serialized_player[get_num_player(p, serialized_player)] = {ask: new}
                                setattr(play, f'{ask}', new)
                                print(f'The {ask} has been successfully changed')
                                break
            else:
                iter = {k: v for k, v in vars(obj).items() if k != 'players'}
                for key, value in iter.items():
                    print(key, '====>', value)
                    while p == value:
                        print(p)
                        if ask == key:
                            new = input(f'What is the new {ask} for {p}?')
                            # serialized_player[get_num_player(p, serialized_player)] = {ask: new}
                            setattr(obj, f'{ask}', new)
                            print(f'The {ask} has been successfully changed')
                            break


# ------------------------------------------------------------------- #
# ------------------- WILL BE IN THE VIEW PART ---------------------- #
# ------------------------------------------------------------------- #

tournament = Tournament()
tournament.add_players()
tournament.modif_infos(tournament.players)