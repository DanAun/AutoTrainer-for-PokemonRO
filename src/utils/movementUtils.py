# Description: Contains utility functions for moving the character in the game
import pyautogui
import logging

from src.utils.battleUtils import isInBattle
from src.utils.configUtils import getConfig, getIntConfig

# Settings
WALK_SPEED = getIntConfig('Walk_Speed')
BIKE_SPEED = getIntConfig('Bike_Speed')
WIGGLE_DISTANCE = getIntConfig('Wiggle_Distance')
WIGGLE_AXES = getConfig('Wiggle_Axes')


def releaseAllKeys():
    keys = ['w', 'a', 's', 'd']
    for key in keys:
        pyautogui.keyUp(key)


def wiggle(distance=WIGGLE_DISTANCE, axes=WIGGLE_AXES, walkSpeed=BIKE_SPEED):
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
