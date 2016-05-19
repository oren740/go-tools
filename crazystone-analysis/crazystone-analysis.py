#!/usr/bin/python

import sys

if len(sys.argv) < 3:
    print "usage is sgffile then analysis"

sys.path.append("./sgflib1.0")
import sgflib


def run_game(cursor):
    sys.stdout.write("(")
    sys.stdout.write(str(cursor.node))
    cursor.next()
    i = 1
    
    while (True):
        comment = ""
        found_comment = False
        try:
            comment = str(cursor.node["C"])
            found_comment = True
        except:
            pass
        comment = crazystone_analysis[i]
        
        sys.stdout.write(";")
        for j in cursor.node:
            if "C[" in str(j):
                sys.stdout.write("C[" + comment + "]")
            else:
                sys.stdout.write(str(j))
        if not found_comment:
            sys.stdout.write("C[" + comment + "]")
        sys.stdout.write("TR[" + crazystone_move[i] + "]")
        sys.stdout.write("\n")
        if cursor.atEnd:
            sys.stdout.write(")")
            break
        i += 1
        cursor.next()
      
sgffile = open(sys.argv[1])
analysis = open(sys.argv[2])

sgfstring = sgffile.read()
sgfinfo = sgflib.SGFParser(sgfstring)
sgfcollection = sgfinfo.parse()
sgfcursor = sgfcollection.cursor()

crazystone_analysis = {}
crazystone_move = {}

for line in analysis:
    try:
        line = line.replace(", ", ",0")
        move_num = int(line.split()[0])
        crazystone_analysis[move_num] = "Playout:" + line.split()[3] + " P(B wins):" + line.split()[4] + " Situation: " + line.split()[5] + " Dispersion: " + line.split()[6] + " Delta:" + line.split()[8]
        x_coord = chr(ord("a") + (ord(line.split()[7].split(",")[0]) - ord("A")))
        if ord(x_coord) > ord("i"):
            x_coord = chr(ord(x_coord) - 1)
        y_coord = chr(19 - int(line.split()[7].split(",")[1]) + ord("a"))
        crazystone_move[move_num] = str(x_coord) + str(y_coord)
    except:
        pass

run_game(sgfcursor)
