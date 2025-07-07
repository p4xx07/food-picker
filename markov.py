from random import randint
potter_text = None


def read_harry_potter():
    harry_potter = ""
    with open("/etc/food-picker/harrypotter.txt", encoding="utf8") as f:
        for line in f:
            harry_potter = harry_potter + line
    return harry_potter


def generate_text(input, words):
    manager = Manager(input)
    finalString = ""
    output = manager.generate_first_output()
    for i in range(0, words):
        if output and len(output.strip()) > 0:
            if not finalString:
                finalString = output
            else:
                finalString = f"{finalString} {output}"
        output = manager.generate_output(output)
    return finalString


def get_potter(count):
    global potter_text
    if not potter_text:
        potter_text = read_harry_potter()
    return generate_text(potter_text, count)


class State:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def attach(self, key):
        if key not in self.connections:
            self.connections[key] = 0

        self.connections[key] = self.connections[key] + 1

    def get_connections(self):
        return self.connections

    def generate_markov_output(self):
        if len(self.connections) == 0:
            return ""

        total_connection_sum = 0
        for key in self.connections:
            total_connection_sum = total_connection_sum + self.connections[key]

        random = randint(0, 100) / 100 * total_connection_sum
        partial_sum = 0

        for key in self.connections:
            partial_sum = partial_sum + self.connections[key]
            if random <= partial_sum:
                return key
        return ""

    def generate_first_output(self):
        if len(self.connections) == 0:
            return ""

        keys = self.connections.keys()
        key_iterator = iter(keys)
        first_value = next(key_iterator)
        return first_value


class Manager():
    def __init__(self, text):
        self.states = {}
        self.text = text
        self.create_states()

    def add_state(self, key) -> State:
        if key in self.states:
            return self.states[key]
        state = State(key)
        self.states[key] = state
        return state

    def create_states(self):
        words = self.text.split()
        for i in range(0, len(words)):
            state = self.add_state(words[i])
            if i < len(words) - 1:
                state.attach(words[i + 1])

    def get_state(self, key):
        return self.states[key]

    def generate_output(self, key) -> str:
        if key not in self.states:
            return ""
        state = self.states[key]
        return state.generate_markov_output()

    def generate_first_output(self):
        values = self.states.values()
        value_iterator = iter(values)
        first_state = next(value_iterator)
        return first_state.generate_first_output()
