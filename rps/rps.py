import random

def rps():
    user = input("Enter (r)ock, (p)aper, or (s)cissors: ").lower()
    cpu = random.choice(["r", "p", "s"])

    if user == cpu:
        print("Tie!")
    elif user == "r":
        if cpu == "p":
            print("CPU picked paper so you lost!")
        else:
            print("CPU picked scissors so you won!")
    elif user == "p":
        if cpu == "r":
            print("CPU picked rock so you won!")
        else:
            print("CPU picked scissors so you lost!")
    elif user == "s":
        if cpu == "r":
            print("CPU picked rock so you lost!")
        else:
            print("CPU picked paper so you won!")
    else:
        print("You were supposed to enter either r, p, or s!")

rps()
