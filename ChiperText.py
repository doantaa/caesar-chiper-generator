from ChiperArt import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount, chiper_direction):
    result_text = ""
    if chiper_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        if not letter in alphabet:
            result_text += letter
        else: 
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            result_text += alphabet[new_position] 
    print(f"Here's the {direction}d result: {result_text}")
    
print(logo)
run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input_text=text, shift_amount=shift, chiper_direction=direction)
    is_run = input("Type 'yes' if you want to go again. Otherwise, type 'no' : \n")
    if is_run == 'no':
        print("Goodbye")
        run = False
