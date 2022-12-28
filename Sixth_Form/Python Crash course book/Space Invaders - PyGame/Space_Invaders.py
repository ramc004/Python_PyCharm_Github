import pygame
from pygame.locals import *
import sys
from random import shuffle

# Imports various libraries: pygame, sys for sleep and the random function 'shuffle'


# Colours for background and characters
Gray = (100, 100, 100)
NavyBlue = (60, 60, 100)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
NearBlack = (19, 15, 48)
ComBlue = (233, 232, 255)

# Creating Player attributes
PlayerWidth = 40
PlayerHeight = 10
PlayerColor = ComBlue
Player1 = 'Player 1'
PlayerSpeed = 5
PlayerColor = Green

# Creating GUI window attributes
GameTitle = 'Space Invaders'
DisplayWidth = 640
DisplayHeight = 480
bgColor = NearBlack
xMargin = 50
yMargin = 50

# Creating Bullet attributes
BulletWidth = 5
BulletHeight = 5
BulletOffSet = 700

# Creating invader attributes
enemyWidth = 25
enemyHeight = 25
enemyName = 'Enemy'
enemyGap = 20
arrayWidth = 10
arrayHeight = 4
MoveTime = 1000
movex = 10
movey = enemyHeight
timeOffset = 300

DIRECT_DICT = {pygame.K_LEFT: (-1),
               pygame.K_RIGHT: (1)}


# Creates player class


class Player(pygame.sprite.Sprite):
    # attributes
    def __init__(self):
        """ this first function uses one of the sprites from pygame to make the characters attributes
        makes the width for the player
        makes the height for the player
        creates the dimensions for the surface of the image
        allows the player to have different colours for the amount of lives
        gives player a specific speed """
        pygame.sprite.Sprite.__init__(self)
        self.width = PlayerWidth
        self.height = PlayerHeight
        self.image = pygame.Surface((self.width, self.height))
        self.color = PlayerColor
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.name = Player1
        self.speed = PlayerSpeed
        self.vectorx = 0

    # Creates update function
    def update(self, keys, *args):
        for key in DIRECT_DICT:
            if keys[key]:
                """ this function searches for the key into the speed to see if enough time has passed in order to 
                 increase the speed """
                self.rect.x += DIRECT_DICT[key] * self.speed

        self.checkForSide()
        self.image.fill(self.color)

    def checkForSide(self):
        """ this function allows the player to move their character from side to side starting them at the point 0
        using vectors """
        if self.rect.right > DisplayWidth:
            self.rect.right = DisplayWidth
            self.vectorx = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.vectorx = 0


# Creates class for shields/blockers
class Blocker(pygame.sprite.Sprite):

    def __init__(self, side, color, row, column):
        """ this function creates all the attributes for the blockers to protect the player and make it harder for the
        user to always shoot the aliens
        creates the width, height and colour for the blocker
        gives the blocker a name
        gives the blocker its parameters"""
        pygame.sprite.Sprite.__init__(self)
        self.width = side
        self.height = side
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.name = 'blocker'
        self.row = row
        self.column = column


# Creates class for Bullets
class Bullet(pygame.sprite.Sprite):

    def __init__(self, rect, color, vectory, speed):
        """ creates the width height and colour for the bullet that the user shoots at the aliens
         gives the bullet a speed and a position form the y axis using vectors """
        pygame.sprite.Sprite.__init__(self)
        self.width = BulletWidth
        self.height = BulletHeight
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = rect.centerx
        self.rect.top = rect.bottom
        self.name = 'bullet'
        self.vectory = vectory
        self.speed = speed

    # Update window
    def update(self, *args):
        """ collects the old location of the bullet and moves it to the new one across the x axis """
        self.oldLocation = (self.rect.x, self.rect.y)
        self.rect.y += self.vectory * self.speed

        if self.rect.bottom < 0:
            self.kill()

        elif self.rect.bottom > 500:
            self.kill()


