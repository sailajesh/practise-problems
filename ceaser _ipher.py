alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
     'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def ceaser(plain_text,directions,shift_position):
    new_text=""
    shift_position=shift_position % 26
    if directions == "decode":
        shift_position = shift_position * -1
    for char in plain_text:
        if char in alphabet:
            position1 = alphabet.index(char)
            new_position=position1+shift_position
            new_text=new_text+alphabet[new_position]
        else:
            new_text=new_text+char
    print(f"the {directions} code is {new_text}")
continue_= True
while continue_ :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(plain_text=text,directions=direction,shift_position=shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        continue_ = False
        print("Goodbye")

