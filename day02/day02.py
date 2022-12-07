with open("day02.txt") as day_02_data:
    data = day_02_data.readlines()
    playbook = [str.replace("X", "A").replace("Y", "B").replace("Z", "C").rstrip("\n").split(" ") for str in data]

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 for loss, 3 for draw, and 6 for win
# A beats C, B beats A, and C beats B

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

def rps_play_score(plays):
    play_score = 0
    for play in plays:
        if play[1] == play[0]:
            play_score += (3 + rps_shape_score(play[1]))
        elif ((play[1] == "A") and (play[0] == "C")) or ((play[1] == "B") and (play[0] == "A")) or ((play[1] == "C") and (play[0] == "B")):
            play_score += (6 + rps_shape_score(play[1]))
        elif ((play[0] == "A") and (play[1] == "C")) or ((play[0] == "B") and (play[1] == "A")) or ((play[0] == "C") and (play[1] == "B")):
            play_score += (0 + rps_shape_score(play[1]))
        else:
            print("Not a valid play")
    return play_score

my_score = rps_play_score(playbook)

print("My total score following the strategy guide would be: ", my_score)