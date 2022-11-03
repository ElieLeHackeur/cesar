def code_cesar(nb, code):
    fin =""
    for i in range(len(code)):
        index=code[i]
        index=ord(index)
        index+=1
        index=chr(index)
        fin+=index
    print("Votre phrase chiffrée :", fin)

def uncode_cesar(nb, code):
    fin=""
    for i in range(len(code)):
        index=code[i]
        index=ord(index)
        index-=1
        index=chr(index)
        fin+=index
    print("Votre phrase déchiffrée :", fin)


code_cesar(nb, "phrase a chiffrer")
uncode_cesar(1, "phrase a dechiffrer")
