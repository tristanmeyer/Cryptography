"""
cryptography.py
Author: Tristan Meyer
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations.find(char)
print(associations)

options = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if options == "e":
    message = input("Message: )
    key = input("Key: )
    
#-------------------------------------------------------------------------------
if options == "d":
    emessage = input("Message: )
    dkey = input("Key: )
    
#-------------------------------------------------------------------------------
if options == "q":
    
if options != "e" and options != "d" and options != "q":
    print("Did not understand command, try again."



