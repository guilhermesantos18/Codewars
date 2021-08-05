def maze_runner(maze, directions):
    end = maze[2][6]
    start = maze[6][2]
    caminho = []
    cont_n = cont_s = cont_e = cont_w = 0
    for direc in directions:




maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1]]
maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"])