# Creates enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, row, column):
        """ this function creates the width, height and colour for the enemy
        places where the aliens are going
        gives them an initial point on the window of 1
        makes when the aliens need to move down faster
        it does this by using teh amount of time passed in the game and performs a calculation on where to move the
        aliens and at what speed """
        pygame.sprite.Sprite.__init__(self)
        self.width = enemyWidth
        self.height = enemyHeight
        self.row = row
        self.column = column
        self.image = self.setImage()
        self.rect = self.image.get_rect()
        self.name = 'enemy'
        self.vectorx = 1
        self.moveNumber = 0
        self.MoveTime = MoveTime
        self.timeOffset = row * timeOffset
        self.timer = pygame.time.get_ticks() - self.timeOffset

    # Update window
    def update(self, keys, currentTime):
        """" updates where the aliens should be
        tells the aliens to start moving if the difference between the time which the game has been running for and the
        current time and if it's greater than the move time of the aliens then they will begin to move lower down the
        screen
        has different timers to allow teh aliens to speed each time they move down """
        if currentTime - self.timer > self.MoveTime:
            if self.moveNumber < 6:
                self.rect.x += movex * self.vectorx
                self.moveNumber += 1
            elif self.moveNumber >= 6:
                self.vectorx *= -1
                self.moveNumber = 0
                self.rect.y += movey
                if self.MoveTime > 100:
                    self.MoveTime -= 50
            self.timer = currentTime

    # setting the image
    def setImage(self):
        """ uses images that I have saved in the same directory for each row of aliens
        converts the image into a vector so it can be moved about """
        if self.row == 0:
            image = pygame.image.load('scary_alien.png')
        elif self.row == 1:
            image = pygame.image.load('scarier_alien.png')
        elif self.row == 2:
            image = pygame.image.load('scariest_alien.png')
        else:
            image = pygame.image.load('scary_alien.png')
        image.convert_alpha()
        image = pygame.transform.scale(image, (self.width, self.height))

        return image


# Creating text class
class Text(object):
    def __init__(self, font, size, message, color, rect, surface):
        """ the front screen message that the player will see when they run the game
        gives it a colour, font, size of text
        also if any key is pressed the message will be replaced with the game """
        self.font = pygame.font.Font(font, size)
        self.message = message
        self.surface = self.font.render(self.message, True, color)
        self.rect = self.surface.get_rect()
        self.setRect(rect)

    def setRect(self, rect):
        """ sets the message about the axis
        the message is placed in the centre of the x and y axis when they are equal and the y axis is five more """
        self.rect.centerx, self.rect.centery = rect.centerx, rect.centery - 5

    def draw(self, surface):
        """ this function sketches where the text will be placed """
        surface.blit(self.surface, self.rect)


