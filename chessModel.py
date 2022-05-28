# ------------------------------------------------------- #
# ------------------- CONTROLLER PART ------------------- #
# ------------------------------------------------------- #
import random, operator

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


'''def sort_for_pairs(value):
    if value == "rank":
        listed_p = {i.name: i.rank for i in [play for play in tournament.players]}
    elif value == "score":
        listed_p = {i.name: i.score for i in [play for play in tournament.players]}

    return sorted(((value, key) for (key, value) in listed_p.items()), reverse=True)'''


def sort_for_pairs(value):
    if value == "rank":
        tournament.players.sort(key=operator.attrgetter('rank'))
    elif value == "score":
        tournament.players.sort(key=operator.attrgetter('score'))

    return list(reversed(tournament.players))


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

    # *-------------*------------*------------*------------*------------*------------*------------*------------*------------*

    def generate_pairs(self):
        if len(tournament.rounds) == 1:

            ask = input_must_be('str', 'Does players are already ranked ? /n yes or no ?')

            if ask == 'no':
                p = random.sample(tournament.players, len(tournament.players))
                #return [tuple(p[x:x + 2]) for x in range(0, len(p), 2)]
                pairs = [tuple(p[x:x + 2]) for x in range(0, len(p), 2)]
                for pair in pairs:
                    pair[0].ever_played.append(pair[1])
                    pair[1].ever_played.append(pair[0])
                return pairs

            if ask == 'yes':
                for play in tournament.players:
                    play.rank = input_must_be('int', f"What's {play.name} rank ?")

                    # num = get_num_player(play.name, serialized_player)
                    # serialized_player[num] = update_dic(serialized_player[num], 'rank', play.rank)

                sorted_p = sort_for_pairs('rank')

                part1 = [p for p in list(sorted_p)[:int(len(sorted_p) / 2)]]
                part2 = [p for p in list(sorted_p)[int(len(sorted_p) / 2):]]

                #return [(part1[i], part2[i]) for i in range(len(part1))]
                pairs = [(part1[i], part2[i]) for i in range(len(part1))]
                for pair in pairs:
                    pair[0].ever_played.append(pair[1])
                    pair[1].ever_played.append(pair[0])
                return pairs

        else:
            '''try:
                if [play.rank for play in tournament.players]:

                    a_list = [t.score for t in sort_for_pairs('score')]
                    if any(a_list.count(element) > 1 for element in a_list) is True:

                        sorted_p = sort_for_pairs("rank")
                    else:
                        sorted_p = sort_for_pairs("score")

            except AttributeError:
                sorted_p = sort_for_pairs("score")
            pairs = []'''
            sorted_p = sort_for_pairs("score")
            pairs = []
            for i, play in enumerate(sorted_p):
                p = 1
                while len(pairs) <= 4:
                #while True:
                    try:
                        p2 = sorted_p[i + p]
                    except IndexError:
                        p += 1
                        p2 = sorted_p[i % + p]

                    if p2 in play.ever_played or p2 == play:
                        p += 1
                    elif any(play in i for i in pairs) or any(p2 in i for i in pairs):
                        break

                    else:
                        pairs.append((play, p2))
                        play.ever_played.append(p2)
                        p2.ever_played.append(play)
                        break

                for pair in pairs:
                    print("------------------------")# Mémo
                    print(pair[0].name, pair[1].name)
                    print("------------------------")

            return pairs

# *-------------*------------*------------*------------*------------*------------*------------*------------*------------*


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
try_0 = tournament.generate_pairs()
