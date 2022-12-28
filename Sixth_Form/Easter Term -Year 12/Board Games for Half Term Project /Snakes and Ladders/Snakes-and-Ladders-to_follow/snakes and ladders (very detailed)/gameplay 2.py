import pygame
import chaos_bag

# Initializing pygame
pygame.init()
# Loading the required data
main_font = pygame.font.Font("fonts/Cute Little Sheep.ttf", 48)
total_turns = 0
blue_bead = pygame.image.load("images/beads/blue.png")
red_bead = pygame.image.load("images/beads/red.png")
yellow_bead = pygame.image.load("images/beads/yellow.png")
green_bead = pygame.image.load("images/beads/green.png")

snake_sound = pygame.mixer.Sound('snake.wav')
ladder_sound = pygame.mixer.Sound('ladder.wav')
win_sound = pygame.mixer.Sound('win.wav')

easy_blue_bead = pygame.transform.smoothscale(blue_bead, (40, 60))
easy_red_bead = pygame.transform.smoothscale(red_bead, (40, 60))
easy_yellow_bead = pygame.transform.smoothscale(yellow_bead, (40, 60))
easy_green_bead = pygame.transform.smoothscale(green_bead, (40, 60))
easy_board = pygame.image.load("images/easy_board.png")

hard_blue_bead = pygame.transform.smoothscale(blue_bead, (26, 40))
hard_red_bead = pygame.transform.smoothscale(red_bead, (26, 40))
hard_yellow_bead = pygame.transform.smoothscale(yellow_bead, (26, 40))
hard_green_bead = pygame.transform.smoothscale(green_bead, (26, 40))
hard_board = pygame.image.load("images/hard_board.png")

# The coordinates of the boxes of the easy board. Each coordinate shows the top left corner of the box. The first point
# i.e. at index 0, is an arbitrary point so that the appropriate coordinate can be called by using the box number.
easy_board_points = [(620, 580), (0, 0), (80, 0), (160, 0), (240, 0), (320, 0), (400, 0), (400, -80), (320, -80),
                     (240, -80), (160, -80), (80, -80), (0, -80), (0, -160), (80, -160), (160, -160), (240, -160),
                     (320, -160), (400, -160), (400, -240), (320, -240), (240, -240), (160, -240), (80, -240),
                     (0, -240), (0, -320), (80, -320), (160, -320), (240, -320), (320, -320), (400, -320), (400, -400),
                     (320, -400), (240, -400), (160, -400), (80, -400), (0, -400)]
# The list of rows of the easy board. Each sublist contains the boxes number in the corresponding row.
easy_board_rows = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
                   [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]

# The coordinates of the boxes of the hard board. Each coordinate shows the top left corner of the box. The first point
# i.e. at index 0, is an arbitrary point so that the appropriate coordinate can be called by using the box number.
hard_board_points = [(600, 590), (0, 0), (50, 0), (100, 0), (150, 0), (200, 0), (250, 0), (300, 0), (350, 0),
                     (400, 0), (450, 0), (450, -50), (400, -50), (350, -50), (300, -50), (250, -50), (200, -50),
                     (150, -50), (100, -50), (50, -50), (0, -50), (0, -100), (50, -100), (100, -100),
                     (150, -100), (200, -100), (250, -100), (300, -100), (350, -100), (400, -100), (450, -100),
                     (450, -150), (400, -150), (350, -150), (300, -150), (250, -150), (200, -150), (150, -150),
                     (100, -150), (50, -150), (0, -150), (0, -200), (50, -200), (100, -200), (150, -200),
                     (200, -200), (250, -200), (300, -200), (350, -200), (400, -200), (450, -200), (450, -250),
                     (400, -250), (350, -250), (300, -250), (250, -250), (200, -250), (150, -250), (100, -250),
                     (50, -250), (0, -250), (0, -300), (50, -300), (100, -300), (150, -300), (200, -300),
                     (250, -300), (300, -300), (350, -300), (400, -300), (450, -300), (450, -350), (400, -350),
                     (350, -350), (300, -350), (250, -350), (200, -350), (150, -350), (100, -350), (50, -350),
                     (0, -350), (0, -400), (50, -400), (100, -400), (150, -400), (200, -400), (250, -400),
                     (300, -400), (350, -400), (400, -400), (450, -400), (450, -450), (400, -450), (350, -450),
                     (300, -450), (250, -450), (200, -450), (150, -450), (100, -450), (50, -450), (0, -450)]
