#!/usr/local/bin/python3.4

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print(f"Something bad as {e} happened!")

print("OK lets rock")
