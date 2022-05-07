#!/usr/local/bin/python3.4
# By Amir Hassan Azimi [http://parsclick.net/]


from bwDB import bwDB
from bwConfig import configFile
import random
import os

__version__ = "1.0.1"

g = dict(
    config_file = 'db.conf',
    table_name = 'testimonial'
)

def main():
    init()
    db = g['db']
    idlist = [r[0] for r in db.sql_query(f" SELECT id FROM {g['table_name']} ")]

    # get the count of records to display
    try: count = int(os.environ.get('QUERY_STRING', 3))
    except ValueError: error("Invalid query string, must be a number")
    idcount = len(idlist)

    # check that the count is not too big
    maxcount = idcount // 4
    if count > maxcount:
        error(
            (
                f'There are {idcount} records in the database. '
                + f'For good randomness, you cannot display more than {maxcount} at a time.'
            )
        )


    # build the list of random ids
    result_ids = []
    while len(result_ids) < count:
        randindex = random.randint(0, len(idlist) - 1)
        randid = idlist[randindex]
        del idlist[randindex]   # don't use that one again
        result_ids += [ randid ]

    # display them
    for id in result_ids:
        printrec(id)

def printrec(id):
    db = g['db']
    rec = db.getrec(id)
    print('<div class="testimonial">')
    print(f"""<p class="testimonial">{rec['testimonial']}</p>""")
    print(f"""<p class="byline">&mdash;{rec['byline']}</p>""")
    print('</div>')


def init():
    send_header()
    g['config'] = configFile(g['config_file']).recs()
    g['db'] = bwDB(filename = g['config']['db'], table = g['table_name'])

def send_header():
    print('Content-type: text/html\n\n', end = '')

def error(e):
    print(e)
    exit(0)

if __name__ == "__main__": main()

