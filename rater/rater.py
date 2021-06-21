def rate(phrase):
    base = 0
    for letter in phrase:
        if letter == "A":
            base += 1
        if letter == "B":
            base += 2
        if letter == "C":
            base += 3
        if letter == "D":
            base += 4
        if letter == "E":
            base += 5
        if letter == "F":
            base += 6
        if letter == "G":
            base += 7
        if letter == "H":
            base += 8
        if letter == "I":
            base += 9
        if letter == "J":
            base += 10
        if letter == "K":
            base += 11
        if letter == "L":
            base += 12
        if letter == "M":
            base += 13
        if letter == "N":
            base += 14
        if letter == "O":
            base += 15
        if letter == "P":
            base += 16
        if letter == "Q":
            base += 17
        if letter == "R":
            base += 18
        if letter == "S":
            base += 19
        if letter == "T":
            base += 20
        if letter == "U":
            base += 21
        if letter == "V":
            base += 22
        if letter == "W":
            base += 23
        if letter == "X":
            base += 24
        if letter == "Y":
            base += 25
        if letter == "Z":
            base += 26
    print("Your sexiness is", str(base) + "!")

person = input("Enter name of person: ")
rate(person.upper())
