import string

with open("day03.txt") as day_03_data:
    data = day_03_data.readlines()
    data = [str.rstrip("\n") for str in data]
    pack_contents = [[line[:len(line)//2], line[len(line)//2:]] for line in data]

letters_list = [char for char in (string.ascii_lowercase + string.ascii_uppercase)]
letters_values_dict = {count: letter for letter, count in enumerate(letters_list, 1)}

pocket_overlap = []
for pack in pack_contents:
    overlap = set(pack[0]).intersection(set(pack[1]))
    pocket_overlap.append(str(overlap))

pocket_overlap = [str.lstrip("{'").rstrip("'}") for str in pocket_overlap]

overlap_values = []
for item in pocket_overlap:
    overlap_values.append(letters_values_dict[item])

print("The sum of all items that show up in both pockets is: ", sum(overlap_values))