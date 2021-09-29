def splash():
#Startscreen splash
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print("")
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    return None

def open():
#We assign an open target the integer 0
    return 0

def closed():
#We assign a closed target the integer 1
    return 1

a = open() #The variable a represents a target, indicates open target
b = closed() #The variable b b represents a target, indicates a closed target

def is_open(target):
#This function checks if a target is open
    if target == open():
        return True
    else:
        return False

def is_closed(target):
#This function checks if a target is closed
    if target == closed():
        return True
    elif target==open():
        return False

