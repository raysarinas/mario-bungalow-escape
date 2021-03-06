import pygame, sys, time
from board import *
from walls import *
from characters import *
from pygame.locals import *

BLACK = (0, 0, 0)

class Game:
    # class attributes
    #background colur

    def __init__(self, surface):
        self.surface = surface
        self.exit = False
        self.cont = True
        self.radius = 10
        self.player = Player(self.surface)
        #self.peach = Peach(self.surface)
        self.kong = DonkeyKong(self.surface)
        self.fireball = Fireball(self.surface)
        self.counter = time.time()
        self.princess = PrincessPeach(self.surface)
        self.all_sprite_list = pygame.sprite.Group()
        self.walllist, self.all_sprite_list = makeWalls(self.all_sprite_list)
        self.platforms = pygame.sprite.Group()
        #self.board = Board(self.surface)
        #self.fireballs = [Fireball(self.surface)] # maybe use an array to store fireballs and then
        # when updating just for-loop and draw all of them? idk
        pygame.key.set_repeat(20, 20)

    def play(self):
        # play until player closes box i guess
        self.draw()
        while not self.exit:
            self.handle_event()
            if self.cont:
                self.update()
                self.should_continue()
                # self.check() # check endgame conditions
            self.draw()
            self.all_sprite_list.update()
            self.all_sprite_list.draw(self.surface)
            pygame.display.flip()
            time.sleep(0.02) # frame delay time

    def handle_event(self):
        event = pygame.event.poll()
        if event.type == QUIT:
            self.exit = True
        if event.type == KEYDOWN and self.cont:
            if event.key == K_UP:
                self.player.move_vert(self.player.rect, -1) # move up
            if event.key == K_DOWN:
                self.player.move_vert(self.player.rect, 1) # move down
            if event.key == K_LEFT:
                self.player.move_horiz(self.player.rect, -1) # move left
            if event.key == K_RIGHT:
                self.player.move_horiz(self.player.rect, 1) # move right
            elif event.key == pygame.K_SPACE:
                self.player.jump()


    def draw(self):
        # THIS SEEMS LIKE IT WILL GET TO BE TOO LONG IF WE NEED TO DRAW
        # TOO MANY THINGS. MIGHT NEED TO KEEP GAME CLASS IN DIFFERENT FILE
        # OR HAVE DRAW FUNCTION BE A SUBCLASS OR WHATEVER OR SOMETHING
        self.surface.fill(BLACK)
        self.kong.draw()
        #self.peach.draw()
        self.fireball.draw()
        self.princess.draw()
        self.player.draw()
        # #self.board.initialize()
        # wallColor = pygame.Color('black')

        pygame.display.update()

    def update(self):
        # update game objects
        self.fireball.move(self.walllist)
        # if (self.counter - time.time()) // 5 == 0:
        #     self.fireball.draw()


    def should_continue(self):
        # check and remember if game should continue
        pass

    def check(self):
        # self.iswin() # win game condition
        # self.islose() # DIE condition
        pass

def main():
    pygame.init() # initialize pygame
    # set window size, title, frame delay and create pygame window
    surface = pygame.display.set_mode([600,400], 0, 0)
    # sets the title of the window
    pygame.display.set_caption('275 Final Project - DonPy thong')
    # create and initialize objects
    gameOver = False
    game = Game(surface)
    game.play()
    pygame.quit()

main()
