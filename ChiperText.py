import random


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    chiper_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        chiper_position = position + shift_amount
        if chiper_position >= 26:
            chiper_position -= 26
        chiper_text += alphabet[chiper_position]
    print(f"The encoded text is: {chiper_text}")

def decrypt(chiper_text, shift_amount):
    plain_text = ""
    for letter in chiper_text:
        position = alphabet.index(letter)
        plain_position = position - shift_amount
        plain_text += alphabet[plain_position]
    print(f"The decode text is: {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(chiper_text=text, shift_amount=shift)
else:
    print("You type the wrong choice")