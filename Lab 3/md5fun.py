import hashlib
import time
import itertools as it
import string
import random

#takes 4065.817893266678 seconds
def bruteforce(filein):
    starttime = time.time()
    hashlist=[]
    returnlist = []
    found=0
    possible_characters="1234567890qwertyuiopasdfghjklzxcvbnm"
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        for line in fin:
            hashlist.append(line[:-1])
        for tup in it.product(possible_characters,repeat=5):
            guess = "".join(tup)
            for line in hashlist:
                if line == hashlib.md5(bytearray(guess,encoding="utf-8")).hexdigest():
                    print(str(guess)+" found!")
                    returnlist.append(guess)
                    if found!=14:
                        found+=1
                    else:
                        totaltime = time.time()-starttime
                        print("Total time taken for brute force: " + str(totaltime))
                        return returnlist
       
 #takes 9813.104315393149 seconds
def dictattack(filein,dictionary):
    starttime = time.time()
    hashlist=[]
    returnlist = []
    memolist3=[]
    memolist4=[]
    memolist5=[]
    found=0
    numbers="1234567890"
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        for line in fin:
            hashlist.append(line[:-1])
    with open(dictionary, mode="r", encoding='utf-8', newline='\n') as fin:
        for line in fin:
            guess = line[:-1]
            for line in hashlist:
                if line == hashlib.md5(bytearray(guess,encoding="utf-8")).hexdigest():
                    print(str(guess)+" found!")
                    returnlist.append(guess)
                    if found!=14:
                        found+=1
                    else:
                        totaltime = time.time()-starttime
                        print("Total time taken for dictionary attack: " + str(totaltime))
                        return returnlist
                else:
                    guess = ''.join(sorted(list(line[:-1])))
                    if guess not in memolist5:
                        memolist5.append(guess)
                        for word in it.product(guess,repeat=5):
                            word="".join(word)
                            if line == hashlib.md5(bytearray(word,encoding="utf-8")).hexdigest():
                                print(str(word)+" found!")
                                returnlist.append(word)
                                if found!=14:
                                    found+=1
                                else:
                                    totaltime = time.time()-starttime
                                    print("Total time taken for dictionary attack: " + str(totaltime))
                                    return returnlist 
                            if guess[0:4] not in memolist4:
                                memolist4.append(guess[0:4])
                                for i in range(10):
                                    for word in it.product(guess[0:4]+str(i),repeat=5):
                                        word="".join(word)
                                        if line == hashlib.md5(bytearray(word,encoding="utf-8")).hexdigest():
                                            print(str(word)+" found!")
                                            returnlist.append(word)
                                            if found!=14:
                                                found+=1
                                            else:
                                                totaltime = time.time()-starttime
                                                print("Total time taken for dictionary attack: " + str(totaltime))
                                                return returnlist
                            if guess[1:5] not in memolist4:
                                memolist4.append(guess[1:5])
                                for i in range(10):
                                    for word in it.product(guess[1:5]+str(i),repeat=5):
                                        word="".join(word)
                                        if line == hashlib.md5(bytearray(word,encoding="utf-8")).hexdigest():                             
                                            print(str(word)+" found!")
                                            returnlist.append(word)
                                            if found!=14:
                                                found+=1
                                            else:
                                                totaltime = time.time()-starttime
                                                print("Total time taken for dictionary attack: " + str(totaltime))
                                                return returnlist
                            if guess[0:3] not in memolist3:
                                memolist4.append(guess[0:3])
                                for i in range(10):
                                    for j in range(10):
                                        for word in it.product(guess[0:3]+str(i)+str(j),repeat=5):
                                            word="".join(word)
                                            if line == hashlib.md5(bytearray(word,encoding="utf-8")).hexdigest():
                                                print(str(word)+" found!")
                                                returnlist.append(word)
                                                if found!=14:
                                                    found+=1
                                                else:
                                                    totaltime = time.time()-starttime
                                                    print("Total time taken for dictionary attack: " + str(totaltime))
                                                    return returnlist                                
                            if guess[1:4] not in memolist3:
                                memolist4.append(guess[1:4])
                                for i in range(10):
                                    for j in range(10):
                                        for word in it.product(guess[1:4]+str(i)+str(j),repeat=5):
                                            word="".join(word)
                                            if line == hashlib.md5(bytearray(word,encoding="utf-8")).hexdigest():
                                                print(str(word)+" found!")
                                                returnlist.append(word)
                                                if found!=14:
                                                    found+=1
                                                else:
                                                    totaltime = time.time()-starttime
                                                    print("Total time taken for dictionary attack: " + str(totaltime))
                                                    return returnlist           
                            if guess[2:5] not in memolist3:
                                memolist4.append(guess[2:5])
                                for i in range(10):
                                    for j in range(10):
                                        for word in it.product(guess[2:5]+str(i)+str(j),repeat=5):
                                            word="".join(word)                                            
                                            if line == hashlib.md5(bytearray(word,encoding="utf-8")).hexdigest():
                                                print(str(word)+" found!")
                                                returnlist.append(word)
                                                if found!=14:
                                                    found+=1
                                                else:
                                                    totaltime = time.time()-starttime
                                                    print("Total time taken for dictionary attack: " + str(totaltime))
                                                    return returnlist                                            
                                                
def salting(filein,fileout,passwordout,hashout):
    passwordlist=['egunb',
 'tthel',
 'tpoin',
 'owso9',
 'opmen',
 'ofror',
 'aseas',
 'sso55',
 'di5gv',
 'dsmto',
 'hed4e',
 'lou0g',
 'cance',
 'nized',
 'mlhdi']
    pout = open(passwordout, mode='w+', encoding='utf-8', newline='\n')
    fout = open(fileout, mode='w+', encoding='utf-8', newline='\n')
    hout = open(hashout, mode='w+', encoding='utf-8', newline='\n')
    for i in passwordlist:
        rstring = random.choice(string.ascii_lowercase)
        newhash=hashlib.md5(bytearray(i+rstring,encoding="utf-8")).hexdigest()
        fout.write(rstring)
        fout.write(",")
        fout.write(newhash)
        fout.write("\n")
        pout.write(i+rstring)
        pout.write("\n")
        hout.write(newhash)
        hout.write("\n")
    pout.close()
    fout.close()
    hout.close()
    
if __name__=="__main__":
    bruteforce("hash5.txt")
    dictattack("hash5.txt","words5.txt")
    salting("hash5.txt","salted6.txt","password.txt","salted_hash.txt")
    # salted6.txt contains both the hash values and the salt since that is what the pdf asked us to do, but I need a salted_hash.txt which contains only the new hashes to be decrypted