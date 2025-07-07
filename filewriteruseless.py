from random import randint
with open('somefile.txt', 'w') as the_file:
    the_file.write("1000\n")
    for i in range(1, 1000):
        the_file.write("100000000 ")
    the_file.write("\n2000\n")

    for i in range(1, 30):
        num = randint(1, 3)
        if (1 == num):
            the_file.write("2\n")
        if (2 == num):
            the_file.write("3\n")
        # if(1 == num):
        # the_file.write("1 1 10000 100000000\n")
