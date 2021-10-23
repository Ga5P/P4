import random

valid_tournament_info = ['name', 'place', 'date', 'description', 'score historic', 'round duration']
valid_player_info = ['name', 'age', 'last name', 'birth date', 'gender', 'rank', 'position in tournament']

serialized_player = {}
serialized_tournament = {}


def varname(instance):
    if instance == tournament:
        name = 'tournament'
        return name

    else:
        try:
            iter(instance)
            if instance == tournament.players:
                name = 'players'
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
        return [i for i in dir(tournament) if i in valid_tournament_info]

def update_dic(dic, ask, new):
    part1 = {k: v for k, v in dic.items()}
    part2 = {ask: new}
    part1.update(part2)

    return part1

# ----------------------------------------------------- #
# ------------------- MODEL PART ---------------------- #
# ----------------------------------------------------- #

class Player:
    def __init__(self, name=None):
        self.name = name

    # def enter_infos(self, info):

    # num_player = input("Enter the player's name :\n")
    # if len(tournament.players) >= num_player:
    # pass
    # else:
    # return 'Please enter an number smaller than or equal to the number of challengers '

    # For how many players ?
    # For how many infos ?

    # serialized_player[get_num_player(p, serialized_player)] = info
    # pass


class Tournament:
    def __init__(self, name=None):
        self.name = name

    def new_tournament(self):

        dates = []

        tournament.name = str(input("Please enter the name of the tournament: \n"))
        serialized_tournament[tournament.name] = {'name': tournament.name}

        return tournament

    def add_players(self):
        players = []

        num_players = int(input("Enter the number of tournament participants: "))

        for i in range(num_players):
            player = Player()
            player.name = input("Enter the player's name :\n")
            players.append(player)
            serialized_player[f'player{i + 1}'] = {'name': player.name}

        self.players = players

    def new_round(self):
        try:
            if tournament.rounds:
                rounds = tournament.rounds
        except AttributeError:
            rounds = []

        round = Round()
        round.name = f"round_{Round.counter + 1}"
        rounds.append(round)

        self.rounds = rounds
        Round.counter += 1

        pairs = round.generate_random_pairs()
        return pairs

    def modify_infos(self, obj):

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
                        if ask == 'name':
                            new = input(f'What is the new {ask} for {p}?')

                            serialized_tournament[new] = serialized_tournament.pop(tournament.name)
                            tournament.name = new
                            serialized_tournament[tournament.name] = update_dic(serialized_tournament[tournament.name], ask, new)

                        if ask == key:
                            new = input(f'What is the new {ask} for {p}?')
                            serialized_tournament[tournament.name] = {ask: new}
                            setattr(obj, f'{ask}', new)
                            print(f'The {ask} has been successfully changed')
                            break

    def add_infos(self, obj):
        instance = varname(obj)

        if instance == 'players':

            for play in tournament.players:
                valid = [k for k in valid_player_info if
                         k and k.replace(' ', '_') not in current_attributes(tournament.players)]

            print('The list of informations you can add', valid)
            ask = input("Which info do you want to add ?")

            for play in tournament.players:

                if not valid:
                    print(f"You can't add another information for {instance}")
                    return
                else:
                    for i in valid:
                        if i == ask:
                            new = input(f'What is the {ask} of {play.name} ?')
                            num = get_num_player(play.name, serialized_player)
                            serialized_player[num] = update_dic(serialized_player[num], ask, new)

                            asko = ask.replace(' ', '_')
                            setattr(play, f'{asko}', new)

        elif instance == 'tournament':
            valid = [i for i in valid_tournament_info if i not in current_attributes(obj)]
            if not valid:
                print(f"You can't add another information for this {instance}")
                return
            else:
                print('The list of informations you can add', valid)
                ask = input("Which info do you want to add ?")
                for i in valid:
                    if i == ask:
                        new = input(f'What is the {ask} of the {instance} ?')
                        serialized_tournament[tournament.name] = update_dic(serialized_tournament[tournament.name], ask, new)

                        asko = ask.replace(' ', '_')
                        setattr(obj, f'{asko}', new)





class Round:
    counter = 0

    def __init__(self):
        pass

    # Chaque paire fait un match

    def new_match(self, pairs):
        matchs = []
        iter = 0

        for pair in pairs:
            match = Match()
            match.paired_players = pair
            match.name = f"match_{iter + 1}"
            matchs.append(match)

            iter += 1

        self.matchs = matchs

    def generate_random_pairs(self):

        p = random.sample(tournament.players, len(tournament.players))
        pairs = [tuple(p[x:x + 2]) for x in range(0, len(p), 2)]

        print('--------------------------------------------------------')
        print(pairs[0][0].name, " will fight against ", pairs[0][1].name)
        print(pairs[1][0].name, " will fight against ", pairs[1][1].name)

        return pairs

    def generate_pairs(self):


        ask = input('Does players are already ranked ? /n yes or no ?')

        if ask == 'yes':
            for play in tournament.players:
                play.rank = int(input(f"What's {play.name} rank ?"))

                num = get_num_player(play.name, serialized_player)
                serialized_player[num] = update_dic(serialized_player[num], 'rank', play.rank)

        pass    


class Match:

    def __init__(self):
        pass


# ------------------------------------------------------------------ #
# ------------------- WILL BE IN THE VIEW PART --------------------- #
# ------------------ FROM NOW, IT'S THE TEST PART ------------------ #
# ------------------------------------------------------------------ #


tournament = Tournament()
tournament.new_tournament()
tournament.add_players()

# tournament.modify_infos(tournament.players)
# tournament.modify_infos(tournament)

# tournament.add_infos(tournament)
# tournament.add_infos(tournament.players)

# tournament.new_round()

# round = Round()
# round.new_match(tournament.new_round())
