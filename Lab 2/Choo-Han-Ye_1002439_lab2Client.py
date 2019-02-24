#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG, 2019
# Samson Choo, 2019

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote

# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r

def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    
    # decrypt the challenge here
    ## print(challenge.decode('utf-8'))
    
    # attempt to build own frequency analysis list from sherlock.txt, did not work well
#     import string
#     d={}
#     with open("sherlock-Copy1.txt", mode="r", encoding='utf-8', newline='\n') as fin:
#         text = fin.read()
#         for char in text:
#             if char.isalpha():
#                 char=char.lower()
#             if char not in d:
#                 d[char]=100/len(text)
#             else:
#                 d[char]+=100/len(text)
#     import operator
#     max(d.items(), key=operator.itemgetter(1))
#     frequencylist = sorted(d, key=d.__getitem__)[::-1]
#     for key, value in sorted(d.items(), key=lambda item: (item[1], item[0])):
#         print ("%s: %s" % (key, value))
#     print(frequencylist)
    
    
    # using hardcoded frequency list found online instead
    frequencylist = [' ','e','t','a','o','h','r','n','d','i','s','l','w','\n','g',',','u','c','m','y','f','p','.','b','k','v','\"','-','\'','j','q','?','\t']
        
    d={}
    for char in challenge:
        if char not in d:
            d[char]=100/len(challenge)     # percentage of appearance
        else:
            d[char]+=100/len(challenge)
            
    import operator
    ## for key, value in sorted(d.items(), key=lambda item: (item[1], item[0])):     # sort according to appearance percentage
        ## print ("%s: %s" % (key, value))
    frequencylist2 = sorted(d, key=d.__getitem__)[::-1]     # frequency list of received text
    ## print(frequencylist2)
    
    decoded = ""     # initialise decoded solution
    for char in challenge:
        replacedword = frequencylist[frequencylist2.index(char)]
        if replacedword == "?":
            decoded += "q"
        elif replacedword == "q":
            decoded += "?"
        else:
            decoded+=replacedword
    solution = decoded
    print(solution)
    
    # end of decryption
    # solution = int(0).to_bytes(7408, 'big')
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    if message == b'Congratulations! Similarity: 1.0\n':
        conn.close()


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    ## print(challenge)
    # some all zero mask.
    # TODO: find the magic mask!
    ## hardcoded mask
    mask = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04\x03\x09\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'
    ## print(mask)
    a = b"Student ID 1000000 gets 0 points."
    b = b"Student ID 1002439 gets 4 points."
    mask = XOR(a,b)
    print(mask)
    message = XOR(mask, challenge)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'exact' in message:
        print(message)
    conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '157.230.47.126'
    PORT = 1337

    # sol1()
    sol2()
