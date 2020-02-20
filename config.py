def readConfig(path) -> {}:
    d = {}
    with open(path) as f:
        for line in f:
            (key, val) = line.split("=")
            d[key] = val.replace('\n', '')
    return d

class Config():
    def __init__(self, path):
        self.path = path
        config_path = "/etc/food-picker/config.dat"
        config_dictionary = readConfig(config_path)

        self.token = config_dictionary["token"]
        self.gif_url = config_dictionary["gif_url"]
        self.chat_id = config_dictionary["chat_id"]

