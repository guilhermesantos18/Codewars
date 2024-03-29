def maze_runner(maze, directions):
    starty = startx = 0
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[y][x] == 2:
                starty = y
                startx = x
    for direc in directions:
        if direc == 'N':
            starty -= 1
        elif direc == 'S':
            starty += 1
        elif direc == 'E':
            startx += 1
        elif direc == 'W':
            startx -= 1
        if starty > len(maze) - 1 or startx > len(maze) - 1 or IndexError or maze[starty][startx] == 1:
            return 'Dead'
        if maze[starty][startx] == 3:
            return 'Finish'
    return 'Lost'


maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1]]

print(maze_runner(maze, ["N","N","N","N","N","E","E","S","S","S","S","S","S"]))
