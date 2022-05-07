#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        if match := re.search('(Len|Neverm)ore', line):
            print(match.group())

if __name__ == "__main__": main()
