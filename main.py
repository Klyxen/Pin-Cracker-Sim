#This is the main Script for Pin cracker
pin = "284"

#Checks the length of the pin
pin_len = len(pin)

#Finds the password and bases the length of the given pin
for pin in range(10 ** pin_len):
    guess = str(pin).zfill(pin_len) 
    print(f"Trying PIN: {guess}")
    if guess == pin:
        print(f"PIN found! : {guess}")
        break
