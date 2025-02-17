# Description: Contains utility functions for moving the character in the game
import pyautogui
import logging

from utils.battleUtils import isInBattle

# Options
DEFAULT_WALK_SPEED = 1
DEFAULT_BIKE_SPEED = 10
DEFAULT_WIGGLE_DISTANCE = 5
DEFAULT_WIGGLE_AXES = 'x'


def releaseAllKeys():
    keys = ['w', 'a', 's', 'd']
    for key in keys:
        pyautogui.keyUp(key)


def wiggle(distance=DEFAULT_WIGGLE_DISTANCE, axes=DEFAULT_WIGGLE_AXES, walkSpeed=DEFAULT_BIKE_SPEED):
    """Moves the character distance back and forth on the specified axes"""
    match axes:
        case 'x':
            forward = 'd'
            backward = 'a'
        case 'y':
            forward = 'w'
            backward = 's'
        case _:
            raise ValueError("Invalid axes")
    pyautogui.keyDown(forward)
    pyautogui.sleep(distance / walkSpeed)
    pyautogui.keyUp(forward)
    pyautogui.keyDown(backward)
    pyautogui.sleep(distance / walkSpeed)
    pyautogui.keyUp(backward)


def attractWildPokemon():
    while not isInBattle():
        wiggle()
    logging.debug("Battle started")
