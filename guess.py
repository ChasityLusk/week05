import math

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))


maxGuesses = int(math.log(high - low + 1, 2))
if 2 ** maxGuesses < (high - low + 1):
    maxGuesses += 1

print(f"I can guess your number in at most {maxGuesses} tries.")

count = 0
cheating = False

while low <= high:
    count += 1
    guess = (low + high) // 2
    print(f"My guess is {guess}")

    response = input("Is it too high (H), too low (L), or correct (C)? ").strip().upper()
    
    if response == "C":
        print(f"I guess your number in {count} tries!")
        break
    elif response == "H":
        high = guess - 1
    elif response == "L":
        low = guess + 1
    else:
        print("Please enter only H, L, or C.")
        count -= 1
        contiue

    if low > high:
        cheating = True
        break
    if cheating:
        print("Something doesn't add up! You might have given hints!")

        
