import pygame

# Initializing pygame
pygame.init()
# Loading the required images
main_font = pygame.font.Font("fonts/Cute Little Sheep.ttf", 36)
main_font_big = pygame.font.Font("fonts/Cute Little Sheep.ttf", 42)
instructions_img = pygame.image.load("images/instructions.png")
board = pygame.transform.smoothscale(pygame.image.load("images/Artboard (1).png"), (800, 400))
play_game_img = pygame.image.load("images/playgame.png")
leaderboard_img = pygame.image.load("images/leaderboard.png")
quit_img = pygame.image.load("images/quit.png")
difficulty_lvl_img = pygame.image.load("images/diff_level.png")
diff_easy_img = pygame.image.load("images/diff_easy.png")
diff_hard_img = pygame.image.load("images/diff_hard.png")
backward_img = pygame.image.load("images/backward.png")
forward_img = pygame.image.load("images/forward.png")
two_players_img = pygame.image.load("images/2 players.png")
three_players_img = pygame.image.load("images/3 players.png")
four_players_img = pygame.image.load("images/4 players.png")
textbox_img = pygame.image.load("images/textbox.png")
first_player = pygame.image.load("images/first player.png")
second_player = pygame.image.load("images/second player.png")
third_player = pygame.image.load("images/third player.png")
fourth_player = pygame.image.load("images/fourth player.png")
player_num_img = [first_player, second_player, third_player, fourth_player]

# Assigning variables to the required font and colors
text_font = pygame.font.Font("fonts/Pumpkin Story.ttf", 48)
selected_color = (135, 250, 0)
deselected_color = (135, 200, 0)

alphabets = 'abcdefghijklmnopqrstuvwxyz'
# First making a list of all the images of the alphabet, then loading them
img_directories = [f"images/alphabets/{i}.png" for i in alphabets]
img1_directories = [f"images/alphabets/{i}1.png" for i in alphabets]
letter_imgs = [pygame.image.load(i) for i in img_directories]
letter1_imgs = [pygame.image.load(i) for i in img1_directories]
letters_data = []
# Using for loops to append sub-lists within the letters_data list with the format: [x-coordinate, y-coordinate, 'letter']
for i in range(97, 497, 80):
    for j in range(666, 1066, 80):
        letters_data.append([j, i])
for i in range(25):
    letters_data[i].append(alphabets[i])
letters_data.append([826, 497, 'z'])


def main(window):
    """Gets the window on which the main menu will be shown and block transfers (blits) the required images on it.
    Using if-else conditions it checks where the mouse click occurred and returns a string accordingly.
    Argument
    --------
    window : Display Surface
        The surface on which all screens will be shown
    Return
    ------
    main_menu_command : string
        A string is returned according to the command chosen by the user"""
    # Getting mouse position in the form (x, y)
    mouse = pygame.mouse.get_pos()
    main_menu_command = None

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    # If the mouse is hovering within the given coordinates the image transforms into a larger version of itself
    if 400 <= mouse[0] <= 800 and 132 <= mouse[1] <= 212:
        window.blit(play_game_img, (350, 122))
        # If the mouse is clicked within the given coordinates, the variable main_menu_command is assigned a string according to the image clicked
        if mouse_clicked():
            main_menu_command = 'play game'
    # This else condition will blit the image if no mouse is hovering over those coordinates
    else:
        window.blit(pygame.transform.smoothscale(play_game_img, (400, 80)), (400, 132))
    if 400 <= mouse[0] <= 800 and 232 <= mouse[1] <= 312:
        window.blit(leaderboard_img, (350, 222))
        if mouse_clicked():
            main_menu_command = 'leaderboard'
    else:
        window.blit(pygame.transform.smoothscale(leaderboard_img, (400, 80)), (400, 232))
    if 400 <= mouse[0] <= 800 and 332 <= mouse[1] <= 412:
        window.blit(instructions_img, (350, 322))
        if mouse_clicked():
            main_menu_command = 'instructions'
    else:
        window.blit(pygame.transform.smoothscale(instructions_img, (400, 80)), (400, 332))
    if 400 <= mouse[0] <= 800 and 432 <= mouse[1] <= 512:
        window.blit(quit_img, (350, 422))
        if mouse_clicked():
            main_menu_command = 'quit'
    else:
        window.blit(pygame.transform.smoothscale(quit_img, (400, 80)), (400, 432))
    return main_menu_command


