import pygame
# imports the pygame library to be used throughout this python file
import random
# imports a random generator library allowing random numbers to be generated throughout the game
import numpy as np
# imports numpy and renames it to np for ease of typing
# numpy is used for arrays which helps with layout of my 2048 game

WINDOW_WIDTH = 530
# describes how wide the tkinter window will be to play 2048 in
WINDOW_HEIGHT = 500
# describes how long the tkinter window will be to play 2048 in

pygame.init()
# sets up the library pygame to be used
pygame.font.init()
# allows fonts to be added in the pygame window
my_font = pygame.font.SysFont('Helvetica Neue', 70)
# tells the program which font to use and links it a variable to be used throughout the program

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# creates the pygamer window using the width and heights from above
colour = (29, 202, 194)
# creates a variable for the background colour of the window
window.fill(colour)
# uses the background colour variable (I chose a bright blue)
pygame.display.set_caption("2048 game")
# sets the name of the pygame window to 2048 game

COLOUR2 = (255, 255, 255)
# creates a variable for the 2 block and makes gives it the colour white
COLOUR4 = (0, 230, 31)
# creates a variable for the 4 block and makes gives it the colour bright green
COLOUR8 = (231, 177, 118)
# creates a variable for the 8 block and makes gives it a 'sand' colour
COLOUR16 = (232, 114, 45)
# creates a variable for the 16 block and makes gives it the colour orange/red
COLOUR32 = (235, 91, 6)
# creates a variable for the 32 block and makes gives it the colour red
COLOUR64 = (247, 95, 59)
# creates a variable for the 64 block and makes gives it the colour light red
COLOUR128 = (244, 255, 0)
# creates a variable for the 128 block and makes gives it the colour yellow
COLOUR256 = (112, 0, 255)
# creates a variable for the 256 block and makes gives it the colour purple
COLOUR512 = (0, 78, 255)
# creates a variable for the 512 block and makes gives it the colour royal blue
COLOUR1024 = (0, 255, 21)
# creates a variable for the 1024 block and makes gives it the colour neon green
COLOUR2048 = (212, 175, 55)
# creates a variable for the 2048 block and makes gives it the colour gold
N = 4
# maximum number that the user is started with each time presses arrows


