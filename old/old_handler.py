
    def sendWater(self):
        with open("/etc/food-picker/water.txt", encoding="utf8") as f:
            for line in f:
                if len(line.strip()) == 0:
                    continue
                self.bot.sendVideo(line, "https://media.tenor.com/images/a7eeadb549ca8b4f725a37d4e23ff2ce/tenor.gif")
                self.sendTextMessage(line, "Remember to drink some water!")

    def subscribeToWater(self, chat_id):
        found = False
        path = "/etc/food-picker/water.txt"
        with open(path, encoding="utf8") as f:
            for line in f:
                if line.strip() != str(chat_id):
                    continue
                found = True
        if found:
            self.unsubscribeFromWater(chat_id)
            return
        with open(path, 'a') as f:
            f.write('\n' + str(chat_id))
        self.sendTextMessage(chat_id, "Subscribed to water reminder")

    def unsubscribeFromWater(self, chat_id):
        path = "/etc/food-picker/water.txt"
        content = ""
        with open(path, "r" ) as f:
            lines = f.readlines()
        with open(path, "w") as f:
            for line in lines:
                if line.strip("\n") != str(chat_id) and len(line.strip()) > 0:
                    f.write(line)
        self.sendTextMessage(chat_id, "Unsubscribed to water reminder")
