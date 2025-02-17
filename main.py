import pyautogui
import logging

from utils.battleUtils import spamToWin, switchPokemon
from utils.movementUtils import attractWildPokemon, releaseAllKeys


def autoBattle():
    while True:
        attractWildPokemon()
        spamToWin(1)


def autoPPBattle(PP):
    for i in range(4):
        while PP[i] > 0:
            attractWildPokemon()
            PP[i] -= spamToWin(i+1)
            print(PP[i])


def carryAutoBattle(CarryPokemon):
    while True:
        attractWildPokemon()
        switchPokemon(CarryPokemon)
        spamToWin(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    pyautogui.FAILSAFE = True
    welcomeText = """Welcome to the AutoBattler!\nTo exit the battler move mouse to top left corner.\nPress OK to start the autoBattler"""
    reply = pyautogui.confirm(text=welcomeText, title='Confirmation', buttons=['OK', 'Cancel'])
    if not reply == 'OK':
        exit()
    logging.info("Starting the AutoBattler")
    try:
        # carryAutoBattle(2)
        PP = [15, 10, 15]
        autoBattle()
    except pyautogui.FailSafeException:
        releaseAllKeys()
        logging.info("Exiting the AutoBattler")