class Grid:
    # creates a class called grid to set up the board for the game
    ANIMATION_TIME = 5
    # gives a timer for the board to set up


    def __init__(self):
        """
        creates a function that sets up the board using numpy to help with teh layout of teh arrays
        tells the program what to start each variable with for example start the score with zero
        creates the initial value to be added to the score of 2 because that will be the first block
        the user is displayed
        """
        self.grid = np.zeros((N, N), dtype=int)
        # creates the grid for the game using numpy to array the blocks
        self.width = 150
        # gives the width of each block in the game
        self.height = 150
        # gives the height of each block in the game
        self.value = 2
        # the initial points to be added to the score
        self.score = 0
        # how many points to start the user with
        self.gap = 25
        # how much of a gap to leave between each block

    def __str__(self):
        # creates another function to convert the self text from above into a string
        """
        creates a function to allow the program to convert any text, for example the score into string while
        keeping it in the same position
        """
        return str(self.grid)
        # returns a string from the text

    def new_number(self, k=1):
        # creates a function to tell the program what number to display the user with
        """
        this function tells the program whether to display a 2 or a 4 to the user and in what position according to
        specific gameplay
        """
        free_position = list(zip(*np.where(self.grid == 0)))
        # requests for the position using numpy to decide the array and places the new block accordingly
        for position in random.sample(free_position, k):
            # places the block randomly but with more pressure to where the user has just played
            if random.random() < .1:
                # creates the random if and else clause and says if is less than 1 give a 4 block
                self.grid[position] = 4
                # positions a 4 block on the grid
            else:
                # uses the else clause if is greater than 1 (not meet the statement)
                self.grid[position] = 2
                # then it will position a 2 block

    def move_sum_number(self):
        # creates a function that allows the numbers to be added together
        """
        this function is used when two numbers combine
        tells the program what number to display next according to the gameplay
        and where to place the new numbered block
        """
        grid_number = self[self != 0]
        # tells the program to add the two blocks together only if they are the same
        grid_sum = []
        # creates the new blocks number by adding the two numbers beforehand as long they are the same block
        skip = False
        # this function will only be passed if the blocks are the same therefore there should be no case where the
        # block is skipped
        for i in range(len(grid_number)):
            # creates a for else iterative process saying if I is in range of the placement of the block in the grid
            # then follow the conditions
            if skip:
                # the if part of the iterative clause - whether the block should be skipped if not equal
                skip = False
                # but since this part of the function is only for if the blocks are equal then skip will equal false
                continue
                # tells the program to continue the rest of the flow
            if i < len(grid_number) - 1 and grid_number[i] == grid_number[i + 1]:
                # tells the program where to place the block whether to add one to the right or to the left
                new_number = grid_number[i] * 2
                # creates the new block by tells the program what number to display by multiplying the previous
                # number by 2
                skip = True
                # tells program to skip the block to avoid repeating the same block and the program
                # displaying the previous block
            else:
                # if all the above if statements are not met then the program will move onto this, the else part
                new_number = grid_number[i]
                # creates a new block and places into the new slot

            grid_sum.append(new_number)
            # appends the array of the blocks by adding the new block into the array

        return np.array(grid_sum)
        # displays the grid with the new block plus the old blocks all in their positions live

    def move_number(self, move):
        # creates a new function within the grid class that allows the user to move the pieces up, down, left or right
        """
        this function is connected to self and allows the player to move the board's pieces up, down, left or right
        while dealing with any collisions of the same numbers
        for example when moving left if there are two twos then they will combine and make one four
        """
        if move == 'l':
            # makes an if statement saying that if the player's movement is left,
            # which is linked to the left key further down, the following will happen
            for i in range(N):
                # when the 'imaginary' (meaning block in use) is in range of the grid
                temp = self.grid[i, :]
                # find a temporary (until next move) space for those blocks (1 left)
                temp_n = Grid.move_sum_number(temp)
                # tells the array where to place the blocks in the grid
                new_temp = np.zeros_like(temp)
                # makes sure the game doesn't ignore empty spaces
                # still includes them in the array while moving the blocks
                new_temp[:len(temp_n)] = temp_n
                # adds the new block with its temporary position
                # adds its length with its position and recalls it as new_temp
                self.grid[i, :] = new_temp
                # resets the new block back to pointing at the one at hand

        elif move == 'u':
            # makes an elif statement saying that if the player's movement is up,
            # which is linked to the up key further down, the following will happen
            for i in range(N):
                # when the 'imaginary' (meaning block in use) is in range of the grid
                temp = self.grid[:, i]
                # find a temporary (until next move) space for those blocks (1 up)
                temp_n = Grid.move_sum_number(temp)
                # tells the array where to place the blocks in the grid
                new_temp = np.zeros_like(temp)
                # makes sure the game doesn't ignore empty spaces
                # still includes them in the array while moving the blocks
                new_temp[:len(temp_n)] = temp_n
                # adds the new block with its temporary position
                # adds its length with its position and recalls it as new_temp
                self.grid[:, i] = new_temp
                # resets the new block back to pointing at the one at hand

        elif move == 'r':
            # makes an elif statement saying that if the player's movement is right,
            # which is linked to the up key further down, the following will happen
            for i in range(N):
                # when the 'imaginary' (meaning block in use) is in range of the grid
                temp = self.grid[i, :]
                # the temporary block will be allocated and pointed at meaning that it will control the movement
                temp = temp[::-1]
                # for example since the above line says right it uses ::-1 to say move left but backwards
                temp_n = Grid.move_sum_number(temp)
                # this now stores the grids temporary new block's position into a variable called temp_n
                new_temp = np.zeros_like(temp)
                # makes sure the game doesn't ignore empty spaces
                # still includes them in the array while moving the blocks
                new_temp[:len(temp_n)] = temp_n
                # adds the new block with its temporary position
                # adds its length with its position and recalls it as new_temp
                new_temp = new_temp[::-1]
                # links the movement of left but backwards (right) to the new_temp variable from above
                self.grid[i, :] = new_temp
                # connects back to the grid and stores this new position inside the variable
                # it can then be looped throughout the whole game

        elif move == 'd':
            # makes an elif statement saying that if the player's movement is down,
            # which is linked to the up key further down, the following will happen
            for i in range(N):
                # when the 'imaginary' (meaning block in use) is in range of the grid
                temp = self.grid[:, i]
                # the temporary block will be allocated and pointed at meaning that it will control the movement
                temp = temp[::-1]
                # for example since the above line says up ::-1 to say move up but backwards
                temp_n = Grid.move_sum_number(temp)
                # this now stores the grids temporary new block's position into a variable called temp_n
                new_temp = np.zeros_like(temp)
                # makes sure the game doesn't ignore empty spaces
                # still includes them in the array while moving the blocks
                new_temp[:len(temp_n)] = temp_n
                # adds the new block with its temporary position
                # adds its length with its position and recalls it as new_temp
                new_temp = new_temp[::-1]
                # links the movement of up but down(right) to the new_temp variable from above
                self.grid[:, i] = new_temp
                # connects back to the grid and stores this new position inside the variable
                # it can then be looped throughout the whole game

    def isfilled(self):
        # creates new function for when all possible moves are out
        # (when all blocks are taken and when adding a two will just block the board)
        """
        this is the game over function that allows the game to finish
        when player gets to this stage it then plays another function
        asking them if they would like to play again or quit the game (this is explained further down)
        """
        old_grid = self.grid.copy()
        # uses the finished board that the user meets game over with
        # creates a new variable and stores it in old_grid
        for move in 'lrdu':
            # if final left, right, down or up results in game over then this function will play out
            self.move_number(move)
            # checks if the player has moved
            if not all((old_grid == self.grid).flatten()):
                # if player hasn't moved
                # it means the game still carries on therefore no game over message
                self.grid = old_grid
                # copies the grid and stores in a variable called old_grid
                return False
                # tells the program to carry on the game and not display game over message
        return True
        # this will return the game over message asking the user if they would like to restart or quit

    def CLI_play(self):
        # creates another function linking to what will happen in the terminal/console per specific circumstances
        """
        this function is how the output is made in the console/terminal
        the terminal will output the result of each game once the game is over
        if the user gets to the point where they are out of moves
        inside the terminal 'Game Over' will be outputted
        """
        self.new_number(k=2)
        # connects the new_number variable to this function and all the other function with self
        # tells the program to add a number 2 to the game
        while True:
            # creates a while statement to perform a series of outputs
            print(self.grid)
            # displays the current game board to the user
            # they then are able to choose their next move
            old_grid = self.grid.copy()
            # copies the past grid without the new block
            player = input("Enter Move : ")
            # creates a variable for the player and asks them to enter there move
            if player == 'q':
                # sets the input for if the player wants to quit the game
                break
                # closes the window
            elif player == 'l':
                # if player moves left once
                self.move_number('l')
                # then there new position is stored into move_number and connected to each function
            elif player == 'r':
                # if player moves right once
                self.move_number('r')
                # then there new position is stored into move_number and connected to each function
            elif player == 'u':
                # if player moves up once
                self.move_number('u')
                # then there new position is stored into move_number and connected to each function
            elif player == 'd':
                # if player moves down once
                self.move_number('d')
                # then there new position is stored into move_number and connected to each function
            if all((old_grid == self.grid).flatten()):
                # if, when the user makes there move and nothing happens due to the arrangement of the numbers
                # then the program will flatten the numbers by combining the same numbers
                continue
                # tells the program to continue with the rest of the flow
            self.new_number()
            # connects the variable new_number throughout the whole game using self as the function

    def createRectangle(self):
        # creates another function to create the rectangles surrounding the numbers
        """
        this function makes the curved boarder around the numbers
        makes sure to include zero spaces as well
        """
        x = 25
        # sets the vertical boarder of the squares to have a width of 25
        y = 25
        # sets the horizontal boarder of the squares to have a length of 25
        rectangle = np.zeros((4, 4), dtype=pygame.Rect)
        # places how much space between block
        rectangle_width = 100
        # sets the width to 100 of the square
        rectangle_height = 100
        # sets the square's height to 100
        rectangle_gap = 20
        # sets the gap of the block to 20


        text = np.zeros((4, 4), dtype=pygame.Surface)
        # creates a variable called text for the blank space where the blocks will go around
        for i in range(4):
            # when the block in use has a value of 4
            x = 15
            # creates a variable called x and stores a value of 15 inside
            for j in range(4):
                # uses the math notation i and j for x and y
                if self.grid[i][j] != 0:
                    # where the x and y (i and j) do not equal zero
                    rectangle[i][j] = pygame.Rect((x, y, rectangle_width, rectangle_height))
                    # take the rectangles i and j components and move them in the way the user has moved them
                    text[i][j] = my_font.render(str(self.grid[i][j]), True, (0, 0, 0))
                    # display the rectangles new i and j components

                x = x + rectangle_width + rectangle_gap
                # store the old x variable and add it to itself plus the gap between each rectangle and the actual width
                # this moves the rectangle accordingly
            y = y + rectangle_height + rectangle_gap
            # stores the old y variable and adds it to itself plus the gap between each rectangle and the actual height
            # this moves the rectangle accordingly by linking it to the above resolved i and j components
        return rectangle, text
    # this displays the new position for all the blocks from the resolved components of i and j

    def draw(self):
        # creates a new function with the name 'draw' to create the grid that the user will use to play the game
        """
        this function creates the grid and connects all the different possible blocks to it
        this function uses the rectangle function to help with spacing of the grid
        for example this function connects back to the fact that the game will have 4 block on vertical and horizontal
        """
        rect, text = self.createRectangle()
        # goes back to the above and says make the rectangle shape of the blocks
        # and the game over message equal them for how to make the rectangles
        window.fill(colour)
        # connects the grid function to the colour of the background for the grid (I chose bright blue)

        for i in range(4):
            # places the blocks onto the i component of the grid, being vertical
            for j in range(4):
                # places the blocks onto the j component of the grid, being horizontal
                if rect[i][j] != 0:
                    # where the blocks are inside the horizontal and vertical (not on zeroth i and j)
                    r = rect[i][j]
                    # a variable called r is set to this grid position
                    # and saved as how the board will be displayed in beginning
                    if self.grid[i][j] == 2:
                        # where the block has a value of 2
                        pygame.draw.rect(window, COLOUR2, r)
                        # tell pygame to create the 2 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 4:
                        # where the block has a value of 4
                        pygame.draw.rect(window, COLOUR4, r)
                        # tells pygame to create the 4 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 8:
                        # where the block has a value of 8
                        pygame.draw.rect(window, COLOUR8, r)
                        # tells pygame to create the 8 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 16:
                        # where the block has a value of 16
                        pygame.draw.rect(window, COLOUR16, r)
                        # tells pygame to create the 16 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 32:
                        # where the block has a value of 32
                        pygame.draw.rect(window, COLOUR32, r)
                        # tells pygame to create the 32 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 64:
                        # where the block has a value of 64
                        pygame.draw.rect(window, COLOUR64, r)
                        # tells pygame to create the 64 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 128:
                        # where the block has a value of 128
                        pygame.draw.rect(window, COLOUR128, r)
                        # tells pygame to create the 128 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 256:
                        # where the block has a value of 256
                        pygame.draw.rect(window, COLOUR256, r)
                        # tells pygame to create the 256 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 512:
                        # where the block has a value of 512
                        pygame.draw.rect(window, COLOUR512, r)
                        # tells pygame to create the 512 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 1024:
                        # where the block has a value of 1024
                        pygame.draw.rect(window, COLOUR1024, r)
                        # tells pygame to create the 1024 block with its colour
                        # using the variable rect for dimensions and spacing
                    elif self.grid[i][j] == 2048:
                        # where the block has a value of 2048
                        pygame.draw.rect(window, COLOUR2048, r)
                        # tells pygame to create the 2048 block with its colour
                        # using the variable rect for dimensions and spacing
                    else:
                        # where none of the above statements are met
                        pygame.draw.rect(window, COLOUR2048, r)
                        # will show the user the 2048 block with its colour
                    text_rect = text[i][j].get_rect(center=(r.left + r.width / 2, r.top + r.height / 2))
                    # creates a variable called 'text_rect'
                    # sets it equal to the text on each block and places this text in the middle
                    # it centres the text by halving the height of the horizontal and vertical
                    window.blit(text[i][j], text_rect)
                    # creates the window with the blocks all evenly spaced out
                    # and with their text in the centre for the value of each block
        self.draw_score()
        # creates a variable and connects it to self called draw_score which will be added in the game below

    def draw_score(self):
        # creates another function, this one called 'draw_score', which is connected to self and creates a score
        """
        this function creates text saying the user's score for the current game they are playing
        the score is calculated using the sum of all the blocks on the board at that current time
        therefore the user's score will change throughout the game until there are no more possible moves
        at which point the game will display game over and the two options
        the score will remain static until the game is restarted
        """
        sum = 0
        # creates a variable for the beginning of the game called sum to be how many points the user starts with
        for i in range(N):
            # captures the horizontal component of the grid
            for j in range(N):
                # captures the vertical component of the grid
                sum += self.grid[i][j]
                # adds the boards points to the initial sum
        myfont = pygame.font.SysFont('Helvetica Neue', 20)
        # creates a variable called 'myfont', which will be used for the text for the score
        # ,and gives it a style of Helevetica to look neat and a size of 20
        text = myfont.render("Score = " + str(sum), True, (0, 0, 0))
        # creates another variable for the words written where the score will be displayed on the grid
        window.blit(text, (400, 20))
        # sets how big the window is going to be in relation to the score
        self.score = sum
        # sets the sum of the users score equal to self.score, so it can be used throughout and linked back to

    def draw_Game_Over(self):
        # creates the game over function - what happens when there is no more space on the board left
        """
        this function gives the game over text options a size of 40 with a font of Helvetica Neue,
        uses two different lines one for the actual 'game over' text and one for the two options:
            restart and play again, or quit (this closes the window),
        also places where this text is going to go
        it is placed around the middle
        """
        myfont = pygame.font.SysFont('Helvetica Neue', 40)
        # creates a variable for the font and size of the 'game over' text
        sfont = pygame.font.SysFont('Helvetica Neue', 40)
        # creates a variable for the font and size of the 'restart/quit' text
        text = myfont.render("Game Over", True, (165, 89, 248), (255, 239, 40))
        # puts a box around the text by rendering it and gives it a colour of yellow
        stext = sfont.render("E = Restart Q = Quit", True, (165, 89, 248), (255, 239, 40))
        # puts a box around the text by rendering it and gives it a colour of yellow
        window.blit(text, ((WINDOW_WIDTH // 2) - 160, (WINDOW_HEIGHT // 2) - 50))
        # tells pygame where to place the text
        window.blit(stext, ((WINDOW_WIDTH // 2) - 210, (WINDOW_HEIGHT // 2) + 10))
        # tells pygame where to display the game over message

    def main(self):
        # creates our main function that brings all the previous functions together to run the full game
        """
        this is our final function of the game
        uses all the previous functions to create the final game that the user will be able to interact with
        makes each case possible by defining the necessary functions true of false for the game to flow
        """
        running = True
        # when the game begins allow it to play through all the necessary logic
        self.new_number(2)
        # start the user with the block with only the number 2

        redraw = True
        # sets the renderer to do its job and render the value of each block onto the squares
        GameOver = False
        # at this time the player still has plenty of moves left, therefore the game is not over yet
        while running:
            # uses a while statement to say, while the game is in the proces of being played the following will occur
            old_grid = self.grid.copy()
            # fetches the old_grid before the users move and stores it into the copied grid
            if redraw:
                # where the rendering is equal to
                self.draw()
                # grid being all drawn out and all numbers on their allocated blocks
                redraw = False
                # sets the rendering to not render the numbers on the blocks because they are all filled
            if not GameOver:
                # creates an if statement for when the game is still carrying on
                # and the user is able to move the pieces up down left or right

                keys = pygame.key.get_pressed()
                # creates a variable called 'keys' to enable what each key does in relation to moving the board
                for event in pygame.event.get():
                    # asks the program to fetch the data from the keyboard to see what keys have been pressed
                    if event.type == pygame.QUIT:
                        # where the user is prompted to quit or restart, and they choose to quit
                        running = False
                        # stop the game from running and close the window, therefore setting it to false

                    elif keys[pygame.K_LEFT]:
                        # where the keyboard presses the left key move the board accordingly

                        self.move_number('l')
                        # fetches the variable where left is given its definition and follows these protocols
                        self.draw()
                        # creates the new board with the movement applied

                    elif keys[pygame.K_RIGHT]:
                        # where the keyboard presses the right key move the board accordingly

                        self.move_number('r')
                        # fetches the variable where right is given its definition and follows these protocols
                        self.draw()
                        # creates the new board with the movement applied

                    elif keys[pygame.K_UP]:
                        # where the keyboard presses the up key move the board accordingly

                        self.move_number('u')
                        # fetches the variable where up is given its definition and follows these protocols
                        self.draw()
                        # creates the new board with the movement applied

                    elif keys[pygame.K_DOWN]:
                        # where the keyboard presses the down key move the board accordingly

                        self.move_number('d')
                        # fetches the variable where down is given its definition and follows these protocols
                        self.draw()
                        # creates the new board with the movement applied

                if self.isfilled():
                    # where there is no more possible moves left and/or all block spaces are taken
                    print('Game Over')
                    # the program will display 'Game Over'
                    GameOver = True
                    # this sets the GameOver message to True and displays two options
                    # first option being to restart and play again
                    # next option to quit the game which will close down the window
                    self.draw_Game_Over()
                    # draws the GameOver boxes around the two pieces of text (game over and the two options)

                pygame.display.flip()
                # flips the game and restarts the logic so the game can be played again

                if all((old_grid == self.grid).flatten()):
                    # where there are some blocks that haven't been added
                    # even though they can be added
                    # then the program will flatten the game combining all possible combinations
                    continue
                    # the game logic then continues the flow if the user moves the board left, right, up or down

                self.new_number()
                # connects the creating the new_number variable
            else:
                # where the game has actually ended and the player is out of moves
                keys = pygame.key.get_pressed()
                # the program will fetch the keyboards input
                for event in pygame.event.get():
                    # then links it back to what will happen if specific keys are selected
                    if event.type == pygame.QUIT:
                        # where the user chooses to quit
                        # from either escaping the window
                        # using their esc key
                        # or pressing q when they run out of blocks
                        # or terminating the window by pressing the cross
                        running = False
                        # this will set the game to perform to false so the window is closed straight away
                    elif keys[pygame.K_e]:
                        # the program fetches and checks if the key 'e' is pressed
                        self.grid = np.zeros((N, N), dtype=int)
                        # looks in the grid for any spaces between blocks and keeps them like that
                        # then converts the user's input of pressing the key 'e' to an integer
                        self.new_number(2)
                        # displays the user their new number when they make their move
                        GameOver = False
                        # the game is still running because the user just begun their new game
                        # they have lots more moves to make until game over
                        redraw = True
                        # sets renderer to work by adding the numbers to the centre of the blocks instantly in real time
                    elif keys[pygame.K_q]:
                        # however, if the user decides that's enough screen time, and they have pressed q
                        # the program will have fetched the keyboards inputs
                        running = False
                        # this will close the 2048 window because the user chose to end their fun!!


if __name__ == '__main__':
    # where the actual game is set back to main and the program will run
    game = Grid()
    # one variable for the entire game which first points to the grid then through all the function which link to it
    game.main()
    # sets the game to have a value of main and allowing the user to interact with the main game
