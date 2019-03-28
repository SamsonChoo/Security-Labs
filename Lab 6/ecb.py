#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
# Samson, SUTD, 2019

from present import *
import argparse
import binascii

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    in_file = open(infile, mode = 'rb')
    key_file = open(key,mode='r')
    out_file = open(outfile, mode = 'wb+')
    initkey = int(key_file.read(),16)
    
    if (mode.lower()=="e"):
        operation = present
    if (mode.lower()=="d"):
        operation = present_inv
    
    output=[]
    
    block = in_file.read(8)
    while (block != b''):
        blockout = ''
        for i in block:
            blockout += format(i, '08b')
        blockout = int(blockout, 2)

        output.append(binascii.unhexlify('%016x' % operation(blockout, initkey)))

        block = in_file.read(8)

    for byte in output:
        out_file.write(byte)
        
    in_file.close()
    key_file.close()
    out_file.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode

    ecb(infile,outfile,keyfile,mode)


