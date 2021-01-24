#!/usr/bin/env python3

# Created by: Marlon Poddalgoda
# Created on: December 2020
# This program is the "Break-out" program on the PyBadge

import ugame
import stage
import time
import random
import supervisor

import constants


def splash_scene():
    # this function is the splash scene
    
    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    
    # image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # stage for background and constant fps
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    
    # stage for background and fps settings
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = [background]
    # render all text and background
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

def menu_scene():
    # this function is the menu game_scene
    
    # image bank
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
    
    # sets the background to image 0 in the image banks
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y)
    
    # stage for background and fps settings
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render all text and background
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # Start button selected
        if keys & ugame.K_START != 0:
            game_scene()
        
        # update game logic
        game.tick()

def game_scene():
    # this function is the main game_scene
    
    class Ball(stage.Sprite):
        def __init__(self, x, y):
            super().__init__(bank, 1, x, y)
            self.dx = 2
            self.dy = 1
 
        def update(self):
            super().update()
            self.set_frame(self.frame % 4 + 1)
            self.move(self.x + self.dx, self.y + self.dy)
            if not 0 < self.x < 144:
                self.dx = -self.dx
            if not 0 < self.y < 112:
                self.dy = -self.dy
 
    # image bank of sprites
    bank = stage.Bank.from_bmp16("ball.bmp")
    
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # background tiles
    background = stage.Grid(bank, 10, 8)
    
    # ball sprite + initial coordinates
    ball1 = Ball(80, 100)
    sprites = [ball1]
    
    # paddle sprites
    paddle = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - 20)
    
    # background with constants fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites, items show up in order
    game.layers = sprites + [paddle] + [background]
    # render all sprites
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_X != 0:
            pass
        
        # right D-pad movement
        if keys & ugame.K_RIGHT != 0:
            if paddle.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                paddle.move(paddle.x + 3, paddle.y)
            else:
                paddle.move(constants.SCREEN_X - constants.SPRITE_SIZE, paddle.y)
        
        # left D-pad movement
        if keys & ugame.K_LEFT != 0:
            if paddle.x >= 0:
                paddle.move(paddle.x - 3, paddle.y)
            else:
                paddle.move(0, paddle.y)
        
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        
            
        ball1.update()
        game.render_sprites(sprites + [paddle])
        game.tick()
    

if __name__ == "__main__":
    game_scene()
