import random
import array

int_array = array.array("i", [0, 0, 0, 0, 0, 0, 0])
oldrando = 0
currando = 0
TRIES = 1000
FREQUENCY = 5
LOWLIMIT = 1
HILIMIT = 6

# try for TRIES times
for x in range(0, TRIES):
    # pick a random number
    currando = random.randint(LOWLIMIT, HILIMIT)
    # is this a repeat rando?
    if currando == oldrando:
        # increment rando counter for that number
        int_array[currando] = int_array[currando] + 1
        # alert when we're almost there
        if int_array[currando] == (FREQUENCY - 1):
            print(f"{int_array[currando]} in a row in {x} tries for number {currando}")
    else:
        # reset rando counter for that number
        int_array[currando] = 0

    # rmember the current rando number for the next loop
    oldrando = currando

    try:
        # have there been FREQUENCY rando numbers in a row?
        print(
            f"Found {FREQUENCY} in a row on try {x-FREQUENCY} through {x} for number {int_array.index(FREQUENCY)}"
        )
        break
    except ValueError as ve:
        # No, not yet
        continue

print(int_array)
