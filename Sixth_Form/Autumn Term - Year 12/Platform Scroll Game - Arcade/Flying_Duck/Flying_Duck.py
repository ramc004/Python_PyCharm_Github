import pygame
import sys
import math
import random
import os


frame_time = 0.0


def text_to_fixed_width(text, width):
    """ checks if length of text is more than width then creates the text for the window """
    if len(text) > width:
        return text[:width]

    return text + " " * (width - len(text))


def prepare_image(image, transparent_color=None, transparency_mask=None):
    """ creates the background for the window
    uses alpha to convert the image from the folder so it can be used for the start of the game """
    result = pygame.Surface.convert(image)

    if transparency_mask != None:
        result = pygame.Surface.convert_alpha(result)

        for y in range(image.get_height()):
            for x in range(image.get_width()):
                color = image.get_at((x, y))
                alpha = transparency_mask.get_at((x, y))

                color.a = alpha.r
                result.set_at((x, y), color)

    elif transparent_color != None:
        result = pygame.Surface.convert_alpha(result)

        for y in range(image.get_height()):
            for x in range(image.get_width()):
                color = image.get_at((x, y))

                if color == transparent_color:
                    color.a = 0
                    result.set_at((x, y), color)

    return result


class MapGridObject:
    """ creates different numbers for each object to make it easier to call them later on
    tiles for each window are set
    collectibles for each level, eggs and coins
    creates variables for duck flying so the image knows when to change
    duck falling to ground
    what happens when hit spikes
    creates a high bounce tile that allows the duck to bounce higher"""
    OBJECT_TILE = 0
    OBJECT_FINISH = 1
    OBJECT_TRAMPOLINE = 2
    OBJECT_COIN = 3
    OBJECT_EGG = 4
    OBJECT_ENEMY_FLYING = 5
    OBJECT_ENEMY_GROUND = 6
    OBJECT_PLAYER = 7
    OBJECT_SPIKES = 8

    def is_tile(self):
        """ uses the object type, tiles
        and sets it equal to where the map has placed it on the grid """
        return self != None and (
                self.object_type == MapGridObject.OBJECT_TILE or self.object_type
                == MapGridObject.OBJECT_TRAMPOLINE)

    def get_instance_from_string(self):
        
        if self == ".":
            return None

        result = MapGridObject()

        if self[0] == "X":
            result.object_type = MapGridObject.OBJECT_FINISH
        elif self[0] == "E":
            result.object_type = MapGridObject.OBJECT_EGG
        elif self[0] == "C":
            result.object_type = MapGridObject.OBJECT_COIN
        elif self[0] == "P":
            result.object_type = MapGridObject.OBJECT_PLAYER
        elif self[0] == "T":
            result.object_type = MapGridObject.OBJECT_TRAMPOLINE
        elif self[0] == "S":
            result.object_type = MapGridObject.OBJECT_SPIKES
        elif self[0] == "F":
            result.object_type = MapGridObject.OBJECT_ENEMY_FLYING
            result.enemy_id = int(self[2:])
        elif self[0] == "G":
            result.object_type = MapGridObject.OBJECT_ENEMY_GROUND
            result.enemy_id = int(self[2:])
        else:
            result.object_type = MapGridObject.OBJECT_TILE
            helper_list = self.split(";")
            result.tile_id = int(helper_list[0])
            result.tile_variant = int(helper_list[1])

        return result

    def __init_attributes(self):
        self.object_type = MapGridObject.OBJECT_TILE
        self.tile_id = 0
        self.tile_variant = 1
        self.enemy_id = 0

    def __str__(self):
        if self.object_type == MapGridObject.OBJECT_TILE:
            return "t"
        if self.object_type == MapGridObject.OBJECT_COIN:
            return "C"
        if self.object_type == MapGridObject.OBJECT_EGG:
            return "E"
        if self.object_type == MapGridObject.OBJECT_PLAYER:
            return "P"
        if self.object_type == MapGridObject.OBJECT_ENEMY_FLYING:
            return "F"
        if self.object_type == MapGridObject.OBJECT_ENEMY_GROUND:
            return "G"
        if self.object_type == MapGridObject.OBJECT_FINISH:
            return "F"
        return "?"

    def __init__(self):
        self.__init_attributes()
        return


