"""
cryptography.py
Author: Tristan Meyer
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

options = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if options == "e":
    message = str(input("Message: "))
    key = str(input("Key: "))
    for a in message:
        nmessage = str(associations.find(a))
        for b in key:
            nkey = str(associations.find(b))
            z = zip(nmessage,nkey)
            for x in z:
                print(x[0],x[1])
    
#-------------------------------------------------------------------------------
if options == "d":
    nmessage = input("Message: ")
    nkey = input("Key: ")
    
#-------------------------------------------------------------------------------
if options == "q":
    print("Goodbye!")
    
if options != "e" and options != "d" and options != "q":
    print("Did not understand command, try again.")




