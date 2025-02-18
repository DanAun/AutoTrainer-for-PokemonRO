import os
import logging
import pyautogui
from ast import literal_eval

from src.utils.configUtils import CONFIG_FILE, getBoolConfig, getConfig, getIntConfig, initConfig
if not os.path.isfile(CONFIG_FILE):
    logging.info("Config file not found, creating a new one")
    initConfig()

from src.utils.battleUtils import spamMove, switchToPokemon
from src.exceptions import ConfigFileError
from src.utils.movementUtils import attractWildPokemon, releaseAllKeys


def autoTraining(PP):
    """Auto battles until PP runs out"""
    for i in range(len(PP)):
        while PP[i] > 0:
            attractWildPokemon()
            PP[i] -= spamMove(i+1)


def switchTraining(PP, pokemonNr):
    """Like autoTraining but switches pokemon first thing in the battle. Useful for training weak pokemon"""
    for i in range(len(PP)):
        while PP[i] > 0:
            attractWildPokemon()
            switchToPokemon(pokemonNr)
            PP[i] -= spamMove(i+1)


def displayWelcomeMessage():
    welcomeText = """Welcome to the AutoBattler!\nTo exit the battler move mouse to top left corner of the screen!\nCustomize possible in 'config.ini'\nPress OK to start the AutoBattler"""
    reply = pyautogui.confirm(text=welcomeText, title='Confirmation', buttons=['OK', 'Cancel'])
    if not reply == 'OK':
        exit()


def main():
    if getBoolConfig('Display_Welcome_Message'):
        displayWelcomeMessage()

    logging.info("Starting the AutoBattler")
    trainingType = getConfig('Training_Type')
    PP = literal_eval(getConfig('Power_Point'))
    match trainingType:
        case 'normal':
            autoTraining(PP)
        case 'switch':
            switchTraining(PP, getIntConfig('Switch_Pokemon'))
        case _:
            logging.error("Invalid training type")
            raise ConfigFileError()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    pyautogui.FAILSAFE = True
    try:
        main()
    except pyautogui.FailSafeException:
        pyautogui.FAILSAFE = False
        releaseAllKeys()
        logging.info("FailSafe triggered, exiting the AutoBattler")
