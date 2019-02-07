"""
Function to validate that the decrypted file is same as the original file.
"""


import filecmp
import sys

originalfile = sys.argv[1]
decyrptedfile  = sys.argv[2]

print(filecmp.cmp(originalfile,decyrptedfile))