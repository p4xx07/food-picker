import os

def readConfig(path) -> {}:
    d = {}
    with open(path) as f:
        for line in f:
            (key, val) = line.split("=")
            d[key] = val.replace('\n', '')
    return d

def get(): 
    config_path = "/etc/food-picker/config.dat"

    if os.name == 'nt':
        config_path = r'C:\Users\pc\Documents\etc\food-picker\config.dat'

    config_dictionary = readConfig(config_path)

    token = config_dictionary["token"]
    gif_url = config_dictionary["gif_url"]
    chat_id = config_dictionary["chat_id"]
    
    return (token, gif_url, chat_id)