# Creating actual app class
class App(object):

    def __init__(self):
        """ creates the gameplay
        what to display to the user as they first open the game and when the game ends
        gives sounds for when the game starts and when the laser is shot at the alien
        sound for intro sound is set to true so when the game is first opened it begins playing """
        pygame.init()
        self.displaySurf, self.displayRect = self.makeScreen()
        self.gameStart = True
        self.gameOver = False
        self.beginGame = False
        self.laserSound = pygame.mixer.Sound('laser.ogg')
        self.startLaser = pygame.mixer.Sound('alienLaser.ogg')
        self.playIntroSound = True

    # Game over, welcome, cont. screens
    def resetGame(self):
        """ when a player either runs out of lives or has not shot all the aliens in time the game will carry on
        the game will reset its timer and its aliens orientation
        the opening message is converted to text so it can be displayed to the user
        each part of the message is given a different part of the window
        if the user looses again there will be a "Game Over" message that pops up in the middle of the screen
        also declares the bullets, the blockers and the timer inside of the actual app class
        """
        self.gameStart = True
        self.needToMakeEnemies = True

        self.introMessage1 = Text('orena.ttf', 25,
                                  'Welcome to Space Invaders!',
                                  Green, self.displayRect,
                                  self.displaySurf)
        self.introMessage2 = Text('orena.ttf', 20,
                                  'Press Any Key to Continue',
                                  Green, self.displayRect,
                                  self.displaySurf)
        self.introMessage2.rect.top = self.introMessage1.rect.bottom + 5

        self.gameOverMessage = Text('orena.ttf', 25,
                                    'GAME OVER', Green,
                                    self.displayRect, self.displaySurf)

        self.player = self.makePlayer()
        self.bullets = pygame.sprite.Group()
        self.GreenBullets = pygame.sprite.Group()
        self.blockerGroup1 = self.makeBlockers(0)
        self.blockerGroup2 = self.makeBlockers(1)
        self.blockerGroup3 = self.makeBlockers(2)
        self.blockerGroup4 = self.makeBlockers(3)
        self.allBlockers = pygame.sprite.Group(self.blockerGroup1, self.blockerGroup2,
                                               self.blockerGroup3, self.blockerGroup4)
        self.allSprites = pygame.sprite.Group(self.player, self.allBlockers)
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.enemyMoves = 0
        self.enemyBulletTimer = pygame.time.get_ticks()
        self.gameOver = False
        self.gameOverTime = pygame.time.get_ticks()
        if self.playIntroSound:
            self.startLaser.play()
            self.playIntroSound = False

    # Creating blockers
    def makeBlockers(self, number=1):
        """ creates a for loop for the blockers to be recreated each time the game restarts
        places the blockers on the tkinter window
        sets a variable for a part of the block to disappear each time either an alien or the player shoots it """
        blockerGroup = pygame.sprite.Group()

        for row in range(5):
            for column in range(7):
                blocker = Blocker(10, Green, row, column)
                blocker.rect.x = 50 + (150 * number) + (column * blocker.width)
                blocker.rect.y = 375 + (row * blocker.height)
                blockerGroup.add(blocker)

        for blocker in blockerGroup:
            if (blocker.column == 0 and blocker.row == 0
                    or blocker.column == 6 and blocker.row == 0):
                blocker.kill()

        return blockerGroup

    # Checks for incoming enemies
    def checkForEnemyBullets(self):
        """ creates a for loop for iff a red bullet hits player they loose a life
        when player is hit when they are green they change to yellow
        from yellow to red
        then if hit again the game is over """
        RedBulletsGroup = pygame.sprite.Group()

        for bullet in self.bullets:
            if bullet.color == Red:
                RedBulletsGroup.add(bullet)

        for bullet in RedBulletsGroup:
            if pygame.sprite.collide_rect(bullet, self.player):
                if self.player.color == Green:
                    self.player.color = Yellow
                elif self.player.color == Yellow:
                    self.player.color = Red
                elif self.player.color == Red:
                    self.gameOver = True
                    self.gameOverTime = pygame.time.get_ticks()
                bullet.kill()

    # Aliens shoot lasers
    def shootEnemyBullet(self, rect):
        """ aliens take turns randomly to shoot the lasers
        after a certain amount of time the aliens will speed up and move down in effort to kill off the player """
        if (pygame.time.get_ticks() - self.enemyBulletTimer) > BulletOffSet:
            self.bullets.add(Bullet(rect, Red, 1, 5))
            self.allSprites.add(self.bullets)
            self.enemyBulletTimer = pygame.time.get_ticks()

    def findEnemyShooter(self):
        """ for the program to choose an enemy shooter each column of enemies needs to be shuffled each time so that
        its purely random """
        columnList = []
        for enemy in self.enemies:
            columnList.append(enemy.column)

        columnSet = set(columnList)
        columnList = list(columnSet)
        shuffle(columnList)
        column = columnList[0]
        enemyList = []
        rowList = []

        for enemy in self.enemies:
            if enemy.column == column:
                rowList.append(enemy.row)

        row = max(rowList)

        for enemy in self.enemies:
            if enemy.column == column and enemy.row == row:
                self.shooter = enemy

    # Placing screen
    def makeScreen(self):
        """ makes the screen width and height
        fills the screen with the colour declared above (blue)
        """
        pygame.display.set_caption(GameTitle)
        displaySurf = pygame.display.set_mode((DisplayWidth, DisplayHeight))
        displayRect = displaySurf.get_rect()
        displaySurf.fill(bgColor)
        displaySurf.convert()

        return displaySurf, displayRect

    # Positioning of player
    def makePlayer(self):
        """ creates where the player will be positioned in relation to the x and y axis """
        player = Player()
        player.rect.centerx = self.displayRect.centerx
        player.rect.bottom = self.displayRect.bottom - 5

        return player

    # Positioning and creating enemies
    def makeEnemies(self):
        """ where to place the enemies
        after about 30 seconds aliens move down the y axis and move across the x axis faster every few seconds """
        enemies = pygame.sprite.Group()

        for row in range(arrayHeight):
            for column in range(arrayWidth):
                enemy = Enemy(row, column)
                enemy.rect.x = xMargin + (column * (enemyWidth + enemyGap))
                enemy.rect.y = yMargin + (row * (enemyHeight + enemyGap))
                enemies.add(enemy)

        return enemies

    def checkInput(self):
        """ creating what each key does
        space bar shoots lasers from player
        when any key is pressed the game begins
        arrow keys move players across teh x axis
        if escape key is pressed the window will close down """
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == QUIT:
                self.terminate()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE and len(self.GreenBullets) < 1:
                    bullet = Bullet(self.player.rect, Green, -1, 20)
                    self.GreenBullets.add(bullet)
                    self.bullets.add(self.GreenBullets)
                    self.allSprites.add(self.bullets)
                    self.laserSound.play()
                elif event.key == K_ESCAPE:
                    self.terminate()

    # Attributes for the start of the game
    def gameStartInput(self):
        """ when idle is quit the window is closed
        when the player runs game it sets game over to false along with game start but begin game to be true """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYUP:
                self.gameOver = False
                self.gameStart = False
                self.beginGame = True

    # Attributes for the end of the game
    def gameOverInput(self):
        """ when any key is pressed while first window is displayed the gameStart will be set to true
        beginGame is set to false
        gameOver is also set to false """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYUP:
                self.gameStart = True
                self.beginGame = False
                self.gameOver = False

    # When alien or player hits either one clause
    def checkCollisions(self):
        """ checks if any enemies have been hit by players laser
        any blockers have been hit by enemy or player
        checks if player hits alien """
        self.checkForEnemyBullets()
        pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        pygame.sprite.groupcollide(self.enemies, self.allBlockers, False, True)
        self.collide_Green_blockers()
        self.collide_Red_blockers()

    # When either alien or player shoot blockers
    def collide_Green_blockers(self):
        """ when the blockers are hit by either player or alien
        one of the parts of the block is removed using casting """
        for bullet in self.GreenBullets:
            casting = Bullet(self.player.rect, Green, -1, 20)
            casting.rect = bullet.rect.copy()
            for pixel in range(bullet.speed):
                hit = pygame.sprite.spritecollideany(casting, self.allBlockers)
                if hit:
                    hit.kill()
                    bullet.kill()
                    break
                casting.rect.y -= 1

    def collide_Red_blockers(self):
        """ when the player collides with the alien's laser the player will loose a life """
        Reds = (shot for shot in self.bullets if shot.color == Red)
        Red_bullets = pygame.sprite.Group(Reds)
        pygame.sprite.groupcollide(Red_bullets, self.allBlockers, True, True)

    # Game over
    def checkGameOver(self):
        """ sets game over to being true meaning game over screen is displayed
        gameStart is set for false meaning is doesn't come up
        when gameOver is displayed timer stops counting """
        if len(self.enemies) == 0:
            self.gameOver = True
            self.gameStart = False
            self.beginGame = False
            self.gameOverTime = pygame.time.get_ticks()

        else:
            for enemy in self.enemies:
                if enemy.rect.bottom > DisplayHeight:
                    self.gameOver = True
                    self.gameStart = False
                    self.beginGame = False
                    self.gameOverTime = pygame.time.get_ticks()

    # Cross and minus
    def terminate(self):
        """ sets what happens when the window is closed """
        pygame.quit()
        sys.exit()

    # Main code for the actual game to run (all logic)
    def mainLoop(self):
        """ when game is run
        gameOver is set to = false because the player hasn't ran out of lives yet
        the intro sound is set to play when game is opened
        when the game begins the enemies have been created and are ready to move
        checks for collisions between the player, the alien and the blockers """
        while True:
            if self.gameStart:
                self.resetGame()
                self.gameOver = False
                self.displaySurf.fill(bgColor)
                self.introMessage1.draw(self.displaySurf)
                self.introMessage2.draw(self.displaySurf)
                self.gameStartInput()
                pygame.display.update()

            elif self.gameOver:
                self.playIntroSound = True
                self.displaySurf.fill(bgColor)
                self.gameOverMessage.draw(self.displaySurf)

                if (pygame.time.get_ticks() - self.gameOverTime) > 2000:
                    self.gameOverInput()
                pygame.display.update()

            elif self.beginGame:
                if self.needToMakeEnemies:
                    self.enemies = self.makeEnemies()
                    self.allSprites.add(self.enemies)
                    self.needToMakeEnemies = False
                    pygame.event.clear()



                else:
                    currentTime = pygame.time.get_ticks()
                    self.displaySurf.fill(bgColor)
                    self.checkInput()
                    self.allSprites.update(self.keys, currentTime)
                    if len(self.enemies) > 0:
                        self.findEnemyShooter()
                        self.shootEnemyBullet(self.shooter.rect)
                    self.checkCollisions()
                    self.allSprites.draw(self.displaySurf)
                    self.blockerGroup1.draw(self.displaySurf)
                    pygame.display.update()
                    self.checkGameOver()
                    self.clock.tick(self.fps)


if __name__ == '__main__':
    app = App()
    app.mainLoop()
