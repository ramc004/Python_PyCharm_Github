import pygame

# Initiating pygame
pygame.init()
# Loading required images
main_bg_file = pygame.image.load("images/main bg.png")
board = pygame.image.load("images/Artboard (1).png")
empty_box = pygame.image.load("images/Artboard.png")
backward_img = pygame.image.load("images/backward.png")
forward_img = pygame.image.load("images/forward.png")
main_font = pygame.font.Font("fonts/Cute Little Sheep.ttf", 36)
main_font_big = pygame.font.Font("fonts/Cute Little Sheep.ttf", 46)
instructions_img = pygame.image.load("images/instructions.png")


def game_rules(window):
    """Gets the window on which the game rules need to be shown and block transfers (blits) it there."""

    # Rendering the text so it can be blit on the screen later
    msg1 = main_font_big.render('Game Rules :', True, (255, 165, 0))
    window.blit(msg1, (60, 150))
    msg = ['1. Each player will be assigned a color and all the counters will start from the ',
           'bottom left corner of the board.',
           '2. Each player will take turns on the chaos bag. The number that the chaos',
           'bag gives is the number of squares your center will move.',
           '3. If your counter lands on the bottom of a ladder, it will move up to the top', 'of the ladder.',
           '4. If your counter lands on the head of a snake, it will slide down to the bottom', 'of the snake.',
           "5. The game ends when one player reaches the 'Finish' box."]

    # Making a list of the rendered font
    msg_render = [main_font.render(x, True, (255, 185, 0)) for x in msg]

    # Blitting the rendered text on different coordinates according to requirement
    y = 0
    for i in msg_render:
        window.blit(i, (60, 200 + y))
        y += 40


def chaos_bag_info(window):
    """Gets the window on which the information regarding chaos bag and leaderboard need to be shown and
    block transfers (blits) it there."""

    msg1 = main_font_big.render('Chaos Bag :', True, (255, 165, 0))
    msg2 = main_font_big.render('Leaderboard : ', True, (255, 165, 0))
    window.blit(msg1, (50, 150))
    window.blit(msg2, (50, 315))
    msg = ['In this version of the game, a chaos bag has been introduced instead of the dice.',
           'To get a number, click on the bag.', 'The numbers can range from -6 to 6',
           " ",
           'Before you can play the game , you will be asked to enter a playername.',
           "Click the word 'User' to enter player name.",
           'All your wins and losses will be recorded under this playername.',
           "The playernames and scores will be shown in descending order once you click",
           "on the 'Leaderboard' option."]
    msg_render = [main_font.render(x, True, (255, 185, 0)) for x in msg]
    y = 0
    for i in msg_render:
        window.blit(i, (60, 200 + y))
        y += 40


def levels(window):
    """Gets the window on which the information regarding levels needs to be shown and block transfers (blits)
     it there."""

    msg1 = main_font_big.render('Levels :', True, (255, 165, 0))
    window.blit(msg1, (60, 150))
    msg = ['1.  Easy Level :', 'In this level the board is 6x6.', 'The player to reach Finish on box 36 wins.', " ",
           '2.  Hard Level :', 'In this level the board is 10x10.', 'The player to reach Finish on box 100 wins.']
    msg_render = [main_font.render(x, True, (255, 185, 0)) for x in msg]
    y = 0
    for i in msg_render:
        window.blit(i, (60, 200 + y))
        y += 40


