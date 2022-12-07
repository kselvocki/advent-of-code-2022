import string

with open("day03.txt") as day_03_data:
    data = day_03_data.readlines()
    data = [str.rstrip("\n") for str in data]
    
n = 3
elf_trios = [data[x:x+n] for x in range(0, len(data), n)]

letters_list = [char for char in (string.ascii_lowercase + string.ascii_uppercase)]
letters_values_dict = {count: letter for letter, count in enumerate(letters_list, 1)}

pack_overlap = []
for trio in elf_trios:
    overlap = set(trio[0]).intersection(set(trio[1]), set(trio[2]))
    pack_overlap.append(str(overlap))

pack_overlap = [str.lstrip("{'").rstrip("'}") for str in pack_overlap]

overlap_values = []
for item in pack_overlap:
    overlap_values.append(letters_values_dict[item])

print("The sum of all the badge priorities for all groups is: ", sum(overlap_values))