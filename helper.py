def read_as_dictionary(path) -> {}:
    dictionary = {}
    with open(path, encoding="utf8") as f:
        i = 0
        for line in f:
            res = line.replace('\n', '')
            dictionary[int(i)] = res
            i += 1
    return dictionary
