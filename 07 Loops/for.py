#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

def main():
    #    first example
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line)

    #    second example
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's':
            print(f'index {i} is an s')


if __name__ == "__main__": main()
