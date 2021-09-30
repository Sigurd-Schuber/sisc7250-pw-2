def splash():
#Startscreen splash
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon\n")
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
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
    else:
        return False

def new_targets():
#This function crates a new list of open targets.
    new_targets = []
    for x in range(5):
        new_targets.append(open())
    return(new_targets)

# def new_targets():
# #This function is a less elegant solution to do the same.
#     return [open(), open(), open(), open(), open()]

ts = new_targets()

#target:   indexet för ett mål på tavlan
#targets:  listan med mål på tavlan
#ts:       funktionen som öppnar en ny fräsch måltavla

def close_target(target, targets):
    targets[target] = closed()
    return targets

def hits(targets):
    n = 0
    for x in targets:
        if x == closed():
            n = n + 1
    return n

def target_to_string(target):
#Funktion som "översätter" vårt binära open/close till
#visuell representation
    if is_open(target) is True:
        return "* "
    elif is_closed(target) is True:
        return "O "



def targets_to_string(targets):
#Funktion som översätter måltavlans binära sträng till en visuell sträng
    s = []
    for element in targets:
        if is_open(element) is True:
            s.append("* ")
        elif is_closed(element) is True:
            s.append("O ")
    return s


