# Description: This file contains utility functions for pokemon battles

import pyautogui
import logging
from exceptions import NotInBattleError, BattleTimeoutError
from utils.utils import resourcePath

# Constants
MOUSE_DURATION = 0.2
NUMBER_OF_MOVES = 4
Y_COEFF = 0.10  # 10% of the window height


def getWindowDimensions():
    """Returns the dimensions of the battle window"""
    topLeft = pyautogui.locateCenterOnScreen(resourcePath('images/battle-window-corner.png'),
                                             grayscale=True, confidence=0.9)
    bottomRight = pyautogui.locateCenterOnScreen(resourcePath('images/icons/run-icon.png'), grayscale=True)
    return abs(bottomRight.x - topLeft.x), abs(bottomRight.y - topLeft.y)


def clickFight():
    """Clicks the fight icon"""
    pos = pyautogui.locateCenterOnScreen(resourcePath('images/icons/fight-icon.png'), grayscale=True)
    pyautogui.moveTo(pos.x, pos.y, duration=MOUSE_DURATION)
    pyautogui.click()


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


def spamToWin(moveNr):
    while isInBattle():
        failedAttempts = 0
        try:
            useMove(moveNr)
        except Exception:
            if failedAttempts >= 5:
                raise BattleTimeoutError()
            failedAttempts += 1
            pyautogui.sleep(1)
    logging.debug("Battle ended")
