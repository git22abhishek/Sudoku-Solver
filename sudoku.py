import pygame

pygame.init()

def drawGrid(window, cell_width):
    for i in range(1,9):
        if i%3 == 0:
            stroke = 3
        else: 
            stroke = 1
        pygame.draw.line(window, (60,113,210), (0, i*cell_width), (WIDTH, i*cell_width), stroke)
        pygame.draw.line(window, (69,113,210), (i*cell_width, 0), (i*cell_width, HEIGHT), stroke)

def displayBoard(board):

    number_font = pygame.font.SysFont("Century Gothic", 30)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                number = number_font.render(" ", 1, (203,217,243))
            else:
                number = number_font.render(str(board[i][j]), 1, (203,217,243))

            WIN.blit(number, ((j*CELL_WIDTH)+int(CELL_WIDTH/2.5), (i*CELL_WIDTH)+int(CELL_WIDTH/3)))

def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return False

def valid(board, pos , n):
    # Check row 
    for j in range(9):
        if board[pos[0]][j] == n:
            return False
    # Check column
    for i in range(9):
        if board[i][pos[1]] == n:
            return False
    # Check square
    row_index = pos[0]//3
    col_index = pos[1]//3

    for i in range(row_index*3, row_index*3 + 3):
        for j in range(col_index*3, col_index*3 + 3):
            if board[i][j] == n:
                return False
    return True

def solve():
    global grid

    pos = findEmpty(grid)
    if pos == False:
        return True

    for i in range(1, 10):
        if valid(grid, pos, i):
            grid[pos[0]][pos[1]] = i

            displayBoard(grid)
            pygame.display.update()

            if solve():
                return True
            grid[pos[0]][pos[1]] = 0
    return False

if __name__ == "__main__":
    
    WIDTH, HEIGHT = 540, 540
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    CELL_WIDTH = WIDTH/9

    grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]

    running = True

    while running:

        drawGrid(WIN, CELL_WIDTH)
        displayBoard(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                solve()
        
        pygame.display.update()
        WIN.fill((50,50,50))
        
