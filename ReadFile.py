if __name__ == '__main__':

    count = 0
    f = open("inputFile.txt", "r")
    passFile = open("passFile.txt", "w")
    failFile = open("failFile.txt", "w")
    for line in f:
        line_split = line.split()
        if line_split[2] == 'P':
            passFile.write(line)
        else:
            failFile.write(line)
    failFile.close()
    passFile.close()
    f.close()