# LEADERBOARD
def leaderboard(window):
    """Gets the window on which the leaderboard screen needs to be shown and block transfers (blits) the required images
    on it. Data in txt file is stored in dictionary form. From dictionary, 'easy wins' and 'hard wins' are used to
    calculate 'total wins' on whose basis the winners in leaderboard are sorted. The data in txt file is turned into a
    list, sorted and displayed accordingly on the blitted board
    Arguments
    ---------
    window : Display Surface
        The surface on which all screens will be shown
    Return
    ------
    play_game_command : string
        A string is returned according to the command chosen by the user"""

    board = pygame.image.load("images/Artboard (1).png")
    board = pygame.transform.smoothscale(board, (1000, 400))
    main_font = pygame.font.Font("fonts/Cute Little Sheep.ttf", 32)
    # Getting mouse position in the form (x, y)
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    window.blit(board, (150, 100))
    with open('data\\players_data.txt') as players_data:
        data_list = []
        for i in players_data:
            # eval() used to remove the quotations, turn string to dictionary, append dictionary to list.
            data_list.append(eval(i))
        total_wins_list = []
        for i in data_list:
            # total wins calculated with the help of 'easy wins' and 'hard wins' and appended to the the existing list and new list of total wins
            i['total_wins'] = i['easy_wins'] + i['hard_wins']
            total_wins_list.append(i['easy_wins'] + i['hard_wins'])

        # Sorting the values of total_wins_list in the data_list2 lis
        length = len(total_wins_list)
        data_list2 = []
        for i in range(length):
            # index of highest total wins used to sort the winners
            index = total_wins_list.index(max(total_wins_list))
            x = data_list.pop(index)
            data_list2.insert(i, x)
            total_wins_list.remove(max(total_wins_list))

    y = 150
    for i in data_list2:
        msg = main_font.render(
            f"Name: {i['name']},   Easy Wins: {i['easy_wins']},   Hard Wins: {i['hard_wins']},   Total Wins: "
            f"{i['total_wins']}",
            True, (255, 185, 0))
        window.blit(msg, (250, y))
        # display each winner one by one, in next line
        y += 40

    if 200 <= mouse[0] <= 280 and 432 <= mouse[1] <= 512:
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (190, 422))
        if mouse_clicked():
            play_game_command = 'backward'
    else:
        window.blit(backward_img, (200, 432))
    # Incase the user does not choose any other command, the variable play_game_command is still defined to avoid runtime error
    if 'play_game_command' not in locals():
        play_game_command = None

    return play_game_command


def play_game(window, difficulty_level):
    """Gets the difficulty and the window on which the play game screen needs to be shown and block transfers (blits) the required images
    on it. It will return the difficulty level chosen by the user.
    Arguments
    ---------
    window : Display Surface
        The surface on which all screens will be shown
    difficulty_level : string or keyword
        It will either be None, 'easy' or 'hard'.
    Return
    ------
    difficulty : string or keyword
        It is either None, 'easy' or 'hard' depending on the option selected by the user.
    play_game_command : string or keyword
        None or a string is returned according to the option chosen by the user."""
    difficulty = difficulty_level
    # Getting mouse position in the form (x, y)
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    window.blit(pygame.transform.smoothscale(difficulty_lvl_img, (400, 80)), (400, 132))
    # If the mouse is hovering within the given coordinates the image transforms into a larger version of itself
    if 400 <= mouse[0] <= 800 and 232 <= mouse[1] <= 312:
        window.blit(diff_easy_img, (350, 222))
        # If the mouse is clicked within the given coordinates, the variables difficulty and play_game_command are
        # assigned strings or None according to the image clicked
        if mouse_clicked():
            difficulty = 'easy'
    # This else condition will blit the image if no mouse is hovering over those coordinates
    else:
        if difficulty == 'easy':
            window.blit(diff_easy_img, (350, 222))
        else:
            window.blit(pygame.transform.smoothscale(diff_easy_img, (400, 80)), (400, 232))
    if 400 <= mouse[0] <= 800 and 332 <= mouse[1] <= 412:
        window.blit(diff_hard_img, (350, 322))
        if mouse_clicked():
            difficulty = 'hard'
    else:
        if difficulty == 'hard':
            window.blit(diff_hard_img, (350, 322))
        else:
            window.blit(pygame.transform.smoothscale(diff_hard_img, (400, 80)), (400, 332))
    if 400 <= mouse[0] <= 480 and 432 <= mouse[1] <= 512:
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (390, 422))
        if mouse_clicked():
            play_game_command = 'backward'
            difficulty = None
    else:
        window.blit(backward_img, (400, 432))
    if 720 <= mouse[0] <= 800 and 432 <= mouse[1] <= 512 and (difficulty == 'easy' or difficulty == 'hard'):
        window.blit(pygame.transform.smoothscale(forward_img, (100, 100)), (710, 422))
        if mouse_clicked():
            play_game_command = 'forward'
    else:
        window.blit(forward_img, (720, 432))
    # Incase the user chooses a command where play_game_command is not defined, the variable play_game_command will be defined here to avoid runtime error
    if 'play_game_command' not in locals():
        play_game_command = None
    return difficulty, play_game_command


