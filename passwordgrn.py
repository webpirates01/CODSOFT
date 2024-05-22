import random
import string

def USER_INPUT():
    try:
        length = int(input("ENTER THE DESIRED LENGTH OF PASSWORD: "))
        if length <= 0:
            print("ERROR: INVALID PASSWORD LENGTH")
            return None, None
    except ValueError:
        print("ERROR: INVALID INPUT FOR PASSWORD LENGTH")
        return None, None

    try:
        diffi_level = int(input("ENTER THE DESIRED DIFFICULTY OF THE PASSWORD\nLEVEL '1'BASIC \nLEVEL '2'NORMAL \nLEVEL '3'HARD\n<--->\n"))
        if diffi_level not in [1, 2, 3]:
            print("ERROR: WRONG DIFFICULTY LEVEL")
            return None, None
    except ValueError:
        print("ERROR: INVALID INPUT FOR DIFFICULTY LEVEL")
        return None, None

    return length, diffi_level

def generate_password(length, difficulty):
    if difficulty == 1:
        characters = string.digits
    elif difficulty == 2:
        characters = string.ascii_letters + string.digits
    elif difficulty == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length, diffi_level = USER_INPUT()
if length is not None and diffi_level is not None:
    password = generate_password(length, diffi_level)
    print(f"Generated password: {password}")
