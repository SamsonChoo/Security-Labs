import sys
import argparse
import string

printabledict={}
for i in range(len(string.printable)):
    printabledict[i]=string.printable[i]
    
def encrypt_printable(filein="sherlock.txt",fileout="sherlock_encrypted.txt",k=None):
    
    if not isinstance(filein, str):
        raise ValueError("File name must be a string!")
    if not isinstance(fileout, str):
        raise ValueError("File name must be a string!")
    if not isinstance(k, int):
        raise ValueError("Key must be an integer!")
    if(k==None):
        raise ValueError("key is not given!")
    if(k<1)or(k>99):
        raise ValueError("key value must be between 1 and 99!")
    
    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    c    = fin.read()         # read in file into c as a str
    mapped_value = []        # List of mapped integer values from string 
    for char in c:
        mapped_value.append(char_to_val(char)+k)
    fout = open(fileout, mode='w+', encoding='utf-8', newline='\n')      # write mode
    m_modified = ''.join(val_to_char(i) for i in mapped_value)         #convert back into string
    for char in m_modified:
        fout.write(char)            #write to new file
    fin.close()
    fout.close()

def decrypt_printable(filein="sherlock_encrypted.txt",fileout="sherlock_decrypted.txt",k=None):

    if not isinstance(filein, str):
        raise ValueError("File name must be a string!")
    if not isinstance(fileout, str):
        raise ValueError("File name must be a string!")
    if not isinstance(k, int):
        raise ValueError("Key must be an integer!")
    if(k==None):
        raise ValueError("key is not given!")
    if(k<1)or(k>99):
        raise ValueError("key value must be between 1 and 99!")
        
    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    c    = fin.read()         # read in file into c as a str
    mapped_value = []        # List of mapped integer values from string
    for char in c:
        mapped_value.append(char)
    m = ''.join(val_to_char(char_to_val(i)-k) for i in mapped_value)     #convert back into string
    fout = open(fileout, mode='w+', encoding='utf-8', newline='\n')      # write mode
    for char in m:
        fout.write(char)            #write to new file
    fin.close()
    fout.close()
    
def encrypt_binary(filein="sherlock.txt",fileout="sherlock_encrypted.txt",k=None):
    
    if not isinstance(filein, str):
        raise ValueError("File name must be a string!")
    if not isinstance(fileout, str):
        raise ValueError("File name must be a string!")
    if not isinstance(k, int):
        raise ValueError("Key must be an integer!")
    if(k==None):
        raise ValueError("key is not given!")
    if(k<0)or(k>255):
        raise ValueError("key value must be between 0 and 255!")
    
    fin  = open(filein, mode='rb')       # binary read mode
    c    = bytearray(fin.read())         # read in file into c
    fout = open(fileout, mode='wb+')      # write mode
    msg_out = bytearray(b"")            #initialise empty bytearray string
    for char in c:
        msg_out.append((char+k)%256)
    fout.write(msg_out)
    fin.close()
    fout.close()

def decrypt_binary(filein="sherlock_encrypted.txt",fileout="sherlock_decrypted.txt",k=None):
    
    if not isinstance(filein, str):
        raise ValueError("File name must be a string!")
    if not isinstance(fileout, str):
        raise ValueError("File name must be a string!")
    if not isinstance(k, int):
        raise ValueError("Key must be an integer!")
    if(k==None):
        raise ValueError("key is not given!")
    if(k<0)or(k>255):
        raise ValueError("key value must be between 0 and 255!")
    
    fin  = open(filein, mode='rb')       # binary read mode
    c    = fin.read()         # read in file into c
    fout = open(fileout, mode='wb+')      # write mode
    msg_out = bytearray(b"")            #initialise empty bytearray string
    for char in c:
        msg_out.append((char-k)%256)
    fout.write(msg_out)
    fin.close()
    fout.close()
    
def char_to_val(char):
    """
    Convert string character into value mapped by string.printable
    """
    if not isinstance(char, str):
        raise ValueError("Input must be a string!")
    return(list(printabledict.keys())[list(printabledict.values()).index(char)])

def val_to_char(val):
    """
    Convert value mapped by string.printable into string characters
    """
    if not isinstance(val, int):
        raise ValueError("Input must be a Integer!")
    if(val<0)or(val>99):
        raise ValueError("Input must be between 0 and 99!")
    return printabledict[val]


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key',help='cipher key')
    parser.add_argument('-m', dest='mode',help='encryption/decryption mode')
    parser.add_argument('-t', dest='type',help='input type')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    k = int(args.key)
    mode = args.mode
    input_type = args.type
    
    if not(type(mode)is str):
        raise ValueError("Please enter your mode parameter 'm'! E for encryption or D for decryption")
    elif not(type(input_type)is str):
        raise ValueError("Please enter your input type parameter 't'! P for printable or B for binary")
    
    elif(mode.upper()=="E"):       #Encryption
        if(input_type.upper()=="P"):          #printable
            encrypt_printable(filein=filein,fileout=fileout,k=k)
        elif(input_type.upper()=="B"):          #binary
            encrypt_binary(filein=filein,fileout=fileout,k=k)
        else:
            raise ValueError("Please enter your input type parameter 't'! P for printable or B for binary")
            
    elif(mode.upper()=="D"):        #Decryption
        if(input_type.upper()=="P"):
            decrypt_printable(filein=filein,fileout=fileout,k=k)
        elif(input_type.upper()=="B"):
            decrypt_binary(filein=filein,fileout=fileout,k=k)
        else:
            raise ValueError("Please enter your input type parameter 't'! P for printable or B for binary")
    else:
        raise ValueError("Please enter your mode parameter 'm'! E for encryption or D for decryption")