def player_selection(window, num):
    """Gets the number of players (initially they are None) and the window on which the player selection screen needs to
     be shown and block transfers (blits) the required images on it. It will return the number of players the user selects.
    Arguments
    ---------
    window : Display Surface
        The surface on which all screens will be shown
    num : integer or keyword
        The number of players
    Return
    ------
    players_num : integer or keyword
        The total number of players chosen by the user
    player_selection_command : string or keyword
        None or a string is returned according to the option chosen by the user."""
    players_num = num
    # Getting mouse position in the form (x, y)
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    # If the mouse is hovering within the given coordinates the image transforms into a larger version of itself
    if 400 <= mouse[0] <= 800 and 132 <= mouse[1] <= 212:
        window.blit(two_players_img, (350, 122))
        # If the mouse is clicked within the given coordinates, the variables player_num and player_selection_command
        # are assigned a string or None according to the image clicked
        if mouse_clicked():
            players_num = 2
    # This else condition will blit the image if not mouse is hovering over those coordinates
    else:
        if players_num == 2:
            window.blit(two_players_img, (350, 122))
        else:
            window.blit(pygame.transform.smoothscale(two_players_img, (400, 80)), (400, 132))
    if 400 <= mouse[0] <= 800 and 232 <= mouse[1] <= 312:
        window.blit(three_players_img, (350, 222))
        if mouse_clicked():
            players_num = 3
    else:
        if players_num == 3:
            window.blit(three_players_img, (350, 222))
        else:
            window.blit(pygame.transform.smoothscale(three_players_img, (400, 80)), (400, 232))
    if 400 <= mouse[0] <= 800 and 332 <= mouse[1] <= 412:
        window.blit(four_players_img, (350, 322))
        if mouse_clicked():
            players_num = 4
    else:
        if players_num == 4:
            window.blit(four_players_img, (350, 322))
        else:
            window.blit(pygame.transform.smoothscale(four_players_img, (400, 80)), (400, 332))
    if 400 <= mouse[0] <= 480 and 432 <= mouse[1] <= 512:
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (390, 422))
        if mouse_clicked():
            player_selection_command = 'backward'
            players_num = None
    else:
        window.blit(backward_img, (400, 432))
    if 720 <= mouse[0] <= 800 and 432 <= mouse[1] <= 512 and (players_num in [2, 3, 4]):
        window.blit(pygame.transform.smoothscale(forward_img, (100, 100)), (710, 422))
        if mouse_clicked():
            player_selection_command = 'forward'
    else:
        window.blit(forward_img, (720, 432))
    # In case the user chooses a command where player_selection_command is not defined, the variable
    # player_selection_command will be defined here to avoid runtime error
    if 'player_selection_command' not in locals():
        player_selection_command = None
    return players_num, player_selection_command


