"""
cryptography.py
Author: Tristan Meyer
Credit: https://www.dreamincode.net/forums/topic/214465-add-two-lists/

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"



options = input("Enter e to encrypt, d to decrypt, or q to quit: ")

t = []
m = []
s = ""
if options == "e":
    message = list(input("Message: "))
    lmessage = len(message)
    key = list(input("Key: "))
    nnkey = key * lmessage
    for a in message:
        nmessage = associations.find(a)
        t.append(nmessage)
    for b in nnkey:
        nkey = associations.find(b)
        m.append(nkey)
    c = [(t + m) for t, m in zip(t, m)]
    for d in c:
        e = ''.join([associations[f % len(associations)] for f in c])
    print(e)

    
#-------------------------------------------------------------------------------
if options == "d":
    message = list(input("Message: "))
    lmessage = len(message)
    key = list(input("Key: "))
    nnkey = key * lmessage
    for a in message:
        nmessage = associations.find(a)
        t.append(nmessage)
    for b in nnkey:
        nkey = associations.find(b)
        m.append(nkey)
    c = [(t - m) for t, m in zip(t, m)]
    for d in c:
        e = ''.join([associations[f % len(associations)] for f in c])
    print(e)

if options == "d" or options == "e": 
    options = input("Enter e to encrypt, d to decrypt, or q to quit: ")

    
#-------------------------------------------------------------------------------
if options == "q":
    print("Goodbye!")
    
if options != "e" and options != "d" and options != "q":
    print("Did not understand command, try again.")
    options = input("Enter e to encrypt, d to decrypt, or q to quit: ")




