import pygame
import menu_screens as menu
import gameplay
import instructions

# Initializing pygame
pygame.mixer.init()
# Loading the required data
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
pygame.init()
window = pygame.display.set_mode((1200, 675))
clock = pygame.time.Clock()
window_height = window.get_height()
window_width = window.get_width()
main_bg_file = pygame.image.load("images/main bg.png")
main_bg = pygame.transform.smoothscale(main_bg_file, (1200, 675))

# Reading the data and creating a list of dictionaries where each dictionary corresponds to a specific player.
with open('data/players_data.txt') as data_file:
    data_text = data_file.readlines()
data = [eval(i) for i in data_text]


def player_existence(name, data_list):
    "This function returns true if name is present in any of the dictionary in data_list"
    existence = False
    for i in data_list:
        if i['name'] == name:
            existence = True
            break
    return existence


pygame.display.set_caption("Snakes & Ladders")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Assigning the initial variables.
current_screen = 'main_menu'
difficulty = None
total_players = None
current_player = 1
current_game_players = []

username = ''
username_selected = False
token = None
in_movement = False
game_finished = False
winner = None

running = True
# Start of loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(main_bg, (0, 0))

    # MAIN MENU SCREEN
    if current_screen == 'main_menu':
        main_menu_command = menu.main(window)
        if main_menu_command == 'quit':
            quit()
        elif main_menu_command == 'play game':
            current_screen = 'play game'
        elif main_menu_command == 'instructions':
            current_screen = 'instructions'
        elif main_menu_command == 'leaderboard':
            current_screen = 'leaderboard'

    # PLAY GAME SCREEN
    if current_screen == 'play game':
        difficulty, play_game_command = menu.play_game(window, difficulty)
        if play_game_command == 'backward':
            current_screen = 'main_menu'
        elif play_game_command == 'forward':
            current_screen = 'player_selection_menu'

    # PLAYER SELECTION SCREEN
    if current_screen == 'player_selection_menu':
        total_players, players_selection_command = menu.player_selection(window, total_players)
        if players_selection_command == 'backward':
            current_screen = 'play game'
        elif players_selection_command == 'forward':
            current_screen = 'login_menu'

    # LEADERBOARD
    if current_screen == 'leaderboard':
        leaderboard_command = menu.leaderboard(window)
        if leaderboard_command == 'backward':
            current_screen = 'main_menu'

    # INSTRUCTIONS
    if current_screen == 'instructions':
        current_screen = instructions.instructions(window, current_screen)

    # LOGIN MENU
    if current_screen == 'login_menu':
        player_login_command, username, username_selected = menu.player_login(window, current_player, username,
                                                                              username_selected)
        if player_login_command == 'forward':
            current_game_players.append(username)
            current_player += 1
            username = ''
        elif player_login_command == 'backward':
            current_game_players = current_game_players[0: -1]
            if current_player == 1:
                current_screen = 'player_selection_menu'
            else:
                current_player -= 1
        if current_player > total_players:
            current_screen = 'gameplay'
            current_game_players = [{'name': i, 'current_pos': (0, 0), 'temp_box': 1,
                                     'new_box': 1} for i in current_game_players]

    # GAMEPLAY
    if current_screen == 'gameplay':
        if difficulty == 'easy':
            token, in_movement, game_finished, winner = gameplay.easy_game(window, token, current_game_players,
                                                                           in_movement)
            if game_finished:
                current_screen = 'game_over'
                winner_exists = False
                for i in data:
                    if winner == i['name']:
                        winner_exists = True
                        break
                if not winner_exists:
                    data.append({'name': winner, 'easy_wins': 0, 'hard_wins': 0})
                for i in data:
                    if winner == i['name']:
                        i['easy_wins'] += 1
        elif difficulty == 'hard':
            token, in_movement, game_finished, winner = gameplay.hard_game(window, token, current_game_players,
                                                                           in_movement)
            if game_finished:
                current_screen = 'game_over'
                winner_exists = False
                for i in data:
                    if winner == i['name']:
                        winner_exists = True
                        break
                if not winner_exists:
                    data.append({'name': winner, 'easy_wins': 0, 'hard_wins': 0})
                for i in data:
                    if winner == i['name']:
                        i['hard_wins'] += 1

    # GAME OVER
    if current_screen == 'game_over':
        with open("data/players_data.txt", mode='w') as file:
            for i in data:
                file.write(f"{str(i)}\n")
        game_over_command = menu.game_over(window, winner)
        if game_over_command == 'backward':
            current_screen = 'main_menu'
            total_players = None
            current_game_players = []
            username = ''
            username_selected = False
            token = None
            in_movement = False
            game_finished = False
            winner = None
            difficulty = None
            current_player = 1
    pygame.display.update()
    clock.tick(60)