def player_login(window, current_player, username, username_selected):
    """Allows the user to enter the name of the player.
    Arguments
    ---------
    window : Display Surface
        The surface on which all screen will be shown
    current_player : int
        Tells the program the current number of player so that it can blit image according to that.
    username : string
        The name of the player (continuously updates with the user input)
    username_selected : Boolean
        Tells if the textbox is selected or not
    Return
    ------
    player_login_command : string or keyword
        None or a string is returned according to the choice of the user
    username : string
        The name of the player entered by the user
    username_selected : Boolean
        Tells if the textbox is selected or not"""
    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    # Getting mouse position in the form (x, y)
    mouse = pygame.mouse.get_pos()
    # If the mouse button is pressed within the coordinates of the textbox, the user_selected will be assigned a value
    # of True. If the the mouse is clicked elsewhere the user_selected will be assigned a value of False.
    if 133 <= mouse[0] <= 533 and 332 <= mouse[1] <= 412 and mouse_clicked():
        username_selected = True
    elif not (666 <= mouse[0] <= 1066 and 97 <= mouse[1] <= 577):
        if mouse_clicked():
            username_selected = False
    window.blit(pygame.transform.smoothscale(player_num_img[current_player - 1], (400, 80)), (133, 132))
    window.blit(pygame.transform.smoothscale(textbox_img, (400, 80)), (133, 232))
    window.blit(pygame.transform.smoothscale(textbox_img, (400, 80)), (133, 332))
    # This loop will blit the the alphabets on the screen and username can be altered by pressing these letters. The
    # image of letter will alter if the mouse pointer is hovering over it.
    for i in range(26):
        if letters_data[i][0] <= mouse[0] <= letters_data[i][0] + 80 and letters_data[i][1] <= mouse[1] <= \
                letters_data[i][1] + 80:
            window.blit(letter1_imgs[i], (letters_data[i][0], letters_data[i][1]))
            if mouse_clicked() and username_selected and len(username) <= 12:
                username += letters_data[i][2]
        else:
            window.blit(letter_imgs[i], (letters_data[i][0], letters_data[i][1]))
    # This conditional statement will change the colour of text according to the value of username_selected.
    if username_selected:
        text_color = selected_color
    else:
        text_color = deselected_color
    rendered_username = text_font.render('User: ' + username, True, text_color)
    window.blit(rendered_username, (148, 340))
    character_limit = text_font.render('Character Limit: 12', True, deselected_color)
    window.blit(character_limit, (173, 240))
    # The size of the button's image will change if the mouse is hovering over it. The variables are assigned the values
    # according to the buttons that user presses.
    if 133 <= mouse[0] <= 213 and 432 <= mouse[1] <= 512:
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (123, 422))
        if mouse_clicked():
            player_login_command = 'backward'
            username = ''
    else:
        window.blit(backward_img, (133, 432))
    if 443 <= mouse[0] <= 523 and 432 <= mouse[1] <= 512 and len(username) > 0:
        window.blit(pygame.transform.smoothscale(forward_img, (100, 100)), (433, 422))
        if mouse_clicked():
            player_login_command = 'forward'
    else:
        window.blit(forward_img, (443, 432))
    # In case the user chooses a command where player_selection_command is not defined, the variable
    # player_selection_command will be defined here to avoid runtime error
    if 'player_login_command' not in locals():
        player_login_command = None
    return player_login_command, username, username_selected


def game_over(window, winner):
    """Gets the winner of the current game and the window on which the game over screen needs to be shown and block transfers (blits) the required images
    on it. It will return the command chosen by the user.
    Arguments
    ---------
    window : Display Surface
        The surface on which all screens will be shown
    winner : string
        The username of the player that won the current game
    Return
    ------
    game_over_command : string or keyword
        None or a string is returned according to the option chosen by the user."""
    # Getting the position of the mouse in the form (x, y)
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    # Showing the winner of the game on the screen
    winner_text = text_font.render(f"{winner} wins!!", True, selected_color)
    window.blit(pygame.transform.smoothscale(textbox_img, (400, 80)), (400, 237))
    window.blit(winner_text, (600 - (winner_text.get_width() / 2), 247))
    if 560 <= mouse[0] <= 640 and 327 <= mouse[1] <= 407:
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (550, 327))
        if mouse_clicked():
            game_over_command = 'backward'
    else:
        window.blit(backward_img, (560, 337))
    # In case the user chooses a command where game_over_command is not defined, the variable game_over_command
    # will be defined here to avoid runtime error
    if 'game_over_command' not in locals():
        game_over_command = None
    return game_over_command
