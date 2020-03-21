
path= "config/exclamations.dat"
with open(path, encoding="utf8") as f:
    for line in f:
        index = line.index(":")
        line = line.replace('\n', "")
        print(line[:index])