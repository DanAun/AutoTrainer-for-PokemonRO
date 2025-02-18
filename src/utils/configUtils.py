import configparser

CONFIG_FILE = 'config.ini'


def getConfig(value, section='Settings'):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.get(section, value)


def getBoolConfig(value, section='Settings'):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.getboolean(section, value)


def getIntConfig(value, section='Settings'):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.getint(section, value)


def getFloatConfig(value, section='Settings'):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.getfloat(section, value)


def initConfig():
    config = configparser.ConfigParser()
    config['Settings'] = {
                            'training_type': 'normal',
                            'power_point': '[10, 10, 10, 10]',
                            'switch_pokemon': '2',
                            'mouse_duration': '0.05',
                            'walk_speed': '1',
                            'bike_speed': '10',
                            'wiggle_distance': '5',
                            'wiggle_axes': 'x',
                            'display_welcome_message': 'yes'}

    config['Constants'] = {
                            'NUMBER_OF_MOVES': '4',
                            'Y_COEFF': '0.10',
                            'X_COEFF': '0.10'}

    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)
