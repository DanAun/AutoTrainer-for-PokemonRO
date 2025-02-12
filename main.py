import pyautogui
import logging

from utils.battleUtils import spamToWin
from utils.movementUtils import attractWildPokemon


def autoBattle():
    while True:
        attractWildPokemon()
        spamToWin(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    pyautogui.FAILSAFE = True
    welcomeText = """Welcome to the AutoBattler!\nTo exit the battler move mouse to top left corner.\n
                     Press OK to start the autoBattler"""
    reply = pyautogui.confirm(text=welcomeText, title='Confirmation', buttons=['OK', 'Cancel'])
    if not reply == 'OK':
        exit()
    logging.info("Starting the AutoBattler")
    try:
        autoBattle()
    except pyautogui.FailSafeException:
        logging.info("Exiting the AutoBattler")
