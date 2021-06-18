def owoify(str):
    translate = ""
    for i in str:
        if i in "RL":
            translate += "W"
        elif i in "rl":
            translate += "w"
        else:
            translate += i
    return translate

phrase = input("Enter phrase to be owoified: ")
print(owoify(phrase))
