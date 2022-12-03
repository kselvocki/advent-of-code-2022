with open("day01ex.txt") as day_01_data:
    data = day_01_data.readlines()
    data = [int(line.rstrip("\n")) if line.strip() else line.replace("\n", "next elf") for line in data]
    data.append("next elf")

# Part 1
all_elf_totals = []
elf_total = 0
for item in data:
    if item != "next elf":
        elf_total += item
    else:
        all_elf_totals.append(elf_total)
        elf_total = 0

print("The highest total that an elf is carrying is: ", max(all_elf_totals), "calories")

# Part 2
sorted_elf_totals = sorted(all_elf_totals)
top_three_total = sum(sorted_elf_totals[-3:])

print("The top three elves are carrying: ", top_three_total, "calories")