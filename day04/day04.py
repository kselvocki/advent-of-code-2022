with open("day04.txt") as day_04_data:
    data = day_04_data.readlines()
    data = [str.rstrip("\n").split(",") for str in data]
    data = [[str.split("-") for str in line] for line in data]
    data = [[[int(str) for str in list] for list in line] for line in data]

elf_sections = []
for line in data:
    elf_pair = []
    for list in line:
        start, end = list[0], list[1]+1
        elf_pair = [num for num in range(start, end)]
        elf_sections.append(elf_pair)

n = 2
elf_sections = [elf_sections[x:x+n] for x in range(0, len(elf_sections), n)]

# Part 1
def elf_overlap_part1(list):
    fully_contain_count = 0
    for pair in list:
        overlap = set(pair[0]).intersection(set(pair[1]))
        if (overlap == (set(pair[0]))) or (overlap == set(pair[1])):
            fully_contain_count += 1
    return fully_contain_count

print("The number of assigments in which one fully contains the other is: ", elf_overlap_part1(elf_sections))

# Part 2
def elf_overlap_part2(list):
    any_overlap_count = 0
    for pair in list:
        overlap = set(pair[0]).intersection(set(pair[1]))
        if overlap:
            any_overlap_count += 1
    return any_overlap_count

print("The number of assigments in which one fully contains the other is: ", elf_overlap_part2(elf_sections))