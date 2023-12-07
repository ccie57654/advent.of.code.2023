maxcubes = {"red": 12, "green": 13, "blue": 14}

inputfiles = ['example1.txt','input.txt']

for filename in inputfiles:
    with open(filename) as file:
        games = file.read().splitlines()

    sumIDs,sumProducts = 0,0
    for gameentry, game in enumerate(games):
        gamenum, pulls = game.split(':')
        gamevalid = True
        current_game = {'red': 0, 'green': 0, 'blue': 0}
        d,block = '',''
        for c in pulls:
            if c in (',',';',' '):
                if block != '':
                    current_game[block] = max(int(d), current_game[block])
                    d,block = '',''
                continue
            elif c.isdigit():
                d += c
            else:
                block += c
        current_game[block] = max(int(d), current_game[block])
        for (_, max_block_num), (_, game_block_num) in zip(maxcubes.items(), current_game.items()):
            gamevalid &= game_block_num <= max_block_num
        if gamevalid:
            sumIDs += int(gamenum[5:])
        sumProducts += current_game['red']*current_game['green']*current_game['blue']
    print("Valid Game Sum: "+str(sumIDs) + " ValidGameMinCubeProduct: "+str(sumProducts))