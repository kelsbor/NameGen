import random

print('Hello!')
print('')
vowels = ["a","e","i","o","u","y"]
consonants = ["q","w","r","t","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
def construct():
    sequence = input("Insert the sequence, v for vowels and c for consonants: ")
    times = int(input('How many words do you want?: '))
    while times >= 1:
        word = ""
        for i in sequence:
            if i == "v":
                word += vowels[random.randint(0,5)]
            if i == "c": 
                word += consonants[random.randint(0,19)]
        print(word.capitalize())
        times -= 1
        
    exit_back = input("Do you want exit? (y or n): ")
    if exit_back == "y":
        exit()
    if exit_back == "n":
        construct()
construct()
