#!/usr/bin/env python3

# Created by: Marlon Poddalgoda
# Created on: December 2020
# This constants file is for the "Breakout" game

#PyBadge screen size is 160x128 and sprites 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_LASERS = 5
BALL_SPEED= 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 40
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
  "button_up": "up",
  "button_just_pressed": "just pressed",
  "button_still_pressed": "still pressed",
  "button_released": "released"
}

# new pallet for red filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
               b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

BLUE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

