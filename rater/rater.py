def char_to_numb(char):
    if char in "qwertyuiopasdfghjklzxcvbnm":
        return ord(char[0]) - 96
    elif char == " ":
        return 0
    else:
        return

def rate(phrase):
    base = 0
    for i in phrase:
        base += char_to_numb(i)
    return base

try:
    print(rate(input("Enter person to be rated: ")))
except TypeError:
    print("A name can only have letters in it!")