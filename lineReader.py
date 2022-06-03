def read_large_file(filename):
    with open(filename) as file:
        for line in file:
            print(line.rstrip() + "\n")


if __name__ == '__main__':
    read_large_file("temp_big.txt")