def instructions_1(window):
    """This function gets the window on which the instructions need to be shown and block transfers (blits) the required
     images and text to show the first screen of instructions. It returns the screen the user wants to visit next."""
    instruction_screen = 'instructions'
    # Getting mouse position in the form (x, y)
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    # Blitting the instructions header and the empty background box
    window.blit(pygame.transform.smoothscale(instructions_img, (400, 80)), (400, 20))
    window.blit(pygame.transform.smoothscale(board, (1180, 540)), (10, 110))
    # Calling the function to write the required information
    game_rules(window)
    # If the mouse is hovering within the given coordinates the image transforms into a larger version of itself
    if 1080 <= mouse[0] <= (1080 + 80) and 570 <= mouse[1] <= (570 + 80):
        window.blit(pygame.transform.smoothscale(forward_img, (100, 100)), (1080, 570))
        # If the mouse is clicked within the given coordinates then there will be a change in screens
        if mouse_clicked():
            instruction_screen = 'instructions2'
    # This else condition will blit the image if no mouse is hovering over those coordinates
    else:
        window.blit(forward_img, (1080, 570))

    if 40 <= mouse[0] <= (40 + 390) and 570 <= mouse[1] <= (570 + 80):
        window.blit(pygame.transform.smoothscale(empty_box, (320, 90)), (40, 570))
        if mouse_clicked():
            instruction_screen = 'main menu'
    else:
        window.blit(pygame.transform.smoothscale(empty_box, (300, 80)), (40, 570))
    msg = main_font.render('Back to Main Menu', True, (255, 165, 0))
    window.blit(msg, (60, 580))
    return instruction_screen


def instructions_2(window):
    """This function gets the window on which the instructions need to be shown and block transfers (blits) the required
     images and text to show the second screen of instructions. It returns the screen the user wants to visit next."""
    instruction_screen = 'instructions2'
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    window.blit(pygame.transform.smoothscale(instructions_img, (400, 80)), (400, 20))
    window.blit(pygame.transform.smoothscale(board, (1180, 540)), (10, 110))
    chaos_bag_info(window)
    if 1080 <= mouse[0] <= (1080 + 80) and 570 <= mouse[1] <= (570 + 80):
        window.blit(pygame.transform.smoothscale(forward_img, (100, 100)), (1080, 570))
        if mouse_clicked():
            instruction_screen = 'instructions3'
    else:
        window.blit(forward_img, (1080, 570))
    if 40 <= mouse[0] <= (40 + 80) and 570 <= mouse[1] <= (570 + 80):
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (40, 570))
        if mouse_clicked():
            instruction_screen = 'instructions1'
    else:
        window.blit(backward_img, (40, 570))
    return instruction_screen


def instructions_3(window):
    """This function gets the window on which the instructions need to be shown and block transfers (blits) the required
     images and text to show the third screen of instructions. It returns the screen the user wants to visit next."""
    instruction_screen = 'instructions3'
    mouse = pygame.mouse.get_pos()

    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    window.blit(pygame.transform.smoothscale(instructions_img, (400, 80)), (400, 20))
    window.blit(pygame.transform.smoothscale(board, (1180, 540)), (10, 110))
    levels(window)
    if 40 <= mouse[0] <= (40 + 80) and 570 <= mouse[1] <= (570 + 80):
        window.blit(pygame.transform.smoothscale(backward_img, (100, 100)), (40, 570))
        if mouse_clicked():
            instruction_screen = 'instructions2'
    else:
        window.blit(backward_img, (40, 570))
    return instruction_screen


def bckground(window):
    """Gets the screen and block transfers the background image on it."""
    window.blit(main_bg_file, (0, 0))


def instructions(window, inst_screen):
    """Gets the window on which the instructions need to be shown and the current command by the user. A while loop is
    used to go back and forth between the instruction screens. If the user decides to go back to the main menu screen,
    the string 'main_menu' is returned and the while loop breaks.
    Arguments
    ---------
    window : Display Surface
        The surface on which all screens will be shown
    inst_screen : string
        The string will be according to the command chosen by the user
    Return
    --------
    main_screen : string
        The string returned is 'main menu'."""
    run = True
    while run:
        bckground(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        if inst_screen == 'instructions':
            inst_screen = instructions_1(window)
        if inst_screen == 'instructions2':
            inst_screen = instructions_2(window)
        elif inst_screen == 'main menu':
            break

        if inst_screen == 'instructions3':
            inst_screen = instructions_3(window)
        elif inst_screen == 'instructions1':
            inst_screen = instructions_1(window)

        pygame.display.update()
    main_screen = 'main_menu'
    return main_screen
