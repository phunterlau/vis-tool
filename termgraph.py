#!/usr/bin/env python
# coding=utf-8

# termgraph.py - draw basic graphs on terminal
# https://github.com/mkaz/termgraph

# Marcus Kazmierczak
# http://mkaz.com/

# modified by Hongliang Liu
# usage: cat a two column file to this script where the first column is the label, second column is the data

from __future__ import print_function

#import argparse
import sys

#TODO: change tick character
tick = '▇'
sm_tick = '|'

# sample bar chart data
#labels = ['2007', '2008', '2009', '2010', '2011']
#data = [183.32, 231.23, 16.43, 50.21, 508.97]

try:
    range = xrange
except NameError:
    pass

def main():

    # determine type of graph
    
    # read data
    if len(sys.argv)>1: #has a parameter, use it as filename
        labels, data = read_data(sys.argv[1])
    else: #use stdin
        labels, data = read_data_std()

    # verify data
    m = len(labels)
    if m != len(data):
        print(">> Error: Label and data array sizes don't match")
        sys.exit(1)

    # massage data
    ## normalize for graph
    max = 0
    for i in range(m):
        if data[i] > max:
            max = data[i]

    #step = max / args['width']
    step = max/50
    # display graph
    for i in range(m):
        print_blocks(labels[i], data[i], step)

    print()


def print_blocks(label, count, step):
    #TODO: add flag to hide data labels
    blocks = int(count / step)
    print("{}: ".format(label), end="")
    if count < step:
        sys.stdout.write(sm_tick)
    else:
        for i in range(blocks):
            sys.stdout.write(tick)

    #print("{:>9.2f}".format(count))
    print("\-  %.2f"%count)

def read_data(filename):

    labels = []
    data = []

    f = open(filename, "r")
    for line in f:
        line = line.strip()
        if line:
            if not line.startswith('#'):
                if line.find(",") > 0:
                    cols = line.split(',')
                else:
                    cols = line.split()
                labels.append(cols[0].strip())
                data_point = cols[1].strip()
                data.append(float(data_point))

    f.close()
    return labels, data

def read_data_std():
    print("\n")

    labels = []
    data = []

    #f = open(filename, "r")
    for line in sys.stdin:
        line = line.strip()
        if line:
            if line.find(",") > 0:
                cols = line.split(',')
            else:
                cols = line.split()
            labels.append(cols[0].strip())
            data_point = cols[1].strip()
            data.append(float(data_point))

    return labels, data 

if __name__ == "__main__":
    main()
