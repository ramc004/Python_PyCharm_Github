import random
import pygame
current_time = 0

# The point of time at which the bag is clicked.
bag_clicked_time = 0

death_note_font = pygame.font.Font("fonts/Death_Note_Font.ttf", 48)
# Initializing pygame
pygame.init()
# Loading the required images.
bag_img = pygame.image.load("images/bag.png")
tokens_img = {'death': pygame.image.load("images/tokens/death.png"), '1': pygame.image.load("images/tokens/1.png"),
              '-6': pygame.image.load("images/tokens/-6.png"), '-5': pygame.image.load("images/tokens/-5.png"),
              '-4': pygame.image.load("images/tokens/-4.png"), '-3': pygame.image.load("images/tokens/-3.png"),
              '-2': pygame.image.load("images/tokens/-2.png"), '-1': pygame.image.load("images/tokens/-1.png"),
              '6': pygame.image.load("images/tokens/6.png"), '5': pygame.image.load("images/tokens/5.png"),
              '4': pygame.image.load("images/tokens/4.png"), '3': pygame.image.load("images/tokens/3.png"),
              '2': pygame.image.load("images/tokens/2.png"), 'chances': pygame.image.load("images/tokens/chances.png"),
              '0': pygame.image.load("images/tokens/0.png")}


def chaos_bag(level, players_num):
    """Gets the difficulty level of the game and the number of players and returns a token based on them.
    Arguments
    ---------
    level : string
        The difficulty level of the game. It's either 'easy' or 'hard'.
    players_num : int
        Total number of players in the game.
    Return
    ------
    token[0] : int
        The token is an integer"""
    all_tokens = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    if level == 'easy':
        token = random.choices(all_tokens, weights=[4, 4, 4, 6, 6, 6, 8, 8, 8, 10, 10, 10, 12], k=1)
    elif level == 'hard':
        token = random.choices(all_tokens, weights=[5, 5, 6, 6, 7, 7, 8, 10, 10, 8, 8, 8, 8], k=1)
    # Since random.choices() will return a list so we get the integer out of it by by calling its first index.
    return token[0]


def main(window, difficulty, total_players, token, total_turns, in_movement):
    """This function displays the chaos bag on the screen and when the chaos bag is clicked, appropriate token images is
    shown on the screen and the token integer is returned.
    Arguments
    ---------
    window : Display Surface
        The surface on which all screens are blitted.
    difficulty : string
        The difficulty level of the game. It's either 'easy' or 'hard'.
    total_players : int
        The total number of players in the current game.
    token : int
        The token returned by the chaos bag.
    total_turns : int
        The total number turns in a single game. It increases by 1 whenever chaos bag is clicked.
    in_movement : Boolean
        Tells if any bead is in movement or not. Chaos bag will be disabled as long as this is true.
    Return
    ------
    token : int
        The token returned by the chaos bag.
    total_turns : int
        The total number turns in a single game. It increases by 1 whenever chaos bag is clicked.
    bag_clicked : Boolean
        Tells if the chaos bag was clicked or not."""
    def mouse_clicked():
        """This function will return True if the mouse is clicked."""
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True

    current_time = pygame.time.get_ticks()
    bag_clicked = False
    mouse = pygame.mouse.get_pos()
    # The size of the buttons' and chaos bag images will change when the mouse pointer is hovering over them.
    if 100 <= mouse[0] <= 400 and 100 <= mouse[1] <= 400:
        bag_x = 75
        bag_y = 75
        if not in_movement:
            if mouse_clicked():
                global bag_clicked_time
                bag_clicked_time = pygame.time.get_ticks()
                token = chaos_bag(difficulty, total_players)
                total_turns += 1
                bag_clicked = True
        if token is not None and current_time - bag_clicked_time < 180:
            bag_x = 80
            bag_y = 80
        window.blit(pygame.transform.smoothscale(bag_img, (350, 350)), (bag_x, bag_y))
    else:
        window.blit(pygame.transform.smoothscale(bag_img, (300, 300)), (100, 100))
    # Blitting the token image on the screen.
    if token is not None and current_time - bag_clicked_time < 3000:
        window.blit(pygame.transform.smoothscale(tokens_img[f'{token}'], (200, 200)), (150, 450))
    return token, total_turns, bag_clicked
