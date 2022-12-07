with open("day02.txt") as day_02_data:
    data = day_02_data.readlines()
    playbook = [str.rstrip("\n").split(" ") for str in data]

# A for Rock, B for Paper, and C for Scissors
# X to lose, Y to draw, and Z to win
# 0 for loss, 3 for draw, and 6 for win
# A beats C, B beats A, and C beats B

rps_rules = {"A": "C", "B": "A", "C": "B"}

def rps_shape_score(shape):
    shape_score = 0
    if shape == "A":
        shape_score += 1
    elif shape == "B":
        shape_score += 2
    elif shape == "C":
        shape_score += 3
    else:
        print("Not a valid shape")
    return shape_score

def my_plays(rules, plays):
    my_play_list = []
    for play in plays:
        if play[1] == "Y":
            my_play_list.append(play[0])
        elif play[1] == "X":
            my_play_list.append(rules[play[0]])
        elif play[1] == "Z":
            for k,v in rules.items():
                if v == play[0]:
                    my_play_list.append(k)
        else:
            print("Not a valid play")
    return my_play_list

def rps_score(plays):
    rps_game_score = 0
    for play in plays:
        if play[1] == "Y":
            rps_game_score += 3
        elif play[1] == "Z":
            rps_game_score += 6
        else:
            rps_game_score += 0
    return rps_game_score

my_play_score = sum([rps_shape_score(play) for play in my_plays(rps_rules, playbook)])

my_score = rps_score(playbook) + my_play_score

print("My total score following the strategy guide would be: ", my_score)