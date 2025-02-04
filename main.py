# import the necessary packages

import art
print(art.logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# this project was completed in several steps but this will be the final iteration of the project.


# create a caesar funtion that takes in three different parameters, text, shift, and direction
def caesar(original_text, shift_amount , encode_or_decode):
    # create a variable to store the final text 
    output_text = ""

    # create a for loop to iterate through the text
    # but first we need to check of the direction is encode or decode
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # check to see if the letter is in the alphabet
        if letter not in alphabet:
            output_text += letter
        else:
            # find the position of the letter in the alphabet and shift it by the user input
            shifted_position = alphabet.index(letter) + shift_amount
            # check to see if the shifted position is out of range
            shifted_position %= len(alphabet)
            # add the shifted letter to the output text
            output_text += alphabet[shifted_position]
    print(f"The {encode_or_decode}d text is: {output_text}")


# we check to see if the user wants to continue using the program, so that it may loop again and again
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Have a nice day!")