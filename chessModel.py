# ------------------------------------------------------- #
# ------------------- CONTROLLER PART ------------------- #
# ------------------------------------------------------- #


serialized_player = {}
serialized_tournament = {}


def is_even(n):
    if n % 2 == 0:
        return int(n)
    else:
        raise ValueError("must be an even")


def input_must_be(var, question):
    while True:
        elem = input(f"{question}: \n")
        try:
            if var == 'str':
                elem = str(elem)
            if var == 'int':
                elem = int(elem)
            if var == 'float':
                elem = float(elem)
            if var == 'even' and is_even(int(elem)):
                elem = int(elem)
        except ValueError:
            print("saisie incorrecte")
            continue
        else:
            return elem


def get_num_player(val, dic):
    for key, value in dic.items():
        for k, v in value.items():
            if val == v:
                return key


def sort_for_pairs(value):
    if value == "rank":
        listed_p = {i.name: i.rank for i in [play for play in tournament.players]}
    elif value == "score":
        listed_p = {i.name: i.score for i in [play for play in tournament.players]}

    return sorted(((value, key) for (key, value) in listed_p.items()), reverse=True)


def update_dic(dic, ask, new):
    part1 = {k: v for k, v in dic.items()}
    part2 = {ask: new}
    part1.update(part2)

    return part1


# ----------------------------------------------------- #
# ------------------- MODEL PART ---------------------- #
# ----------------------------------------------------- #

# Not a lot to say here, I try to make this as dynamic as possible
class Player:
    def __init__(self, name=None):
        self.name = name
        self.score = 0
        self.ever_played = []


class Tournament:
    def __init__(self, name=None):

        self.rounds = []
        self.name = name
        self.ever_played = []

        # Valids informations that user can add/modify in the future

        self.valid_tournament_info = ['name', 'place', 'date', 'description', 'score historic', 'round duration']
        self.valid_player_info = ['name', 'age', 'last name', 'birth date', 'gender', 'rank', 'position in tournament',
                                  'total score']

    def new_tournament(self):

        self.name = input_must_be('str', "Please enter the name of the tournament")
        serialized_tournament["name"] = self.name
        # J'AI CHANGÉ LA FORME DU DIC ICI

    def add_players(self):

        players = []
        num_players = input_must_be('even', "Enter the number of tournament participants (must be even)")

        for i in range(num_players):
            player = Player()
            player.name = input_must_be('str', "Enter the player's name")
            players.append(player)
            serialized_player[f'player{i + 1}'] = {'name': player.name}

        self.players = players

    def new_round(self):

        round = Round()
        round.name = f"round_{round.counter}"
        self.rounds.append(round)
        serialized_tournament["rounds"] = [i.name for i in self.rounds]
        # UPDATE DIC RISQUE D'ÊTRE FORT UTILE


class Round:
    counter = 0

    def __init__(self):
        type(self).counter += 1


class Match:
    def __init__(self):
        pass


# ------------------------------------------------- #
# ------------------- MAIN PART ------------------- #
# ------------------------------------------------- #

tournament = Tournament()
tournament.new_tournament()
tournament.add_players()
tournament.new_round()

