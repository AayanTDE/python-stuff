def rate(phrase):
    base = 0
    for letter in phrase:
        if letter == "A" or letter == "a":
            base += 1
        if letter == "B" or letter == "b":
            base += 2
        if letter == "C" or letter == "c":
            base += 3
        if letter == "D" or letter == "d":
            base += 4
        if letter == "E" or letter == "e":
            base += 5
        if letter == "F" or letter == "f":
            base += 6
        if letter == "G" or letter == "g":
            base += 7
        if letter == "H" or letter == "h":
            base += 8
        if letter == "I" or letter == "i":
            base += 9
        if letter == "J" or letter == "j":
            base += 10
        if letter == "K" or letter == "k":
            base += 11
        if letter == "L" or letter == "l":
            base += 12
        if letter == "M" or letter == "m":
            base += 13
        if letter == "N" or letter == "n":
            base += 14
        if letter == "O" or letter == "o":
            base += 15
        if letter == "P" or letter == "p":
            base += 16
        if letter == "Q" or letter == "q":
            base += 17
        if letter == "R" or letter == "r":
            base += 18
        if letter == "S" or letter == "s":
            base += 19
        if letter == "T" or letter == "t":
            base += 20
        if letter == "U" or letter == "u":
            base += 21
        if letter == "V" or letter == "v":
            base += 22
        if letter == "W" or letter == "w":
            base += 23
        if letter == "X" or letter == "x":
            base += 24
        if letter == "Y" or letter == "y":
            base += 25
        if letter == "Z" or letter == "z":
            base += 26
    print("Your sexiness is", str(base) + "!")

person = input("Enter name of person: ")
rate(person)
