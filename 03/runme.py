inputfiles = ['example.txt','input.txt']

for filename in inputfiles:
    with open(filename) as file:
        schematic_map = file.read().splitlines()

    non_symbols = set(['.','0','1','2','3','4','5','6','7','8','9'])
    part_numbers = []
    part_sum = 0
    for row, line in enumerate(schematic_map):
        part_number = ''
        for i,c in enumerate(line):
            process_num = False
            if c.isdigit():
                part_number += c
                if i == len(line)-1:
                    process_num = True
            else:
                process_num = True
            if process_num and part_number != '':
                start = i-len(part_number)-1 \
                    if i-len(part_number)-1 > 0 else 0
                end = i + 1
                search_set = set(schematic_map[row][start:end])-non_symbols
                if row != 0:
                    search_set |= set(schematic_map[row-1][start:end])-non_symbols
                if row != len(schematic_map)-1:
                    search_set |= set(schematic_map[row+1][start:end])-non_symbols
                if search_set:
                    part_sum += int(part_number)
                part_number = ''
    print(part_sum)