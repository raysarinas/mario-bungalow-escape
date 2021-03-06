# character classes should be put here later for better organization i guess
# like mario/player, peach, and donkey kong classes.
# also enemy classes like barrels, fireballs, etc.
import pygame, sys, time, board, random
from pygame.locals import *
vec = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.surface = game
        self.surface_size = self.surface.get_size()
        self.color = pygame.Color('red')
        self.rect = Rect(10, self.surface_size[1] - 40, 20, 20)


        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

    def draw(self):
        #pygame.draw.rect(self.surface, self.color, self.rect)
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load('mario.png').convert_alpha()
        sprite.rect = sprite.image.get_rect()
        self.surface.blit(sprite.image, self.rect)

    def move_vert(self, rect, direction):
        size = self.surface.get_size()
        if direction < 0 and rect.top > 10:
                rect.y = rect.y + direction * 10
        if direction > 0 and rect.bottom < size[1] - 20:
                rect.y = rect.y + direction * 10

    def move_horiz(self, rect, direction):
        size = self.surface.get_size()
        if direction < 0 and rect.left > 10:
            rect.x = rect.x + direction * 10
            #self.vx = -5
        if direction > 0 and rect.right < size[0] - 10:
            rect.x = rect.x + direction * 10
            #self.vx = 5


# class Player: # player class. could possible change this to have options to have different players/colors
#     # need to add conditions so doesnt go through structures/walls/platforms
#     # CONDITIONS SHOULD USE collidepoint function call with rectangles and stuff i think
#
#     def __init__(self, surface):
#         self.surface = surface
#         self.surface_size = self.surface.get_size()
#         self.color = pygame.Color('red')
#         self.rect = Rect(10, self.surface_size[1] - 30, 20, 20)
#
#
#         self.vel = vec(0, 0)
#         self.acc = vec(0, 0)
#
#
#     def draw(self):
#         pygame.draw.rect(self.surface, self.color, self.rect)
#
#     def move_vert(self, rect, direction):
#         size = self.surface.get_size()
#         if direction < 0 and rect.top > 10:
#                 rect.y = rect.y + direction * 10
#         if direction > 0 and rect.bottom < size[1] - 10:
#                 rect.y = rect.y + direction * 10
#
#     def move_horiz(self, rect, direction):
#         size = self.surface.get_size()
#         if direction < 0 and rect.left > 10:
#             rect.x = rect.x + direction * 10
#             #self.vx = -5
#         if direction > 0 and rect.right < size[0] - 10:
#             rect.x = rect.x + direction * 10
#             #self.vx = 5
#
#     def jump(self):
#         # # jump only if standing on a platform
#         # self.rect.x += 1
#         # hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
#         # self.rect.x -= 1
#         # if hits:
#         self.vel.y = -10

class Fireball:

    def __init__(self, surface):
        self.surface = surface
        self.radius = 5
        self.center = [55, 40]
        self.color = pygame.Color('yellow')
        self.randomspeed = random.randint(1, 5)
        self.speed = [6, 7]
        self.surface_size = self.surface.get_size()
        self.walls = None

    def draw(self):
        #pygame.draw.circle(self.surface, self.color, self.center, self.radius)
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load('fireball.png').convert_alpha()
        sprite.rect = sprite.image.get_rect()
        self.surface.blit(sprite.image, [self.center[0] - 5, self.center[1] - 5])

    def move(self, walllist): # add in more parameters/arguments when walls are drawn
        for coord in range(2):
            self.center[coord] = (self.center[coord] + self.speed[coord])

             # change direction if top or left
            if self.center[coord] < self.radius + 15:
                self.speed[coord] = -self.speed[coord]

             # change direction if bottom or right
            if self.center[coord] + self.radius > self.surface_size[coord] - 15:
                self.speed[coord] = -self.speed[coord]

            walls = walllist
            for wall in walls:
                pass # this should check collisions but not sure how to do that yet

# class Peach:
#     peachColor = pygame.Color('pink') # replace with sprite?
#
#     def __init__(self, surface):
#         self.surface = surface
#         self.surface_size = self.surface.get_size()
#         self.color = pygame.Color('pink')
#         self.rect = Rect(self.surface_size[0] - 30, 10, 20, 20)
#
#     def draw(self):
#         pygame.draw.rect(self.surface, self.color, self.rect)

class DonkeyKong:
    kongColor = pygame.Color('brown')

    def __init__(self, surface):
        self.surface = surface
        self.radius = 30
        self.center = [40, 40]
        self.color = DonkeyKong.kongColor

    def draw(self):
        #pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load('bowser.png.gif').convert_alpha()
        sprite.rect = sprite.image.get_rect()
        self.surface.blit(sprite.image, [self.center[0] - 30, self.center[1] - 30])

class PrincessPeach:
    def __init__(self, surface):
        self.surface = surface
        self.surface_size = self.surface.get_size()
        self.location = [self.surface_size[0] - 30, 10]

    # def makeImage(self):
    #     file = 'peach.png'
    #     image = pygame.image.load(file)
    #     return image

    def draw(self):
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.image.load('peach.png').convert_alpha()
        sprite.rect = sprite.image.get_rect()
        self.surface.blit(sprite.image, self.location)
        # image = self.makeImage()
        # self.surface.blit(image, self.location)