# The list of rows of the hard board. Each sublist contains the boxes number in the corresponding row.
hard_board_rows = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                   [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                   [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                   [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]


def current_easy_box(x, y):
    """Gets the coordinates of the beads on the easy board and returns the box number in which the bead is present.
    Arguments
    ---------
    x : int
        The x-coordinate of the bead.
    y : int
        The y-coordinate of the bead.
    Return
    ------
    box : int
        The number of box in which the bead is present."""
    box = 1
    for i in easy_board_points:
        if i[0] <= x < i[0] + 80 and i[1] <= y < i[1] + 80:
            box = easy_board_points.index(i)
            break
    return box


def current_hard_box(x, y):
    """Gets the coordinates of the beads on the hard board and returns the box number in which the bead is present.
    Arguments
    ---------
    x : int
        The x-coordinate of the bead.
    y : int
        The y-coordinate of the bead.
    Return
    ------
    box : int
        The number of box in which the bead is present."""
    box = 1
    for i in hard_board_points:
        if i[0] <= x < i[0] + 50 and i[1] <= y < i[1] + 50:
            box = hard_board_points.index(i)
            break
    return box


def positive_easy_movement(x, y):
    """Gets the coordinates of the beads on the easy board and changes them according to the row and column of the board
    in which the bead is present. This function is only for the positive values of the token.
        Arguments
        ---------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead.
        Return
        ------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead."""
    row = 0
    for i in easy_board_rows:
        if current_easy_box(x, y) in i:
            row = easy_board_rows.index(i)
    if current_easy_box(x, y) in [6, 12, 18, 24, 30] and (x == 0 or x == 400):
        y -= 80
    else:
        if row % 2 == 0:
            x += 5
        else:
            x -= 5
    return x, y


def positive_hard_movement(x, y):
    """Gets the coordinates of the beads on the hard board and changes them according to the row and column of the board
    in which the bead is present. This function is only for the positive values of the token.
        Arguments
        ---------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead.
        Return
        ------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead."""
    row = 0
    for i in hard_board_rows:
        if current_hard_box(x, y) in i:
            row = hard_board_rows.index(i)
    if current_hard_box(x, y) in [10, 20, 30, 40, 50, 60, 70, 80, 90] and (x == 0 or x == 450):
        y -= 50
    else:
        if row % 2 == 0:
            x += 5
        else:
            x -= 5
    return x, y


def negative_easy_movement(x, y):
    """Gets the coordinates of the beads on the easy board and changes them according to the row and column of the board
    in which the bead is present. This function is only for the negative values of the token.
        Arguments
        ---------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead.
        Return
        ------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead."""
    row = 0
    for i in easy_board_rows:
        if current_easy_box(x, y) in i:
            row = easy_board_rows.index(i)
    if current_easy_box(x, y) in [7, 13, 19, 25, 31] and (x == 0 or x == 400):
        y += 80
    else:
        if row % 2 == 0:
            x -= 5
        else:
            x += 5
    return x, y


def negative_hard_movement(x, y):
    """Gets the coordinates of the beads on the hard board and changes them according to the row and column of the board
    in which the bead is present. This function is only for the negative values of the token.
        Arguments
        ---------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead.
        Return
        ------
        x : int
            The x-coordinate of the bead.
        y : int
            The y-coordinate of the bead."""
    row = 0
    for i in hard_board_rows:
        if current_hard_box(x, y) in i:
            row = hard_board_rows.index(i)
    if current_hard_box(x, y) in [11, 21, 31, 41, 51, 61, 71, 81, 91] and (x == 0 or x == 450):
        y += 50
    else:
        if row % 2 == 0:
            x -= 5
        else:
            x += 5
    return x, y


def easy_movement(x, y, num):
    """Gets the coordinates of the beads on the easy board and uses the pre-defined functions to change the coordinates.
    Arguments
    ---------
    x : int
        The x-coordinate of the bead.
    y : int
        The y-coordinate of the bead.
    num : int
        The token returned by the chaos bag
    Return
    ------
    x : int
        The x-coordinate of the bead.
    y : int
        The y-coordinate of the bead."""
    if num > 0:
        x, y = positive_easy_movement(x, y)
    elif num < 0:
        x, y = negative_easy_movement(x, y)
    else:
        pass
    return x, y


def hard_movement(x, y, num):
    """Gets the coordinates of the beads on the hard board and uses the pre-defined functions to change the coordinates.
    Arguments
    ---------
    x : int
        The x-coordinate of the bead.
    y : int
        The y-coordinate of the bead.
    num : int
        The token returned by the chaos bag
    Return
    ------
    x : int
        The x-coordinate of the bead.
    y : int
        The y-coordinate of the bead."""
    if num > 0:
        x, y = positive_hard_movement(x, y)
    elif num < 0:
        x, y = negative_hard_movement(x, y)
    else:
        pass
    return x, y


def easy_ladders(box):
    """Gets the box in which the bead is present and if the box is the start of a ladder, then the box at the end of the
    corresponding ladder will be returned. This function is only for the easy board.
    Arguments
    ---------
    box : int
        The box in which the bead is present.
    Return
    ------
    box : int
        The box in which bead is present."""
    ladders = [[6, 18], [12, 24], [15, 27]]
    for i in ladders:
        if box == i[0]:
            box = i[1]
            break
    return box


def easy_snakes(box):
    """Gets the box in which the bead is present and if the box is the start of a snake, then the box at the end of the
    corresponding snake will be returned. This function is only for the easy board.
    Arguments
    ---------
    box : int
        The box in which the bead is present.
    Return
    ------
    box : int
        The box in which bead is present."""
    snakes = [[11, 3], [20, 16], [25, 23], [32, 28]]
    for i in snakes:
        if box == i[0]:
            box = i[1]
            break
    return box


def hard_ladders(box):
    """Gets the box in which the bead is present and if the box is the start of a ladder, then the box at the end of the
    corresponding ladder will be returned. This function is only for the hard board.
    Arguments
    ---------
    box : int
        The box in which the bead is present.
    Return
    ------
    box : int
        The box in which bead is present."""
    ladders = [[3, 21], [8, 30], [28, 84], [58, 77], [75, 86], [80, 100], [90, 91]]
    for i in ladders:
        if box == i[0]:
            box = i[1]
            break
    return box


def hard_snakes(box):
    """Gets the box in which the bead is present and if the box is the start of a snake, then the box at the end of the
    corresponding snake will be returned. This function is only for the hard board.
    Arguments
    ---------
    box : int
        The box in which the bead is present.
    Return
    ------
    box : int
        The box in which bead is present."""
    snakes = [[17, 13], [52, 29], [57, 40], [62, 22], [88, 18], [95, 51], [97, 79]]
    for i in snakes:
        if box == i[0]:
            box = i[1]
            break
    return box


# noinspection PyTypeChecker
def easy_game(window, token, players, in_movement):
    """This function starts the game of difficulty level: easy.
    Arguments
    ---------
    window : Display Surface
        The surface on which everything will be blitted
    token : int
        Token returned by the chaos bag. It's when the game starts.
    players : list
        List containing the dictionaries of all the players in the current game.
    in_movement : Boolean
        Tells if any bead is in movement or not.
    Return
    ------
    token : int
        Token returned by the chaos bag. It's when the game starts.
    in_movement : Boolean
        Tells if any bead is in movement or not.
    game_finished : Boolean
        Checks if the game has finished or not. It becomes true when any of the bead reaches last box.
    winner : string
        The name of the player who wins when the game is finished."""
    # Following conditional statements will assign the colors to the players.
    if len(players) == 2:
        colors = [(1, 94, 171), (165, 38, 19)]
    elif len(players) == 3:
        colors = [(254, 208, 0), (1, 94, 171), (165, 38, 19)]
    else:
        colors = [(254, 208, 0), (13, 134, 67), (1, 94, 171), (165, 38, 19)]
    global total_turns
    token, total_turns, bag_clicked = chaos_bag.main(window, 'easy', len(players), token, total_turns, in_movement)
    current_turn = total_turns % len(players)
    # The data of the player will be updated when the chaos bag is clicked.
    x, y = players[current_turn]['current_pos'][0], players[current_turn]['current_pos'][1]
    if bag_clicked and type(token) == int:
        new_box = players[current_turn]['temp_box'] + token
        players[current_turn].update({'temp_box': current_easy_box(x, y)})
        if new_box < 1:
            new_box = 1
        elif new_box > 36:
            new_box = 36
        players[current_turn].update({'new_box': new_box})
    turn_text = main_font.render(f"{players[current_turn]['name']}'s Turn", True, (255, 255, 255))
    turn_rect = pygame.Rect(860 - (turn_text.get_width() / 2), 600, turn_text.get_width(), 55)
    pygame.draw.rect(window, colors[current_turn - 1], turn_rect)
    window.blit(pygame.transform.smoothscale(easy_board, (480, 480)), (620, 100))
    window.blit(turn_text, (860 - (turn_text.get_width() / 2), 600))
    # If a new box is assigned to the player when he clicks the chaos bag, then movement function will be called and the
    # bead will start moving.
    if type(token) == int and (x, y) != easy_board_points[players[current_turn]['new_box']]:
        in_movement = True
        x, y = easy_movement(x, y, token)
        # Following statements will make sure that the bead remains within the board.
        if x < 0:
            x = 0
        if x > 400:
            x = 400
        if y < -400:
            y = -400
        if y > 0:
            y = 0
        # The coordinates of the bead will be updated after movement.
        players[current_turn].update({'current_pos': (x, y)})
        if (x, y) == easy_board_points[players[current_turn]['new_box']]:
            players[current_turn].update({'temp_box': current_easy_box(x, y)})
    else:
        in_movement = False
    # If the player lands on a ladder, he will move to the end of that ladder and the data will be updated accordingly.
    if players[current_turn]['new_box'] in [6, 12, 15]:
        if (x, y) == easy_board_points[players[current_turn]['new_box']]:
            new_box = easy_ladders(players[current_turn]['new_box'])
            (x, y) = easy_board_points[new_box]
            players[current_turn].update({'current_pos': (x, y)})
            players[current_turn].update({'new_box': new_box})
            players[current_turn].update({'temp_box': new_box})
            ladder_sound.play()
    # If the player lands on a snake, he will move to the end of that snake and the data will be updated accordingly.
    if players[current_turn]['new_box'] in [11, 20, 25, 32]:
        if (x, y) == easy_board_points[players[current_turn]['new_box']]:
            new_box = easy_snakes(players[current_turn]['new_box'])
            (x, y) = easy_board_points[new_box]
            players[current_turn].update({'current_pos': (x, y)})
            players[current_turn].update({'new_box': new_box})
            players[current_turn].update({'temp_box': new_box})
            snake_sound.play()

    # The beads will be blitted on the screen at the corresponding coordinates.
    if len(players) == 2:
        window.blit(easy_blue_bead, (640 + players[0]['current_pos'][0], 510 + players[0]['current_pos'][1]))
        window.blit(easy_red_bead, (640 + players[1]['current_pos'][0], 510 + players[1]['current_pos'][1]))
    elif len(players) == 3:
        window.blit(easy_blue_bead, (640 + players[0]['current_pos'][0], 510 + players[0]['current_pos'][1]))
        window.blit(easy_red_bead, (640 + players[1]['current_pos'][0], 510 + players[1]['current_pos'][1]))
        window.blit(easy_yellow_bead, (640 + players[2]['current_pos'][0], 510 + players[2]['current_pos'][1]))
    elif len(players) == 4:
        window.blit(easy_blue_bead, (640 + players[0]['current_pos'][0], 510 + players[0]['current_pos'][1]))
        window.blit(easy_red_bead, (640 + players[1]['current_pos'][0], 510 + players[1]['current_pos'][1]))
        window.blit(easy_yellow_bead, (640 + players[2]['current_pos'][0], 510 + players[2]['current_pos'][1]))
        window.blit(easy_green_bead, (640 + players[3]['current_pos'][0], 510 + players[3]['current_pos'][1]))
    if players[current_turn]['temp_box'] == 36:
        game_finished = True
        winner = players[current_turn - 1]['name']
        win_sound.play()
    else:
        game_finished = False
        winner = None
    return token, in_movement, game_finished, winner


# noinspection PyTypeChecker
def hard_game(window, token, players, in_movement):
    """This function starts the game of difficulty level: hard.
    Arguments
    ---------
    window : Display Surface
        The surface on which everything will be blitted
    token : int
        Token returned by the chaos bag. It's when the game starts.
    players : list
        List containing the dictionaries of all the players in the current game.
    in_movement : Boolean
        Tells if any bead is in movement or not.
    Return
    ------
    token : int
        Token returned by the chaos bag. It's when the game starts.
    in_movement : Boolean
        Tells if any bead is in movement or not.
    game_finished : Boolean
        Checks if the game has finished or not. It becomes true when any of the bead reaches last box.
    winner : string
        The name of the player who wins when the game is finished."""
    # Following conditional statements will assign the colors to the players.
    if len(players) == 2:
        colors = [(1, 94, 171), (165, 38, 19)]
    elif len(players) == 3:
        colors = [(254, 208, 0), (1, 94, 171), (165, 38, 19)]
    else:
        colors = [(254, 208, 0), (13, 134, 67), (1, 94, 171), (165, 38, 19)]
    global total_turns
    token, total_turns, bag_clicked = chaos_bag.main(window, 'hard', len(players), token, total_turns, in_movement)
    current_turn = total_turns % len(players)
    # The data of the player will be updated when the chaos bag is clicked.
    x, y = players[current_turn]['current_pos'][0], players[current_turn]['current_pos'][1]
    if bag_clicked and type(token) == int:
        new_box = players[current_turn]['temp_box'] + token
        players[current_turn].update({'temp_box': current_hard_box(x, y)})
        if new_box < 1:
            new_box = 1
        elif new_box > 100:
            new_box = 100
        players[current_turn].update({'new_box': new_box})
    turn_text = main_font.render(f"{players[current_turn]['name']}'s Turn", True, (255, 255, 255))
    turn_rect = pygame.Rect(850 - (turn_text.get_width() / 2), 610, turn_text.get_width(), 55)
    pygame.draw.rect(window, colors[current_turn - 1], turn_rect)
    window.blit(pygame.transform.smoothscale(hard_board, (500, 500)), (600, 90))
    window.blit(turn_text, (850 - (turn_text.get_width() / 2), 610))
    # If a new box is assigned to the player when he clicks the chaos bag, then movement function will be called and the
    # bead will start moving.
    if type(token) == int and (x, y) != hard_board_points[players[current_turn]['new_box']]:
        in_movement = True
        x, y = hard_movement(x, y, token)
        # Following statements will make sure that the bead remains within the board.
        if x < 0:
            x = 0
        if x > 450:
            x = 450
        if y < -450:
            y = -450
        if y > 0:
            y = 0
        # The coordinates of the bead will be updated after movement.
        players[current_turn].update({'current_pos': (x, y)})
        if (x, y) == hard_board_points[players[current_turn]['new_box']]:
            players[current_turn].update({'temp_box': current_hard_box(x, y)})
    else:
        in_movement = False
    # If the player lands on a ladder, he will move to the end of that ladder and the data will be updated accordingly.
    if players[current_turn]['new_box'] in [3, 8, 28, 58, 75, 80, 90]:
        if (x, y) == hard_board_points[players[current_turn]['new_box']]:
            new_box = hard_ladders(players[current_turn]['new_box'])
            (x, y) = hard_board_points[new_box]
            players[current_turn].update({'current_pos': (x, y)})
            players[current_turn].update({'new_box': new_box})
            players[current_turn].update({'temp_box': new_box})
            ladder_sound.play()
    # If the player lands on a snake, he will move to the end of that snake and the data will be updated accordingly.
    if players[current_turn]['new_box'] in [17, 52, 57, 62, 88, 95, 97]:
        if (x, y) == hard_board_points[players[current_turn]['new_box']]:
            new_box = hard_snakes(players[current_turn]['new_box'])
            (x, y) = hard_board_points[new_box]
            players[current_turn].update({'current_pos': (x, y)})
            players[current_turn].update({'new_box': new_box})
            players[current_turn].update({'temp_box': new_box})
            snake_sound.play()

    # The beads will be blitted on the screen at the corresponding coordinates.
    if len(players) == 2:
        window.blit(hard_blue_bead, (612 + players[0]['current_pos'][0], 545 + players[0]['current_pos'][1]))
        window.blit(hard_red_bead, (612 + players[1]['current_pos'][0], 545 + players[1]['current_pos'][1]))
    elif len(players) == 3:
        window.blit(hard_blue_bead, (612 + players[0]['current_pos'][0], 545 + players[0]['current_pos'][1]))
        window.blit(hard_red_bead, (612 + players[1]['current_pos'][0], 545 + players[1]['current_pos'][1]))
        window.blit(hard_yellow_bead, (612 + players[2]['current_pos'][0], 545 + players[2]['current_pos'][1]))
    elif len(players) == 4:
        window.blit(hard_blue_bead, (612 + players[0]['current_pos'][0], 545 + players[0]['current_pos'][1]))
        window.blit(hard_red_bead, (612 + players[1]['current_pos'][0], 545 + players[1]['current_pos'][1]))
        window.blit(hard_yellow_bead, (612 + players[2]['current_pos'][0], 545 + players[2]['current_pos'][1]))
        window.blit(hard_green_bead, (612 + players[3]['current_pos'][0], 545 + players[3]['current_pos'][1]))
    if players[current_turn]['temp_box'] == 100:
        game_finished = True
        winner = players[current_turn - 1]['name']
        win_sound.play()
    else:
        game_finished = False
        winner = None
    print((x, y), current_hard_box(x, y), players[current_turn]['new_box'])
    return token, in_movement, game_finished, winner