class Level:
    STATE_PLAYING = 0
    STATE_WON = 1
    STATE_LOST = 2

    def load_from_file(self, filename):
        self.filename = filename

        with open(filename) as input_file:
            content = input_file.readlines()

        for i in range(len(content)):
            content[i] = ((content[i])[:-1]).rstrip()

        line_number = 0

        while line_number < len(content):
            if content[line_number] == "name:":
                line_number += 1
                self.name = content[line_number]
            elif content[line_number] == "background:":
                line_number += 1
                self.background_name = content[line_number]
                line_number += 1
                self.background_color = pygame.Color(content[line_number])
            elif content[line_number].rstrip() == "tiles:":
                while True:
                    line_number += 1
                    if line_number >= len(content) or len(content[line_number]) == 0:
                        break

                    helper_list = content[line_number].split()
                    self.tiles.append((int(helper_list[0]), helper_list[1], int(helper_list[2])))

            elif content[line_number] == "outside:":
                line_number += 1
                self.outside_tile = MapGridObject()
                self.outside_tile.object_type = MapGridObject.OBJECT_TILE
                self.outside_tile.tile_id = int(content[line_number])
                self.outside_tile.tile_variant = 1

            elif content[line_number] == "scores:":
                line_number += 1

                while True:
                    if line_number >= len(content):
                        break

                    split_line = content[line_number].split()

                    if len(split_line) != 3:
                        break

                    self.scores.append((split_line[0], int(split_line[1]), int(split_line[2])))
                    line_number += 1

                line_number -= 1

                self._sort_scores()

            elif content[line_number] == "map:":
                line_number += 1
                helper_list = content[line_number].split()
                self.width = int(helper_list[0])
                self.height = int(helper_list[1])
                self.map_array = [[None] * self.height for item in range(self.width)]
                pos_y = 0

                while True:
                    line_number += 1

                    if line_number >= len(content) or len(content[line_number]) == 0:
                        break

                    helper_list = content[line_number].split()

                    for pos_x in range(len(helper_list)):

                        helper_object = MapGridObject.get_instance_from_string(helper_list[pos_x])

                        if helper_object == None:
                            self.map_array[pos_x][pos_y] = helper_object
                        elif helper_object.object_type == MapGridObject.OBJECT_PLAYER:
                            self.player = Player(self)
                            self.player.position_x = pos_x + 0.5
                            self.player.position_y = pos_y + 0.5
                        elif helper_object.object_type == MapGridObject.OBJECT_ENEMY_FLYING:
                            self.enemies.append(Enemy(self, Enemy.ENEMY_FLYING))
                            self.enemies[-1].position_x = pos_x + 0.5
                            self.enemies[-1].position_y = pos_y + 0.5
                        elif helper_object.object_type == MapGridObject.OBJECT_ENEMY_GROUND:
                            self.enemies.append(Enemy(self, Enemy.ENEMY_GROUND))
                            self.enemies[-1].position_x = pos_x + 0.5
                            self.enemies[-1].position_y = pos_y + 0.5
                        else:
                            if helper_object.object_type == MapGridObject.OBJECT_EGG:
                                self.eggs_left += 1
                            elif helper_object.object_type == MapGridObject.OBJECT_COIN:
                                self.coins_total += 1

                            self.map_array[pos_x][pos_y] = helper_object

                    pos_y += 1

            line_number += 1

    def save_scores(self):
        if len(self.filename) == 0:
            return

        output_lines = []

        input_file = open(self.filename)

        for line in input_file:
            if line.lstrip().rstrip() == "scores:":
                break
            else:
                output_lines.append(line)

        input_file.close()

        output_file = open(self.filename, "w")

        for line in output_lines:
            output_file.write(line)

        output_file.write("scores:\n")

        for score in self.scores:
            output_file.write(score[0] + " " + str(score[1]) + " " + str(score[2]) + "\n")

        output_file.close()

    def add_score(self, name, time, score):
        if len(self.scores) < 20:
            self.scores.append((name, score, time))
        else:
            minimum_index = 0
            i = 0

            while len(self.scores):
                if self.scores[i][1] < self.scores[minimum_index][1]:
                    minimum_index = i

                i += 1

            if self.scores[minimum_index][1] < score:
                del self.scores[minimum_index]
                self.scores.append((name, score, time))
                self._sort_scores()

    def _sort_scores(self):
        self.scores.sort(key=lambda item: item[1], reverse=True)

    def update(self):
        player_tile_x = int(self.player.position_x)
        player_tile_y = int(self.player.position_y)

        self.time = pygame.time.get_ticks() - self._time_start

        object_at_player_tile = self.get_at(player_tile_x, player_tile_y)
        object_under_player_tile = self.get_at(player_tile_x, player_tile_y + 1)

        if object_at_player_tile != None:
            if object_at_player_tile.object_type == MapGridObject.OBJECT_COIN:
                self.sound_player.play_coin()
                self.map_array[player_tile_x][player_tile_y] = None
                self.coins_collected += 1
            elif object_at_player_tile.object_type == MapGridObject.OBJECT_EGG:
                self.sound_player.play_click()
                self.map_array[player_tile_x][player_tile_y] = None
                self.eggs_left -= 1
            elif object_at_player_tile.object_type == MapGridObject.OBJECT_FINISH:
                if self.eggs_left <= 0:
                    self.state = Level.STATE_WON
                    self.add_score(self.game.name, pygame.time.get_ticks() - self._time_start, self.score)
                    self.save_scores()
                    self.player.force_computer.velocity_vector[0] = 0
                    self.sound_player.play_win()
            elif object_at_player_tile.object_type == MapGridObject.OBJECT_SPIKES:
                self.set_lost()
                return

        if object_under_player_tile != None and object_under_player_tile.object_type == MapGridObject.OBJECT_TRAMPOLINE\
                and not self.player.is_in_air():
            self.player.force_computer.velocity_vector[1] = -10
            self.sound_player.play_trampoline()
        self.score = int(20000000.0 / (pygame.time.get_ticks() - self._time_start + 20000)) + self.coins_collected * 200

        for enemy in self.enemies:
            if self.player.collides(enemy):
                self.set_lost()

    def set_lost(self):
        if self.state == Level.STATE_LOST:
            return

        self.player.last_quack_time = -99999
        self.player.quack()

        self.state = Level.STATE_LOST
        self.player.solid = False
        self.player.force_computer.velocity_vector[0] = -1
        self.player.force_computer.velocity_vector[1] = -4
        self.player.force_computer.acceleration_vector[0] = 0
        self.player.force_computer.ground_friction = 0

    def __init_attributes(self):
        self.filename = ""
        self.game = None
        self.name = ""
        self.score = 0
        self.scores = []
        self.state = Level.STATE_PLAYING
        self.coins_total = 0
        self.coins_collected = 0
        self.eggs_left = 0
        self.background_name = ""
        self.background_color = None
        self.tiles = []
        self.width = 0
        self.height = 0
        self.map_array = None
        self.outside_tile = None
        self.player = None
        self.enemies = []
        self.sound_player = None
        self.gravity = 4.7
        self.time = 0
        self._time_start = pygame.time.get_ticks()

    def get_at(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.outside_tile

        return self.map_array[x][y]

    def __init__(self, game):
        self.__init_attributes()
        self.sound_player = game.sound_player
        self.game = game


class Movable(object):
    def __init_attributes(self):
        self.position_x = 0.0
        self.position_y = 0.0
        self.width = 0.4
        self.height = 0.8
        self.level = None
        self.solid = True

    def collides(self, with_what):
        if ((self.position_x < with_what.position_x and
             self.position_x < with_what.position_x + with_what.width and
             self.position_x + self.width < with_what.position_x and
             self.position_x + self.width < with_what.position_x + with_what.width)
                or
                (self.position_x > with_what.position_x and
                 self.position_x > with_what.position_x + with_what.width and
                 self.position_x + self.width > with_what.position_x and
                 self.position_x + self.width > with_what.position_x + with_what.width)):
            return False

        if ((self.position_y < with_what.position_y and
             self.position_y < with_what.position_y + with_what.height and
             self.position_y + self.height < with_what.position_y and
             self.position_y + self.height < with_what.position_y + with_what.height)
                or
                (self.position_y > with_what.position_y and
                 self.position_y > with_what.position_y + with_what.height and
                 self.position_y + self.height > with_what.position_y and
                 self.position_y + self.height > with_what.position_y + with_what.height)):
            return False

        return True

    def is_in_air(self):
        distance_to_ground = 99999

        lower_border = self.position_y + self.height / 2.0
        tile_y = int(lower_border) + 1

        if MapGridObject.is_tile(self.level.get_at(int(self.position_x), tile_y)):
            distance_to_ground = tile_y - lower_border

        return distance_to_ground > 0.1

    def move_by(self, dx, dy):
        if not self.solid:
            self.position_x += dx
            self.position_y += dy
            return

        half_width = self.width / 2.0
        half_height = self.height / 2.0
        occupied_cells = (
            int(self.position_x - half_width), int(self.position_y - half_height), int(self.position_x + half_width),
            int(self.position_y + half_height))
        distance_x = 0
        distance_y = 0

        if dx > 0:
            minimum = 65536

            for i in range(occupied_cells[1], occupied_cells[3] + 1):
                value = 65536

                for j in range(occupied_cells[2] + 1, occupied_cells[2] + 3):
                    if MapGridObject.is_tile(self.level.get_at(j, i)):
                        value = j
                        break

                if value < minimum:
                    minimum = value

            distance_x = minimum - (self.position_x + half_width)
        elif dx < 0:
            maximum = -2048

            for i in range(occupied_cells[1], occupied_cells[3] + 1):
                value = -2048

                for j in range(occupied_cells[0] - 1, occupied_cells[0] - 3, -1):
                    if MapGridObject.is_tile(self.level.get_at(j, i)):
                        value = j
                        break

                if value > maximum:
                    maximum = value

            distance_x = (maximum + 1) - (self.position_x - half_width)

        if dy > 0:
            minimum = 65536

            for i in range(occupied_cells[0], occupied_cells[2] + 1):
                value = 65536

                for j in range(occupied_cells[3] + 1, occupied_cells[3] + 3):
                    if MapGridObject.is_tile(self.level.get_at(i, j)):
                        value = j
                        break

                if value < minimum:
                    minimum = value

            distance_y = minimum - (self.position_y + half_height)
        elif dy < 0:
            maximum = -2048

            for i in range(occupied_cells[0], occupied_cells[2] + 1):
                value = -2048

                for j in range(occupied_cells[1] - 1, occupied_cells[1] - 3, -1):
                    if MapGridObject.is_tile(self.level.get_at(i, j)):
                        value = j
                        break

                if value > maximum:
                    maximum = value

            distance_y = (maximum + 1) - (self.position_y - half_height)

        if abs(distance_x) > abs(dx):
            self.position_x += dx

        if abs(distance_y) > abs(dy):
            self.position_y += dy

    def __init__(self, level):
        self.__init_attributes()
        self.level = level
        return


class Player(Movable):
    PLAYER_STATE_STANDING = 0
    PLAYER_STATE_WALKING = 1
    PLAYER_STATE_JUMPING_UP = 2
    PLAYER_STATE_JUMPING_DOWN = 3
    QUACK_COOLDOWN = 5000
    QUACK_DURATION = 2500

    def __init_attributes(self):
        self.state = Player.PLAYER_STATE_STANDING

        self.facing_right = True

        self.flapping_wings = False
        self.last_quack_time = -999999

        self.force_computer = ForceComputer(self)

    def jump(self):
        self.force_computer.velocity_vector[1] = -3.7

    def quack(self):
        if pygame.time.get_ticks() < self.last_quack_time + Player.QUACK_COOLDOWN:
            return

        self.last_quack_time = pygame.time.get_ticks()
        self.level.sound_player.play_quack()

    def __init__(self, level):
        super(Player, self).__init__(level)
        self.__init_attributes()
        self.force_computer.acceleration_vector[0] = self.level.gravity  # set the gravity
        self.force_computer.acceleration_vector[1] = 0


class Enemy(Movable):
    ENEMY_FLYING = 0
    ENEMY_GROUND = 1

    def ai_move(self):
        self.force_computer.execute_step()

        if pygame.time.get_ticks() < self.level.player.last_quack_time + Player.QUACK_DURATION:
            self.force_computer.velocity_vector[0] = 0

            if self.enemy_type == Enemy.ENEMY_FLYING:
                self.force_computer.velocity_vector[1] = 0

            return

        if pygame.time.get_ticks() >= self.next_direction_change:
            self.next_direction_change = pygame.time.get_ticks() + random.randint(500, 2000)
            self.__recompute_direction()

    def __recompute_direction(self):
        self.force_computer.velocity_vector[0] = 1.0 - random.random() * 2.0
        self.force_computer.velocity_vector[1] = 1.0 - random.random() * 2.0

    def __init__(self, level, enemy_type=ENEMY_GROUND):
        super(Enemy, self).__init__(level)
        self.enemy_type = enemy_type

        self.force_computer = ForceComputer(self)

        if self.enemy_type == Enemy.ENEMY_GROUND:
            self.force_computer.acceleration_vector[0] = 0
            self.force_computer.acceleration_vector[1] = level.gravity

        self.force_computer.ground_friction = 0
        self.next_direction_change = 0

        self.enemy_type = enemy_type
        return


class TileTopImageContainer:
    def __init__(self):
        self.image = None
        self.left = None
        self.center = None
        self.right = None


class CharacterImageContainer:
    def __init__(self):
        self.standing = []
        self.moving_right = []
        self.moving_left = []
        self.jumping = []
        self.special = []


class SoundPlayer:
    def __init__(self, allow):
        self.allowed = allow

        if not self.allowed:
            return

        pygame.mixer.init()

        if not pygame.mixer.get_init:
            return

        self.sound_quack = pygame.mixer.Sound("backgrounds and sounds/quack.wav")
        self.sound_trampoline = pygame.mixer.Sound("backgrounds and sounds/trampoline.wav")
        self.sound_coin = pygame.mixer.Sound("backgrounds and sounds/coin.wav")
        self.sound_click = pygame.mixer.Sound("backgrounds and sounds/click.wav")
        self.sound_flap = pygame.mixer.Sound("backgrounds and sounds/flapping.wav")
        self.sound_win = pygame.mixer.Sound("backgrounds and sounds/win.wav")

        pygame.mixer.music.load("backgrounds and sounds/blue_dot_session.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def play_quack(self):
        if self.allowed:
            self.sound_quack.play()

    def play_trampoline(self):
        if self.allowed:
            self.sound_trampoline.play()

    def play_coin(self):
        if self.allowed:
            self.sound_coin.play()

    def play_click(self):
        if self.allowed:
            self.sound_click.play()

    def play_flap(self):
        if self.allowed:
            self.sound_flap.play()

    def play_win(self):
        if self.allowed:
            self.sound_win.play()


class Renderer:
    TILE_WIDTH = 200
    TILE_HEIGHT = 200
    TOP_LAYER_OFFSET = 10
    TOP_LAYER_LEFT_WIDTH = 23
    QUACK_LENGTH = 350

    def __init_attributes(self):
        self.font_normal = pygame.font.Font("backgrounds and sounds/Folktale.ttf", 28)
        self.font_small = pygame.font.Font("backgrounds and sounds/larabiefont.ttf", 20)
        self.font_color = (100, 50, 0)
        self._level = None
        self.screen_width = 640
        self.screen_height = 480
        self.screen_width_tiles = 1
        self.screen_height_tiles = 1
        self._camera_x = 0
        self._camera_y = 0
        self.tile_images = {}
        self.background_image = None
        self.scores_image = None
        arrow_mask = pygame.image.load("backgrounds and sounds/arrow_mask.bmp")
        self.arrow_image = prepare_image(pygame.image.load("backgrounds and sounds/arrow.bmp"),
                                         transparency_mask=arrow_mask)
        self.enemy_flying_images = []
        enemy_flying_mask = pygame.image.load("backgrounds and sounds/robot_flying_1_mask.bmp")
        self.enemy_flying_images.append(
            prepare_image(pygame.image.load("backgrounds and sounds/robot_flying_1.bmp")
                          , transparency_mask=enemy_flying_mask))
        enemy_flying_mask = pygame.image.load("backgrounds and sounds/robot_flying_2_mask.bmp")
        self.enemy_flying_images.append(
            prepare_image(pygame.image.load("backgrounds and sounds/robot_flying_2.bmp")
                          , transparency_mask=enemy_flying_mask))
        enemy_flying_mask = pygame.image.load("backgrounds and sounds/robot_flying_3_mask.bmp")
        self.enemy_flying_images.append(
            prepare_image(pygame.image.load("backgrounds and sounds/robot_flying_3.bmp"),
                          transparency_mask=enemy_flying_mask))
        self.enemy_ground_images = []
        enemy_ground_mask = pygame.image.load("backgrounds and sounds/robot_ground_stand_mask.bmp")
        self.enemy_ground_images.append(
            prepare_image(pygame.image.load("backgrounds and sounds/robot_ground_stand.bmp"),
                          transparency_mask=enemy_ground_mask))
        enemy_ground_mask = pygame.image.load("backgrounds and sounds/robot_ground_right_mask.bmp")
        self.enemy_ground_images.append(
            prepare_image(pygame.image.load("backgrounds and sounds/robot_ground_right.bmp"),
                          transparency_mask=enemy_ground_mask))
        enemy_ground_mask = pygame.image.load("backgrounds and sounds/robot_ground_left_mask.bmp")
        self.enemy_ground_images.append(
            prepare_image(pygame.image.load("backgrounds and sounds/robot_ground_left.bmp"),
                          transparency_mask=enemy_ground_mask))
        teleport_mask = pygame.image.load("backgrounds and sounds/teleport_mask.bmp")
        self.teleport_inactive_image = prepare_image(pygame.image.load("backgrounds and sounds/teleport_1.bmp"),
                                                     transparency_mask=teleport_mask)
        self.teleport_active_image = prepare_image(pygame.image.load("backgrounds and sounds/teleport_2.bmp"),
                                                   transparency_mask=teleport_mask)
        self.logo_image = prepare_image(pygame.image.load("backgrounds and sounds/logo.bmp"))
        self.coin_images = []

        score_bar_mask = pygame.image.load("backgrounds and sounds/score_bar_mask.bmp")
        self.score_bar_image = prepare_image(pygame.image.load("backgrounds and sounds/score_bar.bmp"),
                                             transparency_mask=score_bar_mask)

        for i in range(1, 7):
            coin_mask = pygame.image.load("backgrounds and sounds/coin_" + str(i) + "_mask.bmp")
            self.coin_images.append(
                prepare_image(pygame.image.load("backgrounds and sounds/coin_" + str(i) + ".bmp"),
                              transparency_mask=coin_mask))

        egg_mask = pygame.image.load("backgrounds and sounds/egg_mask.bmp")
        self.egg_image = prepare_image(pygame.image.load("backgrounds and sounds/egg.bmp"), transparency_mask=egg_mask)
        self.background_repeat_times = 1
        self.visible_tile_area = (0, 0, 0, 0)

        spikes_mask = pygame.image.load("backgrounds and sounds/spikes_mask.bmp")
        self.spikes_image = prepare_image(pygame.image.load("backgrounds and sounds/spikes.bmp"),
                                          transparency_mask=spikes_mask)
        self.trampoline_image = prepare_image(pygame.image.load("backgrounds and sounds/trampoline.bmp"))
        self.player_images = CharacterImageContainer()

        self.player_images.standing.append(prepare_image(pygame.image.load
                                                         ("backgrounds and sounds/duck_right_stand.bmp"),
                                                         transparency_mask=pygame.image.load(
                                                             "backgrounds and sounds/duck_right_stand_mask.bmp")))
        self.player_images.standing.append(pygame.transform.flip(self.player_images.standing[0], True, False))

        for i in range(1, 7):
            self.player_images.moving_right.append(
                prepare_image(pygame.image.load("backgrounds and sounds/duck_right_walk_" + str(i) + ".bmp"),
                              transparency_mask=pygame.image.load("backgrounds and sounds/duck_right_walk_" + str(i)
                                                                  + "_mask.bmp")))
            self.player_images.moving_left.append(
                pygame.transform.flip(self.player_images.moving_right[-1], True, False))

        self.player_images.jumping.append(prepare_image(pygame.image.load
                                                        ("backgrounds and sounds/duck_right_jump_up_1.bmp"),
                                                        transparency_mask=pygame.image.load(
                                                            "backgrounds and sounds/duck_right_jump_up_1_mask.bmp")))
        self.player_images.jumping.append(prepare_image(pygame.image.load
                                                        ("backgrounds and sounds/duck_right_jump_up_2.bmp"),
                                                        transparency_mask=pygame.image.load(
                                                            "backgrounds and sounds/duck_right_jump_up_2_mask.bmp")))
        self.player_images.jumping.append(prepare_image(pygame.image.load
                                                        ("backgrounds and sounds/duck_right_jump_down_1.bmp"),
                                                        transparency_mask=pygame.image.load(
                                                            "backgrounds and sounds/duck_right_jump_down_1_mask.bmp")))
        self.player_images.jumping.append(prepare_image(pygame.image.load
                                                        ("backgrounds and sounds/duck_right_jump_down_2.bmp"),
                                                        transparency_mask=pygame.image.load(
                                                            "backgrounds and sounds/duck_right_jump_down_2_mask.bmp")))
        self.player_images.jumping.append(pygame.transform.flip(self.player_images.jumping[0], True, False))
        self.player_images.jumping.append(pygame.transform.flip(self.player_images.jumping[1], True, False))
        self.player_images.jumping.append(pygame.transform.flip(self.player_images.jumping[2], True, False))
        self.player_images.jumping.append(pygame.transform.flip(self.player_images.jumping[3], True, False))

        self.player_images.special.append(prepare_image(pygame.image.load(
            "backgrounds and sounds/duck_right_quack.bmp"),
                                                        transparency_mask=pygame.image.load(
                                                            "backgrounds and sounds/duck_right_quack_mask.bmp")))
        self.player_images.special.append(pygame.transform.flip(self.player_images.special[0], True, False))

    def __milliseconds_to_time(self, value):
        seconds = int(value / 1000)
        tenths = int((value % 1000) / 100)

        return str(seconds) + ":" + str(tenths)

    def set_level(self, level):
        self._level = level
        self.background_image = prepare_image(
            pygame.image.load("backgrounds and sounds/background_" + self._level.background_name + ".bmp"))

        self.background_repeat_times = int(math.ceil(self.screen_width / float(self.background_image.get_width())))
        for tile in level.tiles:
            self.tile_images[tile[0]] = []
            top_mask = pygame.image.load(("backgrounds and sounds/tile_" + tile[1] + "_top_mask.bmp"))
            top_image = prepare_image(pygame.image.load(("backgrounds and sounds/tile_" + tile[1] + "_top.bmp")),
                                      transparency_mask=top_mask)

            self.tile_images[tile[0]].append(TileTopImageContainer())

            self.tile_images[tile[0]][0].image = top_image
            self.tile_images[tile[0]][0].left = top_image.subsurface(pygame.Rect(0, 0, 23, 56))
            self.tile_images[tile[0]][0].center = top_image.subsurface(pygame.Rect(24, 0, 201, 56))
            self.tile_images[tile[0]][0].right = top_image.subsurface(pygame.Rect(225, 0, 21, 56))
            for variant_number in range(tile[2]):
                self.tile_images[tile[0]].append(prepare_image(
                    pygame.image.load("backgrounds and sounds/tile_" + tile[1] + "_" + str(variant_number + 1) +
                                      ".bmp")))

        self.scores_image = prepare_image(pygame.Surface((250, 200)), pygame.Color(0, 0, 0))
        text_image = self.font_normal.render("top scores:", 1, self.font_color)
        self.scores_image.blit(text_image, (0, 0))

        for i in range(min(3, len(self._level.scores))):
            text_image = self.font_small.render(
                text_to_fixed_width(self._level.scores[i][0], 10) + " " + text_to_fixed_width(
                    str(self._level.scores[i][1]), 6) + " " + text_to_fixed_width(
                    self.__milliseconds_to_time(self._level.scores[i][2]), 6), 1, self.font_color)
            self.scores_image.blit(text_image, (0, 30 + (i + 1) * 20))

    def __get_top_layer(self, x, y):
        center = not MapGridObject.is_tile(self._level.get_at(x, y - 1))
        left = not MapGridObject.is_tile(self._level.get_at(x, y - 1)) and not MapGridObject.is_tile(
            self._level.get_at(x - 1, y)) and not MapGridObject.is_tile(self._level.get_at(x - 1, y - 1))
        right = not MapGridObject.is_tile(self._level.get_at(x, y - 1)) and not MapGridObject.is_tile(
            self._level.get_at(x + 1, y)) and not MapGridObject.is_tile(self._level.get_at(x + 1, y - 1))

        return (left, center, right)

    def __map_position_to_screen_position(self, x, y):
        return (x * Renderer.TILE_WIDTH - self._camera_x, y * Renderer.TILE_HEIGHT - self._camera_y)

    def render_menu(self, menu):
        result = pygame.Surface((self.screen_width, self.screen_height))
        result.fill((255, 255, 255))

        result.blit(self.logo_image, (self.screen_width / 2 - self.logo_image.get_width() / 2,
                                      self.screen_height / 2 - self.logo_image.get_height() / 2))

        i = 0

        while i < len(menu.items):
            text_image = self.font_normal.render(menu.items[i], 1, (0, 0, 0))
            result.blit(text_image, (100, 100 + i * 40))

            if i == menu.selected_item:
                result.blit(self.arrow_image, (50, 95 + i * 40))

            i += 1

        i = 0

        while i < len(menu.text_lines):
            text_image = self.font_small.render(menu.text_lines[i], 1, (0, 0, 0))
            result.blit(text_image, (100, self.screen_height / 2 + i * 30))
            i += 1

        return result

    def render_level(self):
        result = pygame.Surface((self.screen_width, self.screen_height))
        result.fill(self._level.background_color)

        animation_frame = int(pygame.time.get_ticks() / 64)
        for i in range(self.background_repeat_times):
            result.blit(self.background_image, (i * self.background_image.get_width(), 0))
        for j in range(self.visible_tile_area[1], self.visible_tile_area[3]):
            for i in range(self.visible_tile_area[0], self.visible_tile_area[2]):
                map_grid_object = self._level.get_at(i, j)

                if map_grid_object == None:
                    continue
                else:
                    x = i * Renderer.TILE_WIDTH - self._camera_x
                    y = j * Renderer.TILE_HEIGHT - self._camera_y

                    if map_grid_object.object_type == MapGridObject.OBJECT_TILE:
                        result.blit(self.tile_images[map_grid_object.tile_id][map_grid_object.tile_variant], (x, y))

                        top_layer = self.__get_top_layer(i, j)

                        if top_layer[0]:  # left
                            result.blit(self.tile_images[map_grid_object.tile_id][0].left,
                                        (x - Renderer.TOP_LAYER_LEFT_WIDTH, y - Renderer.TOP_LAYER_OFFSET))

                        if top_layer[1]:  # center
                            result.blit(self.tile_images[map_grid_object.tile_id][0].center,
                                        (x, y - Renderer.TOP_LAYER_OFFSET))

                        if top_layer[2]:  # right
                            result.blit(self.tile_images[map_grid_object.tile_id][0].right,
                                        (x + Renderer.TILE_WIDTH, y - Renderer.TOP_LAYER_OFFSET))

                    elif map_grid_object.object_type == MapGridObject.OBJECT_SPIKES:
                        result.blit(self.spikes_image, (x, y))
                    elif map_grid_object.object_type == MapGridObject.OBJECT_EGG:
                        result.blit(self.egg_image, (x + 50, y + 50))
                    elif map_grid_object.object_type == MapGridObject.OBJECT_COIN:
                        result.blit(self.coin_images[animation_frame % len(self.coin_images)], (x + 20, y))
                    elif map_grid_object.object_type == MapGridObject.OBJECT_TRAMPOLINE:
                        result.blit(self.trampoline_image, (x, y))
                    elif map_grid_object.object_type == MapGridObject.OBJECT_FINISH:
                        if self._level.eggs_left > 0:
                            result.blit(self.teleport_inactive_image, (x, y))
                        else:
                            result.blit(self.teleport_active_image, (x, y))
        player_position = self.__map_position_to_screen_position(self._level.player.position_x,
                                                                 self._level.player.position_y)

        player_image = self.player_images.standing[0]

        if self._level.player.flapping_wings:
            flapping_animation_frame = animation_frame % 2
        else:
            flapping_animation_frame = 0

        if pygame.time.get_ticks() < self._level.player.last_quack_time + Renderer.QUACK_LENGTH:
            if self._level.player.facing_right:
                player_image = self.player_images.special[0]
            else:
                player_image = self.player_images.special[1]
        elif self._level.player.state == Player.PLAYER_STATE_STANDING:
            if self._level.player.facing_right:
                player_image = self.player_images.standing[0]
            else:
                player_image = self.player_images.standing[1]
        elif self._level.player.state == Player.PLAYER_STATE_WALKING:
            if self._level.player.facing_right:
                player_image = self.player_images.moving_right[animation_frame % len(self.player_images.moving_right)]
            else:
                player_image = self.player_images.moving_left[animation_frame % len(self.player_images.moving_right)]
        elif self._level.player.state == Player.PLAYER_STATE_JUMPING_UP:
            if self._level.player.facing_right:
                player_image = self.player_images.jumping[flapping_animation_frame]
            else:
                player_image = self.player_images.jumping[4 + flapping_animation_frame]
        elif self._level.player.state == Player.PLAYER_STATE_JUMPING_DOWN:
            if self._level.player.facing_right:
                player_image = self.player_images.jumping[3 - flapping_animation_frame]
            else:
                player_image = self.player_images.jumping[7 - flapping_animation_frame]

        result.blit(player_image, (
            player_position[0] - player_image.get_width() / 2, player_position[1] - player_image.get_height() / 2))
        for enemy in self._level.enemies:
            enemy_position = self.__map_position_to_screen_position(enemy.position_x, enemy.position_y)

            if enemy.enemy_type == Enemy.ENEMY_GROUND:
                if enemy.force_computer.velocity_vector[0] > 0.5:
                    enemy_image = self.enemy_ground_images[1]
                elif enemy.force_computer.velocity_vector[0] < -0.5:
                    enemy_image = self.enemy_ground_images[2]
                else:
                    enemy_image = self.enemy_ground_images[0]
            else:
                enemy_image = self.enemy_flying_images[animation_frame % 3]

            result.blit(enemy_image, (
                enemy_position[0] - enemy_image.get_width() / 2, enemy_position[1] - enemy_image.get_height() / 2))

        line_height = 30
        text_image = self.font_normal.render("time: " + self.__milliseconds_to_time(self._level.time), 1,
                                             self.font_color)
        result.blit(text_image, (50, 50))
        text_image = self.font_normal.render("score: " + str(self._level.score), 1, self.font_color)
        result.blit(text_image, (50, 50 + line_height))
        result.blit(self.scores_image, (self.screen_width - 300, 50))

        if self._level.state == Level.STATE_LOST:
            text_image = self.font_normal.render("you lost", 1, (255, 0, 0))
            result.blit(text_image, (
                self.screen_width / 2 - text_image.get_width() / 2,
                self.screen_height / 2 - text_image.get_height() / 2))
        elif self._level.state == Level.STATE_WON:
            text_image = self.font_normal.render("you won", 1, (0, 255, 0))
            result.blit(text_image, (
                self.screen_width / 2 - text_image.get_width() / 2,
                self.screen_height / 2 - text_image.get_height() / 2))

        return result

    def set_camera_position(self, camera_x, camera_y):
        self._camera_x = camera_x - self.screen_width / 2
        self._camera_y = camera_y - self.screen_width / 2

        helper_x = int(self._camera_x / Renderer.TILE_WIDTH)
        helper_y = int(self._camera_y / Renderer.TILE_HEIGHT)

        self.visible_tile_area = (
            helper_x, helper_y, helper_x + self.screen_width_tiles, helper_y + self.screen_height_tiles)

    def __init__(self, screen_width, screen_height):
        self.__init_attributes()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_width_tiles = int(math.ceil(self.screen_width / Renderer.TILE_WIDTH)) + 2
        self.screen_height_tiles = int(math.ceil(self.screen_height / Renderer.TILE_HEIGHT)) + 2
        return


class ForceComputer:
    def __init_attributes(self):
        self.decorated_object = None
        self.velocity_vector = [0, 0]
        self.acceleration_vector = [0, 0]
        self.maximum_horizontal_speed = 3
        self.ground_friction = 5

    def execute_step(self):
        if frame_time == 0:
            return

        seconds = frame_time / 1000.0

        object_position = (self.decorated_object.position_x, self.decorated_object.position_y)
        self.decorated_object.move_by(self.velocity_vector[0] * seconds, self.velocity_vector[1] * seconds)
        object_position2 = (self.decorated_object.position_x, self.decorated_object.position_y)

        self.velocity_vector = [(object_position2[0] - object_position[0]) / seconds,
                                (object_position2[1] - object_position[1]) / seconds]

        self.velocity_vector[0] += (self.acceleration_vector[0] - self.velocity_vector[
            0] * self.ground_friction) * seconds
        self.velocity_vector[1] += self.acceleration_vector[1] * seconds

    def __init__(self, decorated_object):
        self.__init_attributes()
        self.decorated_object = decorated_object


class Menu:
    def __init__(self):
        self.items = []
        self.selected_item = 0
        self.text_lines = []

    def cursor_up(self):
        self.selected_item = max(self.selected_item - 1, 0)

    def cursor_down(self):
        self.selected_item = min(self.selected_item + 1, len(self.items) - 1)


class Config:
    def __init__(self, filename):
        self.sound = True
        self.fullscreen = False
        self.name = "player"

        try:
            lines = [line.strip() for line in open(filename)]

            for line in lines:
                line_split = line.split(":")
                line_split[0] = line_split[0].lstrip().rstrip()
                line_split[1] = line_split[1].lstrip().rstrip()

                if line_split[0] == "sound":
                    self.sound = line_split[1] == "yes"
                elif line_split[0] == "fullscreen":
                    self.fullscreen = line_split[1] == "yes"
                elif line_split[0] == "name":
                    self.sound = line_split[1]

        except Exception:
            output_file = open(filename, 'w')
            output_file.write("name: player\nfullscreen: no\nsound: yes\n")
            output_file.close()


class Game:
    STATE_MENU_MAIN = 0
    STATE_MENU_ABOUT = 1
    STATE_MENU_PLAY = 2
    STATE_IN_GAME = 3
    VERSION = "1.1"

    FLYING_FORCE = 2
    UPDATE_STATE_AFTER_FRAMES = 7

    def __init__(self, name, fullscreen, sound):
        self.name = name
        self.fullscreen = fullscreen
        self.sound = sound
        self.state = Game.STATE_MENU_MAIN
        screen_width = 1024
        screen_height = 640

        if sound:
            pygame.mixer.pre_init(22050, -16, 2,
                                  512)

        pygame.init()

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)

        if self.fullscreen:
            fullscreen_size = (pygame.display.list_modes())[0]

            if fullscreen_size != -1:
                screen_width = fullscreen_size[0]
                screen_height = fullscreen_size[1]

            self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((screen_width, screen_height))

        pygame.display.set_caption("Flying Duck")
        pygame.mouse.set_visible(True)
        self.sound_player = SoundPlayer(sound)
        self.level = None
        self.renderer = Renderer(screen_width, screen_height)
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
        self.key_space = False
        self.key_ctrl = False
        self.key_return = False
        self.key_escape = False
        self.player_state_update_counter = 0
        self.menu_main = Menu()
        self.menu_main.items.append("new game")
        self.menu_main.items.append("about")
        self.menu_main.items.append("exit")

        self.menu_about = Menu()
        self.menu_about.items.append("back")
        self.menu_about.text_lines.append("Caleb Ram, Made in 2021")
        self.menu_about.text_lines.append("version " + Game.VERSION)
        self.menu_about.text_lines.append("powered by Python + Arcade")
        self.menu_about.text_lines.append("your name is set to: " + self.name)

        self.menu_about.text_lines.append("")
        self.menu_about.text_lines.append("arrows = move")
        self.menu_about.text_lines.append("ctrl = quack")
        self.menu_about.text_lines.append("space = flap wings")
        self.menu_about.text_lines.append("aim of game = collect all eggs and fly to the teleport")

        self.menu_play = Menu()
        self.menu_play.items.append("level 1")
        self.menu_play.items.append("level 2")
        self.menu_play.items.append("level 3")
        self.menu_play.items.append("level 4")
        self.menu_play.items.append("level 5")
        self.menu_play.items.append("level 6")
        self.menu_play.items.append("level 7")
        self.menu_play.items.append("level 8")
        self.menu_play.items.append("back")

    def run(self):
        global frame_time, flapping_played
        rendered_frame = None
        done = False
        wait = False
        flapping_player = False
        wait_until = 0
        cheat = False
        cheat_buffer = [0, 0]

        while not done:
            time_start = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.key_right = True
                    elif event.key == pygame.K_UP:
                        self.key_up = True
                    elif event.key == pygame.K_LEFT:
                        self.key_left = True
                    elif event.key == pygame.K_DOWN:
                        self.key_down = True
                    elif event.key == pygame.K_SPACE:
                        self.key_space = True
                    elif event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL:
                        self.key_ctrl = True
                    elif event.key == pygame.K_RETURN:
                        self.key_return = True
                    elif event.key == pygame.K_ESCAPE:
                        self.key_escape = True
                    elif event.key == pygame.K_KP4:
                        cheat_buffer[0] = cheat_buffer[1]
                        cheat_buffer[1] = 4
                    elif event.key == pygame.K_KP2:
                        cheat_buffer[0] = cheat_buffer[1]
                        cheat_buffer[1] = 2
                        if cheat_buffer[0] == 4 and cheat_buffer[1] == 2:
                            self.sound_player.play_win()
                            cheat = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.key_right = False
                    elif event.key == pygame.K_LEFT:
                        self.key_left = False
                    elif event.key == pygame.K_UP:
                        self.key_up = False
                    elif event.key == pygame.K_DOWN:
                        self.key_down = False
                    elif event.key == pygame.K_SPACE:
                        self.key_space = False
                    elif event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL:
                        self.key_ctrl = False
                    elif event.key == pygame.K_RETURN:
                        self.key_return = False
                    elif event.key == pygame.K_ESCAPE:
                        self.key_escape = False

            if self.state == Game.STATE_IN_GAME:
                if self.key_escape:
                    self.state = Game.STATE_MENU_MAIN

                if self.level.state == Level.STATE_PLAYING:
                    if self.key_up:
                        if not self.level.player.state in [Player.PLAYER_STATE_JUMPING_UP,
                                                           Player.PLAYER_STATE_JUMPING_DOWN] \
                                and not self.level.player.is_in_air():
                            self.level.player.jump()

                    if self.key_right and not self.key_left:
                        self.level.player.force_computer.acceleration_vector[0] = 40 if cheat else 20.0
                    elif self.key_left and not self.key_right:
                        self.level.player.force_computer.acceleration_vector[0] = -40 if cheat else -20.0
                    else:
                        self.level.player.force_computer.acceleration_vector[0] = 0

                    if self.key_ctrl:
                        self.level.player.quack()

                    if self.key_space:
                        if not flapping_played:
                            self.level.sound_player.play_flap()
                            flapping_played = True

                        self.level.player.flapping_wings = True
                    else:
                        flapping_played = False
                        self.level.player.flapping_wings = False

                    if self.level.player.flapping_wings:
                        self.level.player.force_computer.acceleration_vector[1] = self.level.gravity - Game.FLYING_FORCE
                    else:
                        self.level.player.force_computer.acceleration_vector[1] = self.level.gravity

                    self.level.update()
                else:
                    if not wait:
                        wait_until = pygame.time.get_ticks() + 3000
                        wait = True
                    elif pygame.time.get_ticks() >= wait_until:
                        wait = False
                        self.state = Game.STATE_MENU_MAIN

                for enemy in self.level.enemies:
                    enemy.ai_move()

                self.level.player.force_computer.execute_step()

                if self.level.state != Level.STATE_LOST:
                    self.renderer.set_camera_position(int(self.level.player.position_x * Renderer.TILE_WIDTH),
                                                      int(self.level.player.position_y * Renderer.TILE_HEIGHT) + 200)

                self.player_state_update_counter = (
                                                           self.player_state_update_counter + 1) % \
                                                   Game.UPDATE_STATE_AFTER_FRAMES

                if self.player_state_update_counter == 0:
                    if self.level.player.force_computer.velocity_vector[1] > 0.1:
                        self.level.player.state = Player.PLAYER_STATE_JUMPING_DOWN
                    elif self.level.player.force_computer.velocity_vector[1] < -0.1:
                        self.level.player.state = Player.PLAYER_STATE_JUMPING_UP
                    else:
                        if self.level.player.force_computer.velocity_vector[0] > 0.1 or \
                                self.level.player.force_computer.velocity_vector[0] < -0.1:
                            self.level.player.state = Player.PLAYER_STATE_WALKING
                        else:
                            self.level.player.state = Player.PLAYER_STATE_STANDING

                    if self.level.player.force_computer.acceleration_vector[0] > 0.1:
                        self.level.player.facing_right = True
                    elif self.level.player.force_computer.acceleration_vector[0] < -0.1:
                        self.level.player.facing_right = False

                self.screen.blit(self.renderer.render_level(), (0, 0))
                pygame.display.flip()
            elif self.state == Game.STATE_MENU_MAIN:
                if self.key_up:
                    self.menu_main.cursor_up()
                    self.key_up = False

                if self.key_down:
                    self.menu_main.cursor_down()
                    self.key_down = False

                if self.key_return:
                    if self.menu_main.selected_item == 0:
                        self.state = Game.STATE_MENU_PLAY
                    elif self.menu_main.selected_item == 1:
                        self.state = Game.STATE_MENU_ABOUT
                    elif self.menu_main.selected_item == 2:
                        done = True

                    self.key_return = False

                self.screen.blit(self.renderer.render_menu(self.menu_main), (0, 0))
                pygame.display.flip()
            elif self.state == Game.STATE_MENU_ABOUT:
                if self.key_return:
                    self.state = Game.STATE_MENU_MAIN
                    self.key_return = False

                self.screen.blit(self.renderer.render_menu(self.menu_about), (0, 0))
                pygame.display.flip()
            elif self.state == Game.STATE_MENU_PLAY:
                if self.key_up:
                    self.menu_play.cursor_up()
                    self.key_up = False

                if self.key_down:
                    self.menu_play.cursor_down()
                    self.key_down = False

                if self.key_return:
                    if self.menu_play.selected_item == 8:
                        self.state = Game.STATE_MENU_MAIN
                    else:
                        level_name = "level" + str(self.menu_play.selected_item + 1) + ".lvl"
                        self.level = Level(self)
                        self.level.load_from_file("backgrounds and sounds/" + level_name)
                        self.renderer.set_level(self.level)
                        self.state = Game.STATE_IN_GAME

                    self.key_return = False

                self.screen.blit(self.renderer.render_menu(self.menu_play), (0, 0))
                pygame.display.flip()

            frame_time = pygame.time.get_ticks() - time_start


config = Config("config.txt")
game = Game(config.name, config.fullscreen, config.sound)
game.run()
