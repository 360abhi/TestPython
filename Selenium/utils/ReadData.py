import configparser

config = configparser.ConfigParser()
config.read('Selenium/Config/paths.properties')


class Read:

    INPUT_DATA = config.get('FILE','input_file')