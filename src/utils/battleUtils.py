# Description: This file contains utility functions for pokemon battles

import pyautogui
import logging
from src.exceptions import NotInBattleError, BattleTimeoutError
from src.utils.configUtils import getFloatConfig, getIntConfig
from src.utils.buildUtils import resourcePath

# Constants
NUMBER_OF_MOVES = getIntConfig('NUMBER_OF_MOVES', 'Constants')
Y_COEFF = getFloatConfig('Y_COEFF', 'Constants')
X_COEFF = getFloatConfig('X_COEFF', 'Constants')

# Settings
MOUSE_DURATION = getFloatConfig('Mouse_Duration')


def getWindowDimensions():
    """Returns the dimensions of the battle window"""
    topLeft = pyautogui.locateCenterOnScreen(resourcePath('images/battle-window-corner.png'),
                                             grayscale=True, confidence=0.9)
    bottomRight = pyautogui.locateCenterOnScreen(resourcePath('images/icons/run-icon.png'), grayscale=True)
    return abs(bottomRight.x - topLeft.x), abs(bottomRight.y - topLeft.y)


def clickFight():
    """Clicks the fight icon"""
    pos = pyautogui.locateCenterOnScreen(resourcePath('images/icons/fight-icon.png'), grayscale=True, confidence=0.8)
    pyautogui.moveTo(pos.x, pos.y, duration=MOUSE_DURATION)
    pyautogui.click()


def clickPokemon():
    """Clicks the pokemon icon"""
    pos = pyautogui.locateCenterOnScreen(resourcePath('images/icons/pokemon-icon.png'), grayscale=True, confidence=0.8)
    pyautogui.moveTo(pos.x, pos.y, duration=MOUSE_DURATION)
    pyautogui.click()


def switchToPokemon(pokemonNr):
    """Switches to the given pokemon number"""
    if pokemonNr not in range(1, 7):
        raise ValueError("Invalid pokemon number")
    if not isInBattle():
        logging.error("Not in battle while trying to switch pokemon")
        raise NotInBattleError()
    try:
        waitForMyTurn()
        clickPokemon()
    except NotInBattleError:
        logging.error("Not in battle while trying to switch pokemon")
        raise NotInBattleError()
    x, y = getWindowDimensions()
    Y_Unit = y * Y_COEFF
    X_Unit = x * X_COEFF
    baseOffset = -2 * Y_Unit
    pokemonInv = 4 - int(pokemonNr/2)
    pokemonIconHeight = 1.3 * Y_Unit
    pokemonOffset = -pokemonInv * pokemonIconHeight
    Y_offset = baseOffset + pokemonOffset
    X_baseOffset = -2 * X_Unit
    X_offset = (pokemonNr % 2) * X_baseOffset
    pyautogui.move(X_offset, Y_offset, duration=MOUSE_DURATION)
    pyautogui.click()
    logging.debug(f"Switched to pokemon {pokemonNr}")


def useMove(moveNr):
    """Uses the given move number"""
    if moveNr not in range(1, NUMBER_OF_MOVES + 1):
        raise ValueError("Invalid move number")
    if not isInBattle():
        logging.error("Not in battle while trying to select move")
        raise NotInBattleError()
    _, y = getWindowDimensions()
    clickFight()
    Y_Unit = y * Y_COEFF
    baseOffset = -2 * Y_Unit
    moveInv = (NUMBER_OF_MOVES + 1) - moveNr
    moveIconHeight = 1.2 * Y_Unit
    moveOffset = -moveInv * moveIconHeight
    offset = baseOffset + moveOffset
    pyautogui.move(0, offset, duration=MOUSE_DURATION)
    pyautogui.click()


def isInBattle():
    try:
        pyautogui.locateCenterOnScreen(resourcePath('images/battle-window-corner.png'), grayscale=True, confidence=0.9)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def isMyTurn():
    """Checks if it is the player's turn my checking if the run icon is visible"""
    try:
        pyautogui.locateCenterOnScreen(resourcePath('images/icons/run-icon.png'), grayscale=True)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def waitForMyTurn(timeout=15):
    """Waits for the player's turn"""
    logging.debug("Waiting for my turn")
    timeoutCnt = 0
    while not isMyTurn():
        if not isInBattle():
            raise NotInBattleError()
        if timeoutCnt >= timeout*10:
            raise BattleTimeoutError()
        timeoutCnt += 1
        pyautogui.sleep(0.1)


def spamMove(moveNr):
    """Spams the given move number until the battle ends, returns the number of moves used"""
    moveCnt = 0
    while isInBattle():
        try:
            waitForMyTurn()
            useMove(moveNr)
            moveCnt += 1
        except NotInBattleError:
            break
    logging.debug("Battle ended, used %d moves", moveCnt)
    return moveCnt